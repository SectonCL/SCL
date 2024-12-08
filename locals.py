default_lang: str = "en"

en_locale = ["SCL could not clear the terminal output.",  #0 Can't clear terminal
             "No description",  #1 Command has no description
             "No variable",  #2 Given variable does not exist
             "SCL does not support your OS's commands.",  #3 Self-explanatory.

             # Keep the string width the same, add the spaces before the words. Here's the example:
             # GOOD:
             # " first:"
             # "second:"
             # "  nine:"
             # BAD:
             # "first:"
             # "second:"
             # "nine:"
             "FOLDER:", #4
             "  LINK:", #5
             "  FILE:", #6
             "   ABS:", #7
             " MOUNT:", #8
             "UNKNWN:", #9

             "This directory does not exist.", #10
             "Exiting...", #11 Closing an app.
             "Gotcha!", #12 This phrase appears when user tries to exit the app through the other way.
             "Auto-Clear mode enabled.", #13
             "Auto-Clear mode disabled.", #14
             "Check the variable's name!", #15 this isnt what you think it is
             "This command does not exist.", #16 Command got typed wrong.
             "Welcome to SCL!", #17 App startup
             "Checking SCLipt for security issues...", #18 File drag-n-dropped into SCL


             "We don't take any responsibility for any damage from third-party SCLipts.", #19 Security warning
             "Time to choose: ", # 20 Choosing time, G-Man reference.
             "SCL wasn't translated for this language.", # 21
             ["Who am I", # 21.0 user
              "OS", # 21.1 Operating System
              "Kernel", # 21.2
              "Uptime", # 21.3 How long system works
              "Screen", # 21.4
              "Architecture", # 21.5 CPU type
              "Processor", # 21.6 CPU
              "RAM", # 21.7 Memory
              "Authors", # 21.8 SCL Authors
              "Version", # 21.9 SCL Version
              "SCL will return as SRSh!" # 21.10
              ], # 22 sectonfetch
             "Check if you correctly written numbers.", # 23 Error when writing "{rand" argument parameters wrong
             "Looks like you don't have installed libraries in order for SCL to work. Would you like to install them?", # 24
             "Done!" # 25
             ]

ru_locale = ["SCL не смог очистить вывод.",  # 0 Can't clear terminal
             "Описание отсутствует",  # 1 Command has no description
             "Искомое имя не принадлежит ни одной переменной",  # 2
             "SCL частично не поддерживает вашу ОС.",  # 3 Self-explanatory.

             # Keep the string width the same, add the spaces before the words. Here's the example:
             # GOOD:
             # " first:"
             # "second:"
             # "  nine:"
             # BAD:
             # "first:"
             # "second:"
             # "nine:"
             " ПАПКА:",  # 4
             " ЯРЛЫК:",  # 5
             "  ФАЙЛ:",  # 6
             "   АБС:",  # 7
             "ПОДКЛ.:",  # 8
             "НЕИЗВ.:",  # 9

             "Такая папка не существует.",  # 10
             "Выключаюсь...",  # 11 Closing an app.
             "Попался, который кусался!",  # 12 This phrase appears when user tries to exit the app through the other way.
             "Auto-Clear включён.",  # 13
             "Auto-Clear выключен.",  # 14
             "Проверьте имя переменной!",  # 15 this isnt what you think it is
             "Эта команда не существует.",  # 16 Command got typed wrong.
             "Добро пожаловать в SCL!",  # 17 App startup
             "Проверяем СКЛипт на безопасность...",  # 18 File drag-n-dropped into SCL

             "Данный СКЛипт содержит выполнение Python команд.\n"
             "Проблема в том, что через Python команды злоумышленник\n"
             "Может сделать что-то плохое с вашей системой, например удалить файлы.\n\n"
             "Если же вы доверяете этому СКЛипту, либо вы написали этот СКЛипт,\n"
             "вы можете продолжить, введя 1, иначе же 0. Если вы знаете Python,\n"
             "Вы можете просмотреть py команды (2).\n"
             "Мы не берём на себя ответственность за любой ущёрб от стороннего СКЛипта."
             "Время выбирать.",  # 19 Securit issued,
             "Время выбирать: ", # 20 Choosing time, G-Man reference.
             "SCL не был переведён на этот язык.", # 21
             ["Кто я", # 0 user
              "ОС", # 1 Operating System
              "Кернель", # 2
              "Время работы", # 3 How long system works
              "Экран", # 4
              "Архитектура", # 5 CPU type
              "Процессор", # 6 CPU
              "Оперативная память", # 7 Memory
              "Авторы", # 8 SCL Authors
              "Версия", # 9 SCL Version
              "SCL вернётся как SRSh!" # 10 Keep the space before the sentence!
              ], # 22 sectonfetch
             "Проверь правильность введёных чисел.", # 23
             "Походу, у вас не все библиотеки установлены, на которых работает SCL. Хотите установить их?", # 24
             "Готово!" # 25
             ]

def_locale: list = globals()[default_lang + "_locale"] # This variable will load the localization strings from default lang

def lookup(string: str):
    if globals()[string + "_locale"] is not None:
        return True
    else:
        return False

def change(string: str):
    global default_lang
    global def_locale
    try:
        default_lang = string
        print("teswt")
        def_locale = globals()[string + "_locale"]
    except Exception:
        print("Error! No")