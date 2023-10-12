print("Загрузка...")
import os
import sys
import random
import termcolor
from termcolor import colored
import webbrowser

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
    "test": "Nice goin', partner."
}

try:
    os.system('cls' if os.name == 'nt' else 'clear')
except Exception:
    print("SCL не смогла очистить вывод под вашей ОС.")
    cantClear = True



def regcommand(name: str, desc: str = "Без описания."):
    global cmds
    cmds[name] = desc



def aftermath():
    global receiver
    global noCmdReceiver
    global usrvars
    receiver = str(input(colored("S", "blue") + colored("C", "green") + colored("L", "red") + ": "))
    receiver = receiver.split(" ")  # Splitting to get every args
    for index, arg in enumerate(receiver):
        if arg.__contains__("{var:"):
            modified_arg = arg.replace("{var:", "")
            try:
                receiver[index] = usrvars[modified_arg] # This works now
            except KeyError as bigE:
                print(f"Нет переменной {bigE}!")
    noCmdReceiver = " ".join(receiver[1:]).replace(">[",   curPath)
    commander()



def commander():
    global curPath
    global receiver
    global noCmdReceiver
    global autoClear
    global scriptmode

    if autoClear:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            print("SCL не поддерживает команды вашей ОС.\nАвто-очистка отключена.")
            autoClear = False

    regcommand("type")
    if receiver[0] == "type":
        print(noCmdReceiver)


    elif receiver[0] == "sp":
        print(os.path.dirname(curPath) + ":")
        for elem in os.listdir(curPath):
            if os.path.isdir(curPath + elem):
                print(f" ПАПКА: {elem}")
            elif os.path.islink(curPath + elem):
                print(f"ССЫЛКА: {elem}")
            elif os.path.isfile(curPath + elem):
                print(f"  ФАЙЛ: {elem}")
            elif os.path.isabs(curPath + elem):
                print(f"   АБС: {elem}")
            elif os.path.ismount(curPath + elem):
                print(f" МАУНТ: {elem}")
            else:
                print(f"НЕИЗВ.: {elem}")
    elif receiver[0].startswith("cp"):
        if os.path.isdir(noCmdReceiver):
            curPath = noCmdReceiver
        else:
            print("Такой директории не существует.")

    elif receiver[0].startswith("dbg"):
        print(receiver[1])


    elif receiver[0].startswith("stop"):
        print("Выхожу...")
        quit(0)

    elif receiver[0].startswith("py"):
        if receiver[1].startswith("exec"):
            """try:"""
            if not noCmdReceiver.__contains__("quit") and not noCmdReceiver.__contains__("exit"):
                pl_c = ""
                for lib in plilibs:
                    pl_c = pl_c + "import " + lib + "; "
                exec(str(pl_c) + " ".join(receiver[2:]))
            else:
                print("Ага ага... Сейчас!")
            """except Exception as excepting:
                print("Ошибка Python!\n" + str(excepting))
                pass"""
        elif receiver[1].startswith("lib"):
            if receiver[2] == "install":
                plilibs.append(receiver[3])
            elif receiver[2] == "remove":
                plilibs.remove(receiver[3])

    elif receiver[0].startswith("clr"):
        if not cantClear and noCmdReceiver == "":
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
            except Exception:
                print("SCL не поддерживает команды вашей ОС.")
        elif not cantClear and noCmdReceiver == "1":
            print("Включён режим авто-очистки.")
            autoClear = True
        elif not cantClear and noCmdReceiver == "0":
            print("Режим авто-очистки отключён.")
            autoClear = False

    elif receiver[0] == "var":
        if receiver[1] == "set":
            usrvars[receiver[2]] = " ".join(receiver[3:])
        try:
            if receiver[1] == "remove":
                usrvars.pop(receiver[2])
            elif receiver[1] == "read":
                print("Переменная " + str(receiver[2]) + " является:\n" + usrvars[receiver[2]])
            elif receiver[1] == "input":
                usrvars[receiver[2]] = input(str(receiver[2]) + " is: ")
        except Exception:
            print("Проверь правильность переменной!")

    elif receiver[0] == "sectonfetch":
        import screeninfo
        import platform
        def grscb(text: str):
            print(colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])),
                  colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])),
                  colored("██", random.choice(["red", "green", "blue"])), colored("██", random.choice(["red", "green", "blue"])), text)
        print(colored("██ ██ ██ ██ ██ ██", "green"), f" Who am I: {os.getlogin()}@{platform.node()}")
        print(colored("██", "blue"), f"                OS: {platform.system()} {platform.release()}")
        print(colored("██   ", "blue"), colored("██", "red"), colored("██", "green"), f"       Kernel: {platform.release()}")
        print(colored("      ██", "blue"), colored("      ██ ", "red"), f"Uptime: {os.popen('uptime -p').read()[:-1]}")
        savememon = ""
        for mon in screeninfo.get_monitors():
            if mon.is_primary: savememon = mon
        print(colored("               ██ ", "red"), f"Screen: {savememon.width}x{savememon.height}")
        print(colored("██ ██ ██ ██ ██ ██", "blue"), f" Architecture: {platform.architecture()[0]}")
        grscb(f" Processor: {platform.processor()}")
        total_memory, used_memory, free_memory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])
        grscb(f" RAM: {used_memory}/{total_memory} MB")
        grscb(f" Python: {platform.python_version()}")
        grscb(" Authors: Secton")
        grscb(" SCL Version: 2.7, 2023, 12 Oct.")
        grscb(" Thanks for your interest in SCL!")
        for color in termcolor.COLORS:
            print(colored("█", color), end="", flush=True)

    elif receiver[0] == "think":
        print("Always think twice.")
        webbrowser.open("https://youtu.be/Bxc4Fvs3Mmo")

    elif receiver[0] == "url":
        webbrowser.open(noCmdReceiver)

    elif receiver[0] == "help":
        print()

    else:
        print('Проверьте правильность написания.')

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
    print("Проверяем СКЛипт на проблемы с безопасностью...")
    dFileInsides = open(sys.argv[1], "r")
    for line in dFileInsides:
        if line.startswith("py "):
            print("Данный СКЛипт содержит выполнение Python команд.\n"
                  "Проблема в том, что через Python команды злоумышленник\n"
                  "Может сделать что-то плохое с вашей системой, например удалить файлы.\n\n"
                  "Если же вы доверяете этому СКЛипту, либо вы написали этот СКЛипт,\n"
                  "чтобы продолжить, введите 1. Иначе же 0. Если вы знаете Python,\n"
                  "Вы можете просмотреть py команды (2). Время выбирать.")
            choice = int(input("Выбор за вами: "))
            if choice <= 0:
                receiver[0] = "stop"
                commander()
            elif choice == 1:
                execscript()
            else:
                for lin2 in dFileInsides:
                    if line.startswith("py "):
                        print(line.removeprefix("py "))
                choice = int(input("Выбор за вами: "))
                if choice <= 0:
                    receiver[0] = "stop"
                    commander()
                elif choice == 1:
                    execscript()
            break
else:
    print("Добро пожаловать в SCL!")
    # droppedFile = ""

aftermath()