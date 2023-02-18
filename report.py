import requests, json
from colorama import Fore

with open("data.json", "r") as df:
    data = json.load(df)



def sendn():
    guild_id = input("Guild/Server ID: ")
    channel_id = input("Channel ID: ")
    message_id = input("Message ID: ")
    print(f"""\n
    {Fore.LIGHTGREEN_EX}Reason:\n
    Ilegal content: 1
    Harrassment: 2
    Spam/Pishing/Relationated: 3
    Self harm: 4
    NSFW Content: 5
    \n""")
    reasonn = input("Reason (number): ")
    heardst = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': data['token'],
        'Content-Type': 'application/json'
    }
    reasons = {
     'channel_id': channel_id,
     'guild_id': guild_id,
     'message_id': message_id,
     'reason': reasonn
    }
    r = requests.post('https://discord.com/api/v6/report', headers=heardst, json=reasons)
    print(r)
    if r == 201:
        print(f'{Fore.LIGHTGREEN_EX} Report Sent!')
    else:
        print("Token invalid!")
def sendm():
    guild_id = input("Guild/Server ID: ")
    channel_id = input("Channel ID: ")
    message_id = input("Message ID: ")
    print(f"""\n
    {Fore.LIGHTGREEN_EX}Reason:\n
    Ilegal content: 1
    Harrassment: 2
    Spam/Pishing/Relationated: 3
    Self harm: 4
    NSFW Content: 5
    \n""")
    reasonn = input("Reason (number): ")
    heardst = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': data['token'],
        'Content-Type': 'application/json'
    }
    reasons = {
     'channel_id': channel_id,
     'guild_id': guild_id,
     'message_id': message_id,
     'reason': reasonn
    }
    count = 0
    while count < 5:
     r = requests.post('https://discord.com/api/v6/report', headers=heardst, json=reasons)
     print(r)
     if r == 201:
        print(f'{Fore.LIGHTGREEN_EX} Report Sent!')
     else:
        print("Token invalid!")
     count+=1
