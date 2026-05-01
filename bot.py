import sqlite3
import logging
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# --- အရေးကြီးသွင်းကုန်များ ---
try:
    from gatet import Tele
    from gatet1 import Tele as Tele1
    from gatet2 import Tele as Tele2
    from gatet3 import Tele as Tele3
    from hit_sender import send
except ImportError as e:
    print(f"Error: ဖိုင်တစ်ခုခု လိုအပ်နေသည် - {e}")

# --- CONFIGURATION ---
BOT_TOKEN = '' 
ADMIN_ID = 7954343626              

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, credits INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS gate_status (gate_name TEXT PRIMARY KEY, is_active INTEGER DEFAULT 1)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS card_history (user_id INTEGER, cc_number TEXT, check_count INTEGER DEFAULT 0, PRIMARY KEY (user_id, cc_number))''')
    
    # ၂။ --- Database အဟောင်းထဲကို column အသစ်ပေါင်းထည့်တဲ့ အပိုင်း ---
    try:
        # last_check_time column မရှိသေးရင် ထည့်မယ်
        cursor.execute("ALTER TABLE card_history ADD COLUMN last_check_time INTEGER DEFAULT 0")
        conn.commit()
        print("Successfully updated database: Added last_check_time column.")
    except sqlite3.OperationalError:
        # Column ရှိပြီးသားဆိုရင် error တက်မှာဖြစ်လို့ ဒီအတိုင်း ကျော်သွားမယ်
        print("Column 'last_check_time' already exists. Skipping update.")
    
    gates = [('au',), ('ad',), ('az',), ('ak',)]
    cursor.executemany('INSERT OR IGNORE INTO gate_status (gate_name) VALUES (?)', gates)
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect('bot_database.db')

def is_gate_on(gate_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT is_active FROM gate_status WHERE gate_name = ?", (gate_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] == 1 if result else False

# --- BOT COMMANDS ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 မင်္ဂလာပါ! Yagami Light Checker မှ ကြိုဆိုပါတယ်။\n\n"
        "သုံးလို့ရတဲ့ Command များ -\n\n"
        "/register - အကောင့်ဖွင့်ပြီး Credit 10 ယူမယ်\n"
        "/balance - လက်ကျန် Credit စစ်မယ်\n"
        "/au - Gateway 1 နဲ့စစ်မယ် (1 Credit)\n"
        "/ad - Gateway 2 နဲ့စစ်မယ် (1 Credit)\n"
        "/az - Gateway 3 နဲ့စစ်မယ် (1 Credit)\n"
        "/ak - Gateway 4 နဲ့စစ်မယ် (1 Credit)\n\n"
        "ဆက်သွယ်ရန် - @strawhatchannel69"
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    if cursor.fetchone():
        await update.message.reply_text("❌ သင် register လုပ်ပြီးသားပါ။")
    else:
        cursor.execute("INSERT INTO users (user_id, credits) VALUES (?, ?)", (user_id, 10))
        conn.commit()
        await update.message.reply_text("✅ Register အောင်မြင်သည်။ Credit 10 ရရှိသည်။")
    conn.close()

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        await update.message.reply_text(f"💰 Balance: {result[0]}")
    else:
        await update.message.reply_text("⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")

# --- Logic with Correct 24-Hour Reset ---
async def process_card_check(update: Update, context: ContextTypes.DEFAULT_TYPE, gate_func, gate_name):
    if not is_gate_on(gate_name):
        await update.message.reply_text(f"❌ Gateway **{gate_name}** သည် လောလောဆယ် ပြုပြင်ထိန်းသိမ်းနေသောကြောင့် ခေတ္တပိတ်ထားပါသည်။")
        return

    user_id = update.effective_user.id
    username = update.effective_user.username or "NoUsername"
    
    if not context.args:
        await update.message.reply_text("⚠️ Card format မမှန်ကန်ပါ။ ဥပမာ- `/au cc|mm|yy|cvc`", parse_mode="Markdown")
        return

    cc = context.args[0]
    conn = get_db_connection()
    cursor = conn.cursor()

    # ၁။ User & Credit စစ်ဆေးခြင်း
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    
    if not user_data or user_data[0] <= 0:
        await update.message.reply_text("❌ သင့်မှာ Credit မလုံလောက်တော့ပါ။" if user_data else "⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")
        conn.close()
        return

    # ၂။ Duplicate Check Logic
    current_time = int(time.time())
    one_day_seconds = 24 * 60 * 60
    
    cursor.execute("SELECT check_count, last_check_time FROM card_history WHERE user_id = ? AND cc_number = ?", (user_id, cc))
    history = cursor.fetchone()

    if history:
        count, last_time = history
        # ၂၄ နာရီ မပြည့်သေးရင် Count စစ်မယ်
        if (current_time - last_time) < one_day_seconds:
            if count >= 3:
                remaining_time = one_day_seconds - (current_time - last_time)
                hours_left = remaining_time // 3600
                minutes_left = (remaining_time % 3600) // 60
                await update.message.reply_text(
                    f"❌ <b>Duplicate check founded!</b>\n\nဒီကတ်ကို ၂၄ နာရီအတွင်း ၃ ကြိမ်စစ်ပြီးသွားပါပြီ။ "
                    f"နောက်ထပ် <b>{int(hours_left)} နာရီ {int(minutes_left)} မိနစ်</b> နေမှ ပြန်စစ်ပေးပါ။", 
                    parse_mode="HTML"
                )
                conn.close()
                return
        else:
            # ၂၄ နာရီ ကျော်သွားပြီဆိုရင် Count ကို Reset ချမယ်
            cursor.execute("UPDATE card_history SET check_count = 0 WHERE user_id = ? AND cc_number = ?", (user_id, cc))
            conn.commit()

    msg = await update.message.reply_text(f"🔍 Processing your card...")
    start_time = time.time()

    try:
        # Gateway ကို စစ်ဆေးခြင်း
        last = str(gate_func(cc))
        
        # --- ဒီအပိုင်းမှာ Database ကို Update လုပ်တာ သေချာအောင် ပြင်ထားပါတယ် ---
        
        # (က) Count နဲ့ အချိန်ကို သိမ်းဆည်းခြင်း
        if history:
            # ရှိပြီးသားဆိုရင် count ကို ၁ တိုးမယ်၊ အချိန်ကို အခုအချိန်ပြောင်းမယ်
            cursor.execute(
                "UPDATE card_history SET check_count = check_count + 1, last_check_time = ? WHERE user_id = ? AND cc_number = ?", 
                (current_time, user_id, cc)
            )
        else:
            # အသစ်ဆိုရင် record အသစ်ဆောက်မယ်
            cursor.execute(
                "INSERT INTO card_history (user_id, cc_number, check_count, last_check_time) VALUES (?, ?, 1, ?)", 
                (user_id, cc, current_time)
            )

        # (ခ) Credit နှုတ်ခြင်း
        new_credits = user_data[0] - 1
        cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_credits, user_id))
        
        conn.commit() 

        # Result ပြသခြင်း
        if any(x in last.lower() for x in ["Successfully", "Thanks", "Thank", "thank", "success"]):
            last = "Charged 💥"
        
        time_taken = round(time.time() - start_time, 2)
        send_response = send(cc, last, username, time_taken)
        await msg.edit_text(send_response, parse_mode="HTML")

    except Exception as e:
        logging.error(f"Error: {e}")
        await msg.edit_text(f"❌ An error occurred: Try again.")
    
    conn.close()

# --- Gateway Commands ---
async def au_check(update: Update, context: ContextTypes.DEFAULT_TYPE): await process_card_check(update, context, Tele, "au")
async def ad_check(update: Update, context: ContextTypes.DEFAULT_TYPE): await process_card_check(update, context, Tele1, "ad")
async def az_check(update: Update, context: ContextTypes.DEFAULT_TYPE): await process_card_check(update, context, Tele2, "az")
async def ak_check(update: Update, context: ContextTypes.DEFAULT_TYPE): await process_card_check(update, context, Tele3, "ak")

async def add_credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    try:
        target_id, amount = int(context.args[0]), int(context.args[1])
        conn = get_db_connection(); cursor = conn.cursor()
        cursor.execute("UPDATE users SET credits = credits + ? WHERE user_id = ?", (amount, target_id))
        conn.commit(); conn.close()
        await update.message.reply_text(f"✅ User {target_id} +{amount} Credits.")
    except: await update.message.reply_text("Usage: /add [ID] [Amount]")

async def control_gate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    try:
        gate_name, action = context.args[0].lower(), context.args[1].lower()
        status = 1 if action == "on" else 0
        conn = get_db_connection(); cursor = conn.cursor()
        cursor.execute("UPDATE gate_status SET is_active = ? WHERE gate_name = ?", (status, gate_name))
        conn.commit(); conn.close()
        await update.message.reply_text(f"✅ Gateway {gate_name} {action}.")
    except: await update.message.reply_text("Usage: /gate [au/ad/az/ak] [on/off]")

if __name__ == '__main__':
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("au", au_check))
    app.add_handler(CommandHandler("ad", ad_check))
    app.add_handler(CommandHandler("az", az_check))
    app.add_handler(CommandHandler("ak", ak_check))
    app.add_handler(CommandHandler("add", add_credit))
    app.add_handler(CommandHandler("gate", control_gate))
    print("Bot is running...")
    app.run_polling()
