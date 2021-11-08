import tkinter as tk
from tkmacosx import Button

# Color variables for backgrounds
opBg = 'Tan'
numBg = '#3C3431'
modBg = 'Beige'
lblBg = '#FDF4E3'
# Color variables for foregrounds
opFg = 'white'
numFg = 'white'
modFg = 'black'
lblFg = 'black'

window = tk.Tk()
window.title('Calculator')
window['bg']=lblBg

opBg_var = tk.StringVar()
numBg_var = tk.StringVar()
modBg_var = tk.StringVar()
lblBg_var = tk.StringVar()

opFg_var = tk.StringVar()
numFg_var = tk.StringVar()
modFg_var = tk.StringVar()

operators = ['+', '-', '*', '/', '%']

def key_pressed(event):
    global side
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
    global opBg, numBg, modBg, lblBg, opFg, numFg, modFg, lblFg
    lblBg = lblBg_var.get()
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
    settings.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=40, weight=1)
    settings.columnconfigure([0, 1], minsize=100, weight=1)
 
    # Buttons to show in toplevel
    lbl_winBg = tk.Label(master=settings, text="Main Background Color", bg = lblBg, fg = lblFg)
    lbl_winBg.grid(row=0, column = 0, sticky = "nsw")

    lbl_numFg = tk.Label(master=settings, text="Number Font Color", bg = lblBg, fg = lblFg)
    lbl_numFg.grid(row=1, column = 0, sticky = "nsw")

    lbl_modBg = tk.Label(master=settings, text="Top Row Background Color", bg = lblBg, fg = lblFg)
    lbl_modBg.grid(row=2, column = 0, sticky = "nsw")

    lbl_modFg = tk.Label(master=settings, text="Top Row Font Color", bg = lblBg, fg = lblFg)
    lbl_modFg.grid(row=3, column = 0, sticky = "nsw")

    ent_winBg = tk.Entry(master=settings, bg = lblBg, fg = lblFg, highlightthickness = 0, textvariable = lblBg_var)
    ent_winBg.grid(row=0, column = 1, sticky = "nsw")

    ent_numFg = tk.Entry(master=settings, bg = lblBg, fg = lblFg, highlightthickness = 0, textvariable = numBg_var)
    ent_numFg.grid(row=1, column = 1, sticky = "nsw")

    ent_modBg = tk.Entry(master=settings, bg = lblBg, fg = lblFg, highlightthickness = 0, textvariable = modBg_var)
    ent_modBg.grid(row=2, column = 1, sticky = "nsw")

    ent_modFg = tk.Entry(master=settings, bg = lblBg, fg = lblFg, highlightthickness = 0, textvariable = modFg_var)
    ent_modFg.grid(row=3, column = 1, sticky = "nsw")

    btn_save = Button(master=settings, bg = lblBg, fg = lblFg, command = saveSettings, borderless = 1, text = "Save")
    btn_save.grid(row=4, column = 0, columnspan = 2)
 

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

btn_settings = Button(master=window, text="Settings", command=openSettings, bg = modBg, fg = modFg, borderless = 1)
btn_settings.grid(row=6, column = 0, columnspan = 4)

lbl_left = tk.Label(master=window, text="", bg=lblBg, fg=lblFg)
lbl_left.grid(row=0, column=0)

lbl_op = tk.Label(master=window, text="", bg=lblBg, fg=lblFg)
lbl_op.grid(row=0, column=1)

lbl_right = tk.Label(master=window, text="", bg=lblBg, fg=lblFg)
lbl_right.grid(row=0, column=2)

lbl_ans = tk.Label(master=window, text="", bg=lblBg, fg=lblFg)
lbl_ans.grid(row=0, column=3)

btn_subtract = Button(master=window, text="-", command=subtract, bg=opBg, fg=opFg, borderless=1)
btn_subtract.grid(row=4, column=3, sticky="nsew")

btn_add = Button(master=window, text="+", command=add, bg=opBg, fg=opFg, borderless=1)
btn_add.grid(row=5, column=3, sticky="nsew")

btn_multiply = Button(master=window, text="x", command=multiply, bg=opBg, fg=opFg, borderless=1)
btn_multiply.grid(row=3, column=3, sticky="nsew")

btn_divide = Button(master=window, text="/", command=divide, bg=opBg, fg=opFg, borderless=1)
btn_divide.grid(row=2, column=3, sticky="nsew")

btn_percent = Button(master=window, text="%", command=percent, bg=modBg, fg=modFg, borderless=1)
btn_percent.grid(row=1, column=2, sticky="nsew")

btn_sign = Button(master=window, text="+/-", command=sign, bg=modBg, fg=modFg, borderless=1)
btn_sign.grid(row=1, column=1, sticky="nsew")

btn_clear = Button(master=window, text="clear", command=clear, bg=modBg, fg=modFg, borderless=1)
btn_clear.grid(row=1, column=0, sticky="nsew")

btn_equal = Button(master=window, text="=", command=equal, bg=opBg, fg=opFg, borderless=1)
btn_equal.grid(row=1, column=3, sticky="nsew")

btn_one = Button(master=window, text="1", command=one, bg=numBg, fg=numFg, borderless=1)
btn_one.grid(row=2, column = 0, sticky="nsew")

btn_two = Button(master=window, text="2", command=two, bg=numBg, fg=numFg, borderless=1)
btn_two.grid(row=2, column = 1, sticky="nsew")

btn_three = Button(master=window, text="3", command=three, bg=numBg, fg=numFg, borderless=1)
btn_three.grid(row=2, column = 2, sticky="nsew")

btn_four = Button(master=window, text="4", command=four, bg=numBg, fg=numFg, borderless=1)
btn_four.grid(row=3, column = 0, sticky="nsew")

btn_five = Button(master=window, text="5", command=five, bg=numBg, fg=numFg, borderless=1)
btn_five.grid(row=3, column = 1, sticky="nsew")

btn_six = Button(master=window, text="6", command=six, bg=numBg, fg=numFg, borderless=1)
btn_six.grid(row=3, column = 2, sticky="nsew")

btn_seven = Button(master=window, text="7", command=seven, bg=numBg, fg=numFg, borderless=1)
btn_seven.grid(row=4, column = 0, sticky="nsew")

btn_eight = Button(master=window, text="8", command=eight, bg=numBg, fg=numFg, borderless=1)
btn_eight.grid(row=4, column = 1, sticky="nsew")

btn_nine = Button(master=window, text="9", command=nine, bg=numBg, fg=numFg, borderless=1)
btn_nine.grid(row=4, column = 2, sticky="nsew")

btn_zero = Button(master=window, text="0", command=zero, bg=numBg, fg=numFg, borderless=1)
btn_zero.grid(row=5, column = 0, columnspan = 2, sticky="nsew")

btn_decimal = Button(master=window, text=".", command=decimal, bg=numBg, fg=numFg, borderless=1)
btn_decimal.grid(row=5, column = 2, sticky="nsew")

window.bind("<Key>",key_pressed)
window.bind("<Return>",ret_equal)

window.mainloop()