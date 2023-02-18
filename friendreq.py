import requests, time, json
from time import sleep
from colorama import Fore

with open("data.json", "r") as df:
    data = json.load(df)

def friendreq():



 friends = 0
 headers = {
        "Authorization": f"{data['token']}"
    }


 payload = {'' : ''}
 with open("users.txt", "r") as ids:    
  for i in ids:
    r = requests.put(f"https://discordapp.com/api/v8/users/@me/relationships/{i}", headers=headers, json=payload)
    print(f"Response: {r}")
    sleep(2)
 if r.status_code == 200:
    friends += 1
    print(f"{Fore.GREEN}[Status]: {Fore.RESET} Succesfully sent friend request")
 elif f"{Fore.RED}[Error]: {Fore.RESET} Couldnt send a friend request" in r.text:
    print(f"{Fore.RED}Error.")
 elif r.status_code == 401:
    print(f"{Fore.RED}[Error]: {Fore.RESET} Invalid REQ/ID")
 time.sleep(2)

