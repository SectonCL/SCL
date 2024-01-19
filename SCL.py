print("Loading...")
locpal = locals.def_locale
import os
import sys
import random

import locals
import info
try:
    import termcolor
    from termcolor import colored
    import webbrowser
    import subprocess
except ModuleNotFoundError:
    print(locpal[24])
    answer = str(input("[Y/N]: "))
    if answer.lower().startswith("y"):
        os.system("pip3 install termcolor webbrowser subprocess")
        print(locpal[25])
    else:
        quit(2)



dFileInsides = ""
cantClear = False
autoClear = False
scriptmode = False
plilibs = []
cmds = {}
receiver = ["f"]       # Received output including everything
noCmdReceiver = "yes"  # Received output without the first word, NOT a list.
curPath = "C:/" if os.name == 'nt' else "/"
usrvars = {
    "test": "Nothin' to see here."
}

try:
    os.system('cls' if os.name == 'nt' else 'clear')
except Exception:
    print(locpal[0])
    cantClear = True



def regcommand(name: str, desc: str = locpal[1]):
    global cmds
    cmds[name] = desc



def aftermath():
    global receiver
    global noCmdReceiver
    global usrvars
    receiver = str(input(colored("S", "blue") + colored("C", "green") + colored("L", "red") + ": "))
    receiver = receiver.split(" ")  # Splitting to get every args

    # ARGUMENTS
    for index, arg in enumerate(receiver):
        if arg.__contains__("{var:"):
            modified_arg = arg.replace("{var:", "")
            try:
                receiver[index] = usrvars[modified_arg] # This works now
            except KeyError as bigE:
                print(f"{locpal[2]} {bigE}!")
        elif arg.__contains__("{rand:"):
            modified_arg = arg.replace("{rand:", "")
            modified_arg = modified_arg.split(",", 1)
            print(modified_arg)
            try:
                receiver[index] = str(random.randrange(random.randrange(int(modified_arg[0]), int(modified_arg[1]))))
            except Exception:
                receiver.pop(index)
                print(locpal[23])

    noCmdReceiver = " ".join(receiver[1:]).replace(">[",   curPath)
    commander()


# COMMANDS
def commander():
    global curPath
    global receiver
    global noCmdReceiver
    global autoClear
    global scriptmode
    global cantClear
    global locpal

    if autoClear:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            print(locpal[3])
            autoClear = False

    match receiver[0]:
        case "type":
            print(noCmdReceiver)


        case "sp":
            print(os.path.dirname(curPath) + ":")
            for elem in os.listdir(curPath):
                if os.path.isdir(curPath + elem):
                    print(f"{locpal[4]} {elem}")
                elif os.path.islink(curPath + elem):
                    print(f"{locpal[5]} {elem}")
                elif os.path.isfile(curPath + elem):
                    print(f"{locpal[6]} {elem}")
                elif os.path.isabs(curPath + elem):
                    print(f"{locpal[7]} {elem}")
                elif os.path.ismount(curPath + elem):
                    print(f"{locpal[8]} {elem}")
                else:
                    print(f"{locpal[9]} {elem}")
        case "cp":
            if os.path.isdir(noCmdReceiver):
                curPath = noCmdReceiver
            else:
                print(locpal[10])

        case "dbg":
            print(receiver[1])


        case "stop":
            print(locpal[11])
            sys.exit(0)


        case "clr":
            if not cantClear and noCmdReceiver == "":
                try:
                    os.system('cls' if os.name == 'nt' else 'clear')
                except Exception:
                    print(locpal[3])
            elif not cantClear and noCmdReceiver == "1":
                print(locpal[13])
                autoClear = True
            elif not cantClear and noCmdReceiver == "0":
                print(locpal[14])
                autoClear = False

        case "var":
            if receiver[1] == "set":
                usrvars[receiver[2]] = " ".join(receiver[3:])
            try:
                if receiver[1] == "remove":
                    usrvars.pop(receiver[2])
                elif receiver[1] == "read":
                    print(usrvars[receiver[2]])
                elif receiver[1] == "input":
                    usrvars[receiver[2]] = input(str(receiver[2]) + ": ")
            except Exception:
                print(locpal[15])

        case "sectonfetch":
            import screeninfo
            import platform
            def grscb(text: str):
                print(colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])),
                      colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])),
                      colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])), text)
            print(colored("██ ██ ██ ██ ██ ██", "green"), f" {locpal[22][0]}: {os.getlogin()}@{platform.node()}")
            print(colored("██", "blue"), f"                {locpal[22][1]}: {platform.system()} {platform.release()}")
            print(colored("██   ", "blue"), colored("██", "red"), colored("██", "green"), f"       {locpal[22][2]}: {platform.release()}")
            print(colored("      ██", "blue"), colored("      ██ ", "red"), f"{locpal[22][3]}: {os.popen('uptime -p').read()[:-1]}")
            savememon = ""
            for mon in screeninfo.get_monitors():
                if mon.is_primary: savememon = mon
            print(colored("               ██ ", "red"), f"{locpal[22][4]}: {savememon.width}x{savememon.height}")
            print(colored("██ ██ ██ ██ ██ ██", "blue"), f" {locpal[22][5]}: {platform.architecture()[0]}")
            grscb(f" {locpal[22][6]}: {platform.processor()}")
            total_memory, used_memory, free_memory = map(
                int, os.popen('free -t -m').readlines()[-1].split()[1:])
            grscb(f" {locpal[22][7]}: {used_memory}/{total_memory} MB")
            grscb(f" Python: {platform.python_version()}")
            grscb(f" {locpal[22][8]}: Secton")
            grscb(f" SCL {locpal[22][9]}: {info.version}")
            grscb(locpal[22][10])
            for color in termcolor.COLORS:
                print(colored("█", color), end="", flush=True)

        case "think":
            print("Always think twice.")
            webbrowser.open("https://youtu.be/Bxc4Fvs3Mmo")

        case "url":
            webbrowser.open(noCmdReceiver)

        case "help":
            subprocess.Popen(["python3", "./windows/SCLHelp/sclhelp.py"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        case "lang":
            try:
                if locals.lookup(receiver[1]) is True:
                    locals.change(receiver[1])
                    locpal = locals.def_locale
                    try:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    except Exception:
                        print(locpal[0])
                        cantClear = True
                    print(locpal[17])
            except Exception:
                print(locpal[21])


        case "": print("lol ok")
        case _:
            print(locpal[16])

    if not scriptmode:
        aftermath()



def execscript():
    global receiver
    global noCmdReceiver
    for lining in dFileInsides:
        receiver = " ".split(lining)
        noCmdReceiver = receiver[1:]
        commander()


if len(sys.argv) > 1:
    print(locpal[17])
    dFileInsides = open(sys.argv[1], "r")
    for line in dFileInsides:
        if line.startswith("py "):
            print(locpal[19])
            choice = int(input(locpal[20]))
            if choice <= 0:
                receiver = "stop"
                commander()
            elif choice == 1:
                execscript()
            else:
                for lin2 in dFileInsides:
                    if line.startswith("py "):
                        print(line.removeprefix("py "))
                choice = int(input(locpal[20]))
                if choice <= 0:
                    receiver = "stop"
                    commander()
                elif choice == 1:
                    execscript()
            break
else:
    print(locpal[17])
    # droppedFile = ""

aftermath()