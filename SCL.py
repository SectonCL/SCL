import locals
import info
locpal = locals.def_locale

import os
import sys
from platform import uname, uname_result
if sys.argv.__len__() == 1: print("Loading...")
import random
import easygui_qt


try:
	import termcolor
	from termcolor import colored
	import webbrowser
	import subprocess
except ModuleNotFoundError:
	print(locpal[24])
	answer = str(input("[Y/N]: "))
	if answer.lower().startswith("y"):
		os.system("pip3 install termcolor webbrowser subprocess easygui_qt")
		print(locpal[25])
	else: quit(2)



dFileInsides = ""
cantClear = False
autoClear = False
scriptmode = False
plilibs = []
cmds = {}
receiver = ["f"]       # Received output including everything
noCmdReceiver = "yes"  # Received output without the first word, NOT a list.
curPath = "C:/" if os.name == 'nt' else "/"
usrvars = { "test": "Nothin' to see here." }



try:
	if sys.argv.__len__() == 1: os.system('cls' if os.name == 'nt' else 'clear')
except Exception:
	print(locpal[0])
	cantClear = True



def regcommand(name: str, desc: str = locpal[1]): global cmds; cmds[name] = desc

def modifyargs():
	global receiver
	global noCmdReceiver
	receiver = receiver.split(" ")  # Splitting to get every args

	# ARGUMENTS
	for index, arg in enumerate(receiver):
		if arg.__contains__("{var:"):
			modified_arg = arg.replace("{var:", "")
			try: receiver[index] = usrvars[modified_arg] # This works now
			except KeyError as bigE: print(f"{locpal[2]} {bigE}!")
		elif arg.__contains__("{rand:"):
			modified_arg = arg.replace("{rand:", "")
			modified_arg = modified_arg.split(",", 1)
			try: receiver[index] = str(random.randrange(random.randrange(int(modified_arg[0]), int(modified_arg[1]))))
			except Exception:
				receiver.pop(index)
				print(locpal[23])
		elif arg.__contains__("{truefalse:"):
			modified_arg = arg.replace("{truefalse:", "")
			modified_arg = modified_arg.split(",", 1)
			receiver[index] = str(easygui_qt.get_yes_or_no(modified_arg[0], modified_arg[1]))

	noCmdReceiver = " ".join(receiver[1:]).replace(">[",   curPath)


def aftermath():
	global receiver
	global noCmdReceiver
	global usrvars
	receiver = str(input(colored("S", "blue") + colored("C", "green") + colored("L", "red") + ": "))
	modifyargs()
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
		try: os.system('cls' if os.name == 'nt' else 'clear')
		except Exception:
			print(locpal[3])
			autoClear = False

	match receiver[0]:
		case "type": print(noCmdReceiver)

		case "spath":
			print(os.path.dirname(curPath) + ":")
			for elem in os.listdir(curPath):
				if os.path.isdir(curPath + elem):    print(f"{locpal[4]} {elem}")
				elif os.path.islink(curPath + elem): print(f"{locpal[5]} {elem}")
				elif os.path.isfile(curPath + elem): print(f"{locpal[6]} {elem}")
				elif os.path.isabs(curPath + elem):  print(f"{locpal[7]} {elem}")
				elif os.path.ismount(curPath + elem):print(f"{locpal[8]} {elem}")
				else:                                print(f"{locpal[9]} {elem}")
		case "cpath":
			if os.path.isdir(noCmdReceiver): curPath = noCmdReceiver
			else:                            print(locpal[10])

		case "logic":
			print("This was never finished."); pass # The unfinished code itself is a comment below
			# if receiver[1] == "True": print("beta")

		case "infodialog":
			if receiver.__len__() == 1: print("You must write at least a message!")
			else: easygui_qt.show_message(receiver[1], receiver[2] if receiver.__len__() >= 3 else "Information")

		case "stop" | "exit" | "quit": print(locpal[11]); sys.exit(0)


		case "clr":
			if not cantClear and noCmdReceiver == "":
				try: os.system('cls' if os.name == 'nt' else 'clear')
				except Exception: print(locpal[3])
			elif not cantClear and noCmdReceiver == "1":
				print(locpal[13])
				autoClear = True
			elif not cantClear and noCmdReceiver == "0":
				print(locpal[14])
				autoClear = False

		case "var":
			try:
				if receiver[1] == "set": usrvars[receiver[2]] = " ".join(receiver[3:])
				try:
					if receiver[1] == "remove": usrvars.pop(receiver[2])
					elif receiver[1] == "read": print(usrvars[receiver[2]])
					elif receiver[1] == "input": usrvars[receiver[2]] = input(str(receiver[2]) + ": ")
				except Exception: print(locpal[15])
			except IndexError: print("Set the settings!")

		case "sectonfetch":
			try: import screeninfo
			except Exception: os.system("pip3 install screeninfo"); import screeninfo
			import platform
			def grscb(text: str = "", asText: bool = False):
				easteregg = random.randint(0, 10)
				if easteregg != 0 or len(receiver) > 2:
					result = colored("▓▓", random.choice(["red", "green", "blue"])) + colored("▓▓", random.choice(["red", "green", "blue"])) + colored("▒▒", random.choice(["red", "green", "blue"])) + colored("▒▒", random.choice(["red", "green", "blue"])) + colored("░░", random.choice(["red", "green", "blue"])) + colored("░░", random.choice(["red", "green", "blue"])) + text
				elif len(receiver) != 2: result = colored("▄▀▄▀▄▀▄▀▄▀▄▀", "black", "on_magenta") + text
				if not asText: print(result) # ^ It had to be done...
				else: return result
			print(colored("████████████", "green"), f"| {os.getlogin()}@{platform.node()} {grscb(asText=True)}")
			print(colored("██", "blue"), f"          | {locpal[22][1]}: {platform.system()} {platform.release()}")
			print(colored("██ ", "blue"), colored("██", "red") + colored("██", "green"), f"    | {locpal[22][3]}: {os.popen('uptime -p').read()[:-1]}")
			savememon = ""
			for mon in screeninfo.get_monitors():
				if mon.is_primary: savememon = mon
			print(colored("    ██", "blue"), colored("   ██", "red"), f"| {locpal[22][4]}: {savememon.width}x{savememon.height}")
			print(colored("          ██", "red"), f"| {locpal[22][5]}: {platform.architecture()[0]}")
			print(colored("████████████", "blue"), f"| {locpal[22][6]}: {platform.processor()}")
			total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
			grscb(f" | {locpal[22][7]}: {used_memory}/{total_memory} MB")
			grscb(f" | Python: {platform.python_version()}")
			grscb(f" | SCL {locpal[22][9]} {info.version}: {info.changeDate}")
			print(f"{locpal[22][10]}")

		case "think": # Easter egg
			print("Always think twice.")
			webbrowser.open("https://youtu.be/Bxc4Fvs3Mmo")

		case "url": webbrowser.open(noCmdReceiver)

		case "lang":
			try:
				if locals.lookup(receiver[1]) is True:
					locals.change(receiver[1])
					locpal = locals.def_locale
					try: os.system('cls' if os.name == 'nt' else 'clear')
					except Exception:
						print(locpal[0])
						cantClear = True
					print(locpal[17])
			except Exception: print(locpal[21])


		case "help":
			print(f"""
SCL {info.version} GUIDE ({info.edition} Edition):
type       | prints what you written.
spath      | shows the contents of current path you're in.
cpath      | changes the current path. Very sensitive to syntax!
logic      | meant to run user-specific function if statement
           | was true, but never got finished
infodialog | shows a windows containing a user's message and then title.
stop       | exits the program. Can also be executed through `exit` or `quit`
clr        | clears the terminal. 1 and 0 toggles the auto-clear.
var        | user variable manager. commands: set, remove, read, input
sectonfetch| was created before neofetch's deprecation.
url        | opens url in user's default web-browser.
lang       | changes language. Lasts for one session.
""")

		case "": print("Nothing was even written.")
		case _: print(locpal[16])

	if not scriptmode and sys.argv.__len__() == 1: aftermath()


if sys.argv.__len__() > 1 and not os.path.isfile(sys.argv[1]):
	receiver = sys.argv[1:]
	noCmdReceiver = " ".join(receiver[1:]).replace(">[",   curPath)
	commander()
	quit(2)

def execscript():
	global receiver
	global noCmdReceiver
	for lining in dFileInsides:
		receiver = lining
		modifyargs()
		commander()

if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
	print("SCL: SCRIPT MODE.")
	print(locpal[19])
	print("-" * os.get_terminal_size().columns)
	scriptmode = True
	dFileInsides = open(sys.argv[1], "r")
	execscript()
else:
	print(locpal[17])
	# droppedFile = ""

aftermath()