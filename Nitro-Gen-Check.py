import random, string
import webbrowser
import time
import requests
import colorama
colorama.init()

print("\033[32m"+"""

▀████    ▐████▀    ▄█    █▄     ▄██████▄     ▄████████     ███        ▄████████    ▄████████ 
  ███▌   ████▀    ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███ 
   ███  ▐███      ███    ███   ███    ███   ███    █▀     ▀███▀▀██   ███    █▀    ███    ███ 
   ▀███▄███▀     ▄███▄▄▄▄███▄▄ ███    ███   ███            ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
   ████▀██▄     ▀▀███▀▀▀▀███▀  ███    ███ ▀███████████     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ▐███  ▀███      ███    ███   ███    ███          ███     ███       ███    █▄  ▀███████████ 
 ▄███     ███▄    ███    ███   ███    ███    ▄█    ███     ███       ███    ███   ███    ███ 
████       ███▄   ███    █▀     ▀██████▀   ▄████████▀     ▄████▀     ██████████   ███    ███ 
                                                                                  ███    ███        

""" "\033[37m" )

num=input('    ➤ Input How Many Codes You Want To Generate And Check: ')

f=open("Nitro Codes.txt", "w", encoding='utf-8')

print("\n" "꧁  " " Wait, Generating for You! ꧂" "\n")

for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("\033[32m" + " Valid | {} ".format(line.strip("\n")))
            break
        else:
            print("\033[31m" + " Invalid | {}".format(line.strip("\n")))
            print("\033[37m")
input("\n" '    ➤ The End! Press Enter Five Time To Quit')
input("\n" "Don't Forget To Subscribe ...")
input("\n" "Byeee")
input("\n" "Nigass")
input("\n" "Have Fun...")
