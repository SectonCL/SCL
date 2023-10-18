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

             "This SCLipt contains Python commands.\n"
             "The issue is that the attacker can do something bad\n"
             "to your system, for example removing files.\n\n"
             "If you trust this SCLipt, or you wrote this,\n"
             "you can continue by entering 1, else 0. If you know Python,\n"
             "You can check py commands (2).\n"
             "We don't take any responsibility for any damage from third-party SCLipts.\n"
             "Time to choose.", #19 Securit issued,
             "Time to choose: ", # 20 Choosing time, G-Man reference.
             "SCL wasn't translated for this language.", # 21
             ["Who am I", # 0 user
              "OS", # 1 Operating System
              "Kernel", # 2
              "Uptime", # 3 How long system works
              "Screen", # 4
              "Architecture", # 5 CPU type
              "Processor", # 6 CPU
              "RAM:", # 7 Memory
              "Authors", # 8 SCL Authors
              "Version", # 9 SCL Version
              " Thanks for your interest in SCL!" # 10 Keep the space before the sentence!
              ] # 22 sectonfetch
             ]

ru_locale = ["SCL не смог очистить вывод.",  # 0 Can't clear terminal
             "Описание отсутствует",  # 1 Command has no description
             "Искомое имя не принадлежит ни одной переменной",  # 2 :) Написал так, как написано, если поисковой движок Яндекса в Государственном Каталоге Сайтов не найдёт ничего
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
              "Оперативная память:", # 7 Memory
              "Авторы", # 8 SCL Authors
              "Версия", # 9 SCL Version
              " Спасибо за ваш интерес в SCL!" # 10 Keep the space before the sentence!
              ] # 22 sectonfetch
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