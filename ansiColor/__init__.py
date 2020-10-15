import os
from sys import platform

if platform == "win32":
    os.system("color")

class colors:
    reset = u"\u001b[0m"
    class foreground:
        red = u"\u001b[31m"
        black = u"\u001b[30m"
        green = u"\u001b[32m"
        yellow = u"\u001b[33m"
        blue = u"\u001b[34m"
        magenta = u"\u001b[35m"
        cyan = u"\u001b[36m"
        white = u"\u001b[37m"
        brightBlack = u"\u001b[30;1m"
        brightRed = u"\u001b[31;1m"
        brightGreen = u"\u001b[32;1m"
        brightYellow = u"\u001b[33;1m"
        brightBlue = u"\u001b[34;1m"
        brightMagenta = u"\u001b[35;1m"
        brightCyan = u"\u001b[36;1m"
        brightWhite = u"\u001b[37;1m"
    class background:
        black = u"\u001b[40m"
        red = u"\u001b[41m"
        green = u"\u001b[42m"
        yellow = u"\u001b[43m"
        blue = u"\u001b[44m"
        magenta = u"\u001b[45m"
        cyan = u"\u001b[46m"
        white = u"\u001b[47m"
        brightBlack = u"\u001b[40;1m"
        brightRed = u"\u001b[41;1m"
        brightGreen = u"\u001b[42;1m"
        brightYellow = u"\u001b[43;1m"
        brightBlue = u"\u001b[44;1m"
        brightMagenta = u"\u001b[45;1m"
        brightCyan = u"\u001b[46;1m"
        brightWhite = u"\u001b[47;1m"
    class decorations:
        bold = u"\u001b[1m"
        underline = u"\u001b[4m"
        reverse = u"\u001b[7m"

    class cursor:
        up = u"\u001b[1A"
        down = u"\u001b[1B"
        right = u"\u001b[1C"
        left = u"\u001b[1D"

class Error(Exception):
    """Base class for other exceptions"""
    
    def __init__(self, foregroundColor,t):
        self.color = foregroundColor
        self.message = f"not an ANSI code color: {t}"
        super().__init__(self.message)

class NotAColor(Error):
    """Raised when the input is not a color"""
    pass

def color(text,foregroundColor,backgroundColor = None):
    if foregroundColor.startswith(u"\u001b") == False:
        raise NotAColor(foregroundColor,"foreground")
    
    if backgroundColor != None:
        if backgroundColor.startswith(u"\u001b") == False:
            raise NotAColor(backgroundColor,"background")
    
    if backgroundColor == None:
        data = f"{foregroundColor}{text}{colors.reset}"
    else:
        data = f"{foregroundColor}{backgroundColor}{text}{colors.reset}"

    return data

def colorNoReset(text,foregroundColor,backgroundColor = None):
    if foregroundColor.startswith(u"\\u001") == False:
        raise NotAColor(foregroundColor)
    
    if backgroundColor.startswith(u"\\u001") == False:
        if backgroundColor != None:
            raise NotAColor(backgroundColor)
    
    if backgroundColor == None:
        data = f"{foregroundColor}{text}"
    else:
        data = f"{foregroundColor}{backgroundColor}{text}"

    return data

def reset():
    return "".join(colors.reset)

