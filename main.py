# Tool made by Lawxsz!! <3, @Lawxsz on github/telegram
# New updates soon!!

import json, requests, os
from time import sleep
from colorama import Fore

os.system('cls')

with open("data.json", "r") as df:
    data = json.load(df)

version_checkk = requests.get("https://raw.githubusercontent.com/Lawxsz/LawX/main/data.json").json()
current_version = version_checkk['LawX']

def check_version():
 if data['LawX'] == current_version:
    print(f"{Fore.LIGHTGREEN_EX}Welcome to LawX MultiTool!!\nFollow Me on Github.com/Lawxsz")
    sleep(2)
    menu()
 else:
     print(f"{Fore.LIGHTCYAN_EX}New Version Available! {Fore.LIGHTGREEN_EX}https://github.com/Lawxsz/LawX")    
     sleep(5)
     menu()
def menu():
 os.system('cls')
 print(f"""{Fore.LIGHTRED_EX}
.____                  ____  ___    ___________           .__    
|    |   _____ __  _  _\   \/  /    \__    ___/___   ____ |  |   
|    |   \__  \\ \/ \/ /\     /       |    | /  _ \ /  _ \|  |   
|    |___ / __ \\     / /     \       |    |(  <_> |  <_> )  |__ 
|_______ (____  /\/\_/ /___/\  \      |____| \____/ \____/|____/ 
        \/    \/             \_/                                 
""")
 print(f"""
{Fore.LIGHTCYAN_EX}|======================================================|
{Fore.LIGHTMAGENTA_EX} 1. Scrapping (IDS) | 2. Mass Friend Request (BETA)
{Fore.LIGHTCYAN_EX}|=====================================================| 
\n{Fore.YELLOW}Guide in github.com/Lawxsz/LawX
""")
 ask = input(f"{Fore.LIGHTMAGENTA_EX}Choice: ")

 if ask == "1":
    from scrapping import save
    
    print("Do you need a token, guild for scrapping!, put it in data.json\n")
    save()
    sleep(3)
    
    os.system('cls')
    print(f"\n{Fore.LIGHTGREEN_EX}¡Done! (saved in users.txt)")
    askt = input(f"{Fore.LIGHTYELLOW_EX}¿Go to main menu? {Fore.LIGHTMAGENTA_EX}(y/n): ")
    if askt == "y" or "Y":
        menu()
    elif askt == "N" or "n":
        exit()
 elif ask == "2":
    from friendreq import friendreq

    print(f"{Fore.LIGHTGREEN_EX}Do you need a token for this, configure in data.json")
    friendreq()
    os.system('cls')
    print("\n\nDone!!")
 else:
  print(f"{Fore.LIGHTRED_EX}Invalid choice!")
  sleep(2)
  menu()

check_version()