import os
import json
import datetime
import time , requests , random , string
import urllib
# from rainbowtext import text
# from colorama import Fore

# Random number 1-999
def rand_number():
    return str(random.randint(1,999))

# Random String
def rand_string(number):
    text = string.ascii_letters + string.digits
    result= ''.join(random.choice(text) for char in range(number))
    return result

def warp_unlimited(id_code, url):
    inst = rand_string(22)
    body = {
        "key": f"{rand_string(43)}=",
        "install_id": inst,
        "fcm_token": f"{inst}:APA91b{rand_string(134)}",
        "referrer": id_code,
        "warp_enabled": False,
        "locale": "es_US"
    }
    data = json.dumps(body).encode('utf8')
    header = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'okhttp/3.12.1'
        }
    try:
        req = urllib.request.Request(url , data , header)
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        time.sleep(5)
        
def main():
    session = requests.Session()
    url = f"https://api.cloudflareclient.com/v0a{rand_number()}/reg"
    
    
    # App > setting > advanced > diagnotics > ID
    #code_id = input("[+] Please Enter Your Client ID : ")
    code_id = "e787b50a-5727-4a4c-b908-b089b42512be"

    print(f"Getting warp...\nYour ID : {code_id}\n{'-'*20}")
    while True:
        try:
            warp_unlimited(code_id, url)
            print ("[+] Success ! You Got 1GB Warp + \n" + "[-] Please Wait 10 Second !")
            time.sleep(17)
            
        except KeyboardInterrupt:
            print ("Stopped ! ")

if __name__ == "__main__":
    main()
