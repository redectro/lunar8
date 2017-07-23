#############
# Name: lunar8
# Description: A altcoin P&D trading bot.
# Author: Redectro
# Version: 1.0
#############

# Imports go here
import os
import glob
import ntpath
# Assign variables here
version = "1.0"
confile = "lunar8/lunar8.dat"
exchangeconf = "lunar8/exchanges"
############# Define functions here #################
##################### START #########################
def clear():
    print("\033[H\033[J")

def welcome():
    print("Welcome to lunar8 " + version + ".")
    print("---------")
    print("Exchange: " + CapExchange)
    print("---------")

def createdat():
    os.makedirs('lunar8/exchanges')
    clear()
    done = 0
    print("""Please configure lunar8's settings.
-----------------------------------
1) Choose your exchange.
        [1] Bittrex
        [2] Yobit
        [3] Cryptopia
""")
    while done != 1:
        done = 1
        c1 = input("Choice: ")
        if c1 == "1":
            print("2) Enter your Bittrex API key.")
            c2 = input("Key: ")
            c3 = input("Key secret: ")
        elif c1 == "2":
            print("2) Enter your Yobit API key.")
            c2 = input("Key: ")
            c3 = input("Key secret: ")
        elif c1 == "3":
            print("2) Enter your Cryptopia API key.")
            c2 = input("Key: ")
            c3 = input("Key secret: ")
        else:
            done = 0
        # Writing to file
    if c1 == "1":
        fname = "btrx"
    elif c1 == "2":
        fname = "ybt"
    else:
        fname = "crypt"

    f = open(exchangeconf + "/" + fname + ".dat", "w")
    f.write(c2 + "\n")
    f.write(c3)
    f.close()
    f = open(confile, "w")
    f.write(fname)
    f.close()

def importsettings():
    global exchange
    global key
    global keysec
    if os.path.isfile(confile) == True:
        f = open(confile, "r")
        setng = []
        for line in f:
            setng.append(line)
        f.close()

        exchange = str(setng[0])

        f = open(exchangeconf + "/" + exchange + ".dat", "r")
        apikey = []
        for line in f:
            line = line.rstrip()
            apikey.append(line)
        f.close()
        # Converting to variables
        exchange = setng[0]
        key = apikey[0]
        keysec = apikey[1]
    else:
        createdat()
        importsettings()


####################################### Settings block
def setexchange():
    clear()
    welcome()
    print("""[1] Add a exchange
[2] Select a exchange
[3] Remove a exchange
[4] Back
""")
    ans = True
    while ans:
        ans = True
        ch = input("Choice: ")
        if ch == "1":
            addexchange()
        elif ch == "2":
            selexchange()
        elif ch == "3":
            remexchange()
        elif ch == "4":
            settings()
        else:
            ans = False

def selexchange():
    clear()
    welcome()
    temp = []
    for f in glob.glob('lunar8/exchanges/*.dat'):
        f = os.path.splitext(ntpath.basename(f))[0]
        temp.append(f)
    list = []
    if "btrx" in temp:
        list.append("Bittrex")
    if "ybt" in temp:
        list.append("Yobit")
    if "crypt" in temp:
        list.append("Cryptopia")
    print(list)
    counter = 1
    counterl = 0
    dict = {}
    for f in list:
        print("[" + str(counter) + "] " + f)
        dict[counter] = f
        counter += 1
        counterl += 1
    print(dict)
    ch = input("Choice: ")
    dict[ch]
def settings():
    clear()
    welcome()
    print("""[1] Exchange settings
[2] Reset the app
[3] Back """)
    ans = True
    while ans:
        ans = False
        ch = input("Choice: ")
        if ch == "1":
            setexchange()
        elif ch == "2":
            os.remove(confile)
            createdat()
        elif ch == "3":
            mainmenu()
        else:
            ans = True


# Main code
importsettings()
if exchange == "btrx":
   CapExchange = "Bittrex"
elif exchange == "ybt":
   CapExchange = "Yobit"
elif exchange == "crypt":
   CapExchange = "Cryptopia"
else:
   exit()

def mainmenu():
    while True:
        clear()
        welcome()
        print('[1] Launch bot')
        print('[2] Settings')
        print('[3] Exit')
        done = 0
        while done != 1:
            done = 1
            a = input("Choice: ")
            if a == "1":
                startbot(exchange)
            elif a == "2":
                settings()
            elif a == "3":
                exit()
            else:
                done = 0

mainmenu()
