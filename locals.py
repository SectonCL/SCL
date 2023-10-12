default_lang: str = "en"

en_locale = ["SCL could not clear the terminal output.",  #0 Can't clear terminal
             "No description",  #1 Command has no description
             "No variable"  #2 Given variable does not exist
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
             ]

def_locale: list = globals()[default_lang + "_locale"]