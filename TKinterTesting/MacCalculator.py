import tkinter as tk
import yaml
from tkmacosx import Button

# Begin configuration file
config = yaml.safe_load(open("/Users/tomaskennedy/Documents/PythonProjects/TKinterTesting/config.yml"))

# Color class for backgrounds
class Background:
    op = config["opBg"]
    num = config["numBg"]
    mod = config["modBg"]
    lbl = config["lblBg"]
# Color variables for foregrounds
class Foreground:
    op = config["opFg"]
    num = config["numFg"]
    mod = config["modFg"]
    lbl = config["lblFg"]

window = tk.Tk()
window.title('Calculator')
window['bg']=Background.lbl

opBg_var = tk.StringVar()
numBg_var = tk.StringVar()
modBg_var = tk.StringVar()
lblBg_var = tk.StringVar()

opFg_var = tk.StringVar()
numFg_var = tk.StringVar()
modFg_var = tk.StringVar()
lblFg_var = tk.StringVar()

operators = ['+', '-', '*', '/', '%']

def reset_settings(setting):
    if setting is "opBg":
        config["opBg"] = config["opDefaultBg"]
    elif setting is "numBg":
        config["numBg"] = config["numDefaultBg"]
    elif setting is "modBg":
        config["modBg"] = config["modDefaultBg"]
    elif setting is "lblBg":
        config["lblBg"] = config["lblDefaultBg"]
    elif setting is "opFg":
        config["opFg"] = config["opDefaultFg"]
    elif setting is "numFg":
        config["numFg"] = config["numDefaultFg"]
    elif setting is "modFg":
        config["modFg"] = config["modDefaultFg"]
    elif setting is "lblFg":
        config["lblFg"] = config["lblDefaultFg"]
def update_settings():
    window['bg'] = Background.lbl
    lbl_left['bg'] = Background.lbl
    lbl_right['bg'] = Background.lbl
    lbl_op['bg'] = Background.lbl
    lbl_ans['bg'] = Background.lbl
    btn_add['bg'] = Background.op
    btn_clear['bg'] = Background.mod
    btn_decimal['bg'] = Background.num
    btn_divide['bg'] = Background.op
    btn_eight['bg'] = Background.num
    btn_equal['bg'] = Background.op
    btn_five['bg'] = Background.num
    btn_four['bg'] = Background.num
    btn_multiply['bg'] = Background.op
    btn_nine['bg'] = Background.num
    btn_one['bg'] = Background.num
    btn_percent['bg'] = Background.mod
    btn_settings['bg'] = Background.op
    btn_seven['bg'] = Background.num
    btn_sign['bg'] = Background.mod
    btn_six['bg'] = Background.num
    btn_subtract['bg'] = Background.op
    btn_three['bg'] = Background.num
    btn_two['bg'] = Background.num
    btn_zero['bg'] = Background.num
    # Updates for foreground colors (font)
    lbl_left['fg'] = Foreground.lbl
    lbl_right['fg'] = Foreground.lbl
    lbl_op['fg'] = Foreground.lbl
    lbl_ans['fg'] = Foreground.lbl
    btn_add['fg'] = Foreground.op
    btn_clear['fg'] = Foreground.mod
    btn_decimal['fg'] = Foreground.num
    btn_divide['fg'] = Foreground.op
    btn_eight['fg'] = Foreground.num
    btn_equal['fg'] = Foreground.op
    btn_five['fg'] = Foreground.num
    btn_four['fg'] = Foreground.num
    btn_multiply['fg'] = Foreground.op
    btn_nine['fg'] = Foreground.num
    btn_one['fg'] = Foreground.num
    btn_percent['fg'] = Foreground.mod
    btn_settings['fg'] = Foreground.op
    btn_seven['fg'] = Foreground.num
    btn_sign['fg'] = Foreground.mod
    btn_six['fg'] = Foreground.num
    btn_subtract['fg'] = Foreground.op
    btn_three['fg'] = Foreground.num
    btn_two['fg'] = Foreground.num
    btn_zero['fg'] = Foreground.num

def key_pressed(event):
    side = sideCheck()
    if side and event.char.isdigit():
        lbl_left["text"] += event.char
    elif not side and event.char.isdigit():
        lbl_right["text"] += event.char
    elif event.char in operators and lbl_ans["text"] == "":
        lbl_op["text"] = event.char
        side = False
    elif event.char in operators:
        tempCopy = lbl_ans["text"]
        clear()
        lbl_left["text"] = tempCopy
        lbl_op["text"] = event.char
        side = False
    elif event.char == "=":
        equal()
    elif event.char == "c":
        clear()
def ret_equal(event):
    equal()
def saveSettings():
    if lblBg_var.get() != "":
        Background.lbl = lblBg_var.get()
    if opBg_var.get() != "":
        Background.op = opBg_var.get()
    if numBg_var.get() != "":
        Background.num = numBg_var.get()
    if modBg_var.get() != "":
        Background.mod = modBg_var.get()
    if modFg_var.get() != "":
        Foreground.mod = modFg_var.get()
    if numFg_var.get() != "":
        Foreground.num = numFg_var.get()
    if opFg_var.get() != "":
        Foreground.op = opFg_var.get()
    if lblFg_var.get() != "":
        Foreground.lbl = lblFg_var.get()
    update_settings()

def openSettings():
    # Toplevel object which will
    # be treated as a new window
    settings = tk.Toplevel()
 
    # sets the title of the
    # Toplevel widget
    settings.title("Settings")

    # sets the background color of the toplevel widget
    settings['bg'] = window['bg']
 
    # sets the geometry of toplevel
    settings.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], minsize=40, weight=1)
    settings.columnconfigure([0, 1], minsize=100, weight=1)
 
    # Buttons to show in toplevel
    lbl_winBg = tk.Label(master=settings, text="Main Background Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_winBg.grid(row=0, column = 0, sticky = "nsw")

    lbl_modBg = tk.Label(master=settings, text="Top Row Background Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_modBg.grid(row=1, column = 0, sticky = "nsw")

    lbl_modFg = tk.Label(master=settings, text="Top Row Font Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_modFg.grid(row=2, column = 0, sticky = "nsw")

    lbl_opBg = tk.Label(master=settings, text="Operator Background Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_opBg.grid(row=3, column = 0, sticky = "nsw")

    lbl_opFg = tk.Label(master=settings, text="Operator Font Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_opFg.grid(row=4, column = 0, sticky = "nsw")

    lbl_numBg = tk.Label(master=settings, text="Number Background Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_numBg.grid(row=5, column = 0, sticky = "nsw")

    lbl_numFg = tk.Label(master=settings, text="Number Font Color", bg = Background.lbl, fg = Foreground.lbl)
    lbl_numFg.grid(row=6, column = 0, sticky = "nsw")

    ent_winBg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = lblBg_var)
    ent_winBg.grid(row=0, column = 1, sticky = "nsw")

    ent_modBg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = modBg_var)
    ent_modBg.grid(row=1, column = 1, sticky = "nsw")

    ent_modFg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = modFg_var)
    ent_modFg.grid(row=2, column = 1, sticky = "nsw")

    ent_opBg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = opBg_var)
    ent_opBg.grid(row=3, column = 1, sticky = "nsw")

    ent_opFg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = opFg_var)
    ent_opFg.grid(row=4, column = 1, sticky = "nsw")

    ent_numBg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = numBg_var)
    ent_numBg.grid(row=5, column = 1, sticky = "nsw")

    ent_numFg = tk.Entry(master=settings, bg = Background.lbl, fg = Foreground.lbl, highlightthickness = 0, textvariable = numFg_var)
    ent_numFg.grid(row=6, column = 1, sticky = "nsw")

    btn_resetWinBg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetWinBg.grid(row=0, column = 2, columnspan = 1)

    btn_resetModBg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetModBg.grid(row=1, column = 2, columnspan = 1)

    btn_resetModFg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetModFg.grid(row=2, column = 2, columnspan = 1)

    btn_resetOpBg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetOpBg.grid(row=3, column = 2, columnspan = 1)

    btn_resetOpFg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetOpFg.grid(row=4, column = 2, columnspan = 1)

    btn_resetNumBg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetNumBg.grid(row=5, column = 2, columnspan = 1)

    btn_resetNumFg = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "reset")
    btn_resetNumFg.grid(row=6, column = 2, columnspan = 1)

    btn_save = Button(master=settings, bg = Background.lbl, fg = Foreground.lbl, command = saveSettings , borderless = 1, text = "Save")
    btn_save.grid(row=7, column = 0, columnspan = 2)
    
 

# Formats float to remove trailing zeros 
def floatToString(inputValue):
    return ('%.3f' % inputValue).rstrip("0").rstrip(".")
    
def sideCheck():
    side = True
    if (lbl_op["text"] != ""):
        side = False
    return side

def add():
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "+"

def subtract():
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "-"

def multiply():
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "x"

def divide():
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "/"

def percent():
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "%"

def one():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "1"
    else:
        lbl_right["text"] += "1"

def two():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "2"
    else:
        lbl_right["text"] += "2"

def three():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "3"
    else:
        lbl_right["text"] += "3"

def four():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "4"
    else:
        lbl_right["text"] += "4"

def five():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "5"
    else:
        lbl_right["text"] += "5"

def six():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "6"
    else:
        lbl_right["text"] += "6"

def seven():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "7"
    else:
        lbl_right["text"] += "7"

def eight():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "8"
    else:
        lbl_right["text"] += "8"

def nine():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "9"
    else:
        lbl_right["text"] += "9"

def zero():
    side = sideCheck()
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "0"
    else:
        lbl_right["text"] += "0"

def decimal():
    side = sideCheck()
    if side and "." not in lbl_left["text"]:
        lbl_left["text"] += "."
    elif not side and "." not in lbl_right["text"]:
        lbl_right["text"] += "."

def clear():
    lbl_left["text"] = ""
    lbl_right["text"] = ""
    lbl_op["text"] = ""
    lbl_ans["text"] = ""

def equal():
    if lbl_ans["text"] != "":
        lbl_left["text"] = lbl_ans["text"]
        lbl_ans["text"] = ""
    if lbl_op["text"] == "+":
        lbl_ans["text"] = floatToString(float(lbl_left["text"]) + float(lbl_right["text"]))
    elif lbl_op["text"] == "-":
        lbl_ans["text"] = floatToString(float(lbl_left["text"]) - float(lbl_right["text"]))
    elif lbl_op["text"] == "x":
        lbl_ans["text"] = floatToString(float(lbl_left["text"]) * float(lbl_right["text"]))
    elif lbl_op["text"] == "/":
        lbl_ans["text"] = floatToString(float(lbl_left["text"]) / float(lbl_right["text"]))
    elif lbl_op["text"] == "%":
        lbl_ans["text"] = floatToString(float(lbl_left["text"]) * (float(lbl_right["text"]) / 100))

def sign():
    side = sideCheck()
    if side:
        if "-" not in lbl_left["text"]:
            lbl_left["text"] = "-" + lbl_left["text"]
        else:
            lbl_left["text"] = lbl_left["text"][1:]
    else:
        if "-" not in lbl_right["text"]:
            lbl_right["text"] = "-" + lbl_right["text"]
        else:
            lbl_right["text"] = lbl_right["text"][1:]


window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

btn_settings = Button(master=window, text="Settings", command=openSettings, bg = Background.mod, fg = Foreground.mod, borderless = 1)
btn_settings.grid(row=6, column = 0, columnspan = 4)

lbl_left = tk.Label(master=window, text="", bg=Background.lbl, fg=Foreground.lbl)
lbl_left.grid(row=0, column=0)

lbl_op = tk.Label(master=window, text="", bg=Background.lbl, fg=Foreground.lbl)
lbl_op.grid(row=0, column=1)

lbl_right = tk.Label(master=window, text="", bg=Background.lbl, fg=Foreground.lbl)
lbl_right.grid(row=0, column=2)

lbl_ans = tk.Label(master=window, text="", bg=Background.lbl, fg=Foreground.lbl)
lbl_ans.grid(row=0, column=3)

btn_subtract = Button(master=window, text="-", command=subtract, bg=Background.op, fg=Foreground.op, borderless=1)
btn_subtract.grid(row=4, column=3, sticky="nsew")

btn_add = Button(master=window, text="+", command=add, bg=Background.op, fg=Foreground.op, borderless=1)
btn_add.grid(row=5, column=3, sticky="nsew")

btn_multiply = Button(master=window, text="x", command=multiply, bg=Background.op, fg=Foreground.op, borderless=1)
btn_multiply.grid(row=3, column=3, sticky="nsew")

btn_divide = Button(master=window, text="/", command=divide, bg=Background.op, fg=Foreground.op, borderless=1)
btn_divide.grid(row=2, column=3, sticky="nsew")

btn_percent = Button(master=window, text="%", command=percent, bg=Background.mod, fg=Foreground.mod, borderless=1)
btn_percent.grid(row=1, column=2, sticky="nsew")

btn_sign = Button(master=window, text="+/-", command=sign, bg=Background.mod, fg=Foreground.mod, borderless=1)
btn_sign.grid(row=1, column=1, sticky="nsew")

btn_clear = Button(master=window, text="clear", command=clear, bg=Background.mod, fg=Foreground.mod, borderless=1)
btn_clear.grid(row=1, column=0, sticky="nsew")

btn_equal = Button(master=window, text="=", command=equal, bg=Background.op, fg=Foreground.op, borderless=1)
btn_equal.grid(row=1, column=3, sticky="nsew")

btn_one = Button(master=window, text="1", command=one, bg=Background.num, fg=Foreground.num, borderless=1)
btn_one.grid(row=2, column = 0, sticky="nsew")

btn_two = Button(master=window, text="2", command=two, bg=Background.num, fg=Foreground.num, borderless=1)
btn_two.grid(row=2, column = 1, sticky="nsew")

btn_three = Button(master=window, text="3", command=three, bg=Background.num, fg=Foreground.num, borderless=1)
btn_three.grid(row=2, column = 2, sticky="nsew")

btn_four = Button(master=window, text="4", command=four, bg=Background.num, fg=Foreground.num, borderless=1)
btn_four.grid(row=3, column = 0, sticky="nsew")

btn_five = Button(master=window, text="5", command=five, bg=Background.num, fg=Foreground.num, borderless=1)
btn_five.grid(row=3, column = 1, sticky="nsew")

btn_six = Button(master=window, text="6", command=six, bg=Background.num, fg=Foreground.num, borderless=1)
btn_six.grid(row=3, column = 2, sticky="nsew")

btn_seven = Button(master=window, text="7", command=seven, bg=Background.num, fg=Foreground.num, borderless=1)
btn_seven.grid(row=4, column = 0, sticky="nsew")

btn_eight = Button(master=window, text="8", command=eight, bg=Background.num, fg=Foreground.num, borderless=1)
btn_eight.grid(row=4, column = 1, sticky="nsew")

btn_nine = Button(master=window, text="9", command=nine, bg=Background.num, fg=Foreground.num, borderless=1)
btn_nine.grid(row=4, column = 2, sticky="nsew")

btn_zero = Button(master=window, text="0", command=zero, bg=Background.num, fg=Foreground.num, borderless=1)
btn_zero.grid(row=5, column = 0, columnspan = 2, sticky="nsew")

btn_decimal = Button(master=window, text=".", command=decimal, bg=Background.num, fg=Foreground.num, borderless=1)
btn_decimal.grid(row=5, column = 2, sticky="nsew")

window.bind("<Key>",key_pressed)
window.bind("<Return>",ret_equal)

window.mainloop()