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
BOT_TOKEN = '7730132849:AAGxRopXYWDKsK0kshMu8BIU2LkznOVj6ug' 
ADMIN_ID = 7954343626              

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    # User Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            credits INTEGER DEFAULT 0
        )
    ''')
    # Gateway Status Table (Gate တွေ ပိတ်/ဖွင့် သိမ်းရန်)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gate_status (
            gate_name TEXT PRIMARY KEY,
            is_active INTEGER DEFAULT 1
        )
    ''')
    # အစပိုင်းမှာ Gate အားလုံးကို ON (1) ထားမယ်
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

# Admin က Gate ကို ပိတ်/ဖွင့် လုပ်ရန်
# Usage: /gate au off သို့မဟုတ် /gate au on
async def control_gate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    
    try:
        gate_name = context.args[0].lower()
        action = context.args[1].lower()
        
        status = 1 if action == "on" else 0
        status_text = "ဖွင့်" if status == 1 else "ပိတ်"
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE gate_status SET is_active = ? WHERE gate_name = ?", (status, gate_name))
        conn.commit()
        
        if cursor.rowcount > 0:
            await update.message.reply_text(f"✅ Gateway **{gate_name}** ကို {status_text}လိုက်ပါပြီ။")
        else:
            await update.message.reply_text("❌ Gateway အမည် မှားနေပါသည်။")
        conn.close()
    except:
        await update.message.reply_text("Usage: `/gate [au/ad/az/ak] [on/off]`")

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
        await update.message.reply_text("✅ Register အောင်မြင်ပါသည်။")
    conn.close()
    
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        await update.message.reply_text(f"💰 သင့်ရဲ့လက်ကျန် Credit: {result[0]}")
    else:
        await update.message.reply_text("⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")

# --- Generic Check Logic ---
async def process_card_check(update: Update, context: ContextTypes.DEFAULT_TYPE, gate_func, gate_name):
    # ၁။ Gate ပိတ်ထားလား အရင်စစ်မယ်
    if not is_gate_on(gate_name):
        await update.message.reply_text(f"❌ Gateway **{gate_name}** သည် လောလောဆယ် ပြုပြင်ထိန်းသိမ်းနေသောကြောင့် ခေတ္တပိတ်ထားပါသည်။")
        return

    user_id = update.effective_user.id
    username = update.effective_user.username or "NoUsername"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT credits FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    
    if not result:
        await update.message.reply_text("⚠️ ကျေးဇူးပြု၍ အရင် /register လုပ်ပါ။")
        conn.close()
        return
    
    if result[0] <= 0:
        await update.message.reply_text("❌ သင့်မှာ Credit မလုံလောက်တော့ပါ။")
        conn.close()
        return

    if not context.args:
        await update.message.reply_text("⚠️ Card format လိုအပ်သည်။ ဥပမာ- `/au cc|mm|yy|cvc`", parse_mode="Markdown")
        conn.close()
        return

    cc = context.args[0]
    msg = await update.message.reply_text(f"Checking on Gateway {gate_name.upper()}...")
    start_time = time.time()

    try:
        last = str(gate_func(cc))
        if any(x in last.lower() for x in ["Successfully", "Thanks", "thank", "success"]):
            last = "Charged 💥"
        
        time_taken = round(time.time() - start_time, 2)
        send_response = send(cc, last, username, time_taken)

        # Credit လျှော့မယ်
        new_credits = result[0] - 1
        cursor.execute("UPDATE users SET credits = ? WHERE user_id = ?", (new_credits, user_id))
        conn.commit()

        await msg.edit_text(send_response, parse_mode="HTML")

    except Exception as e:
        logging.error(f"Error: {e}")
        await msg.edit_text(f"An error occurred: Try again.")
    
    conn.close()

# --- Gateway Commands ---
async def au_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_card_check(update, context, Tele, "au")

async def ad_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_card_check(update, context, Tele1, "ad")

async def az_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_card_check(update, context, Tele2, "az")
    
async def ak_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await process_card_check(update, context, Tele3, "ak")

# Admin Command
async def add_credit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    try:
        target_id, amount = int(context.args[0]), int(context.args[1])
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET credits = credits + ? WHERE user_id = ?", (amount, target_id))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"✅ User {target_id} ဆီသို့ {amount} Credits ထည့်ပြီးပါပြီ။")
    except:
        await update.message.reply_text("Usage: /add [ID] [Amount]")

# --- MAIN ---
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
    
    # Gateway Control Command (Admin Only)
    app.add_handler(CommandHandler("gate", control_gate))
    
    print("Bot is running with Gate Control System...")
    app.run_polling()
