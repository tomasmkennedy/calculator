import tkinter as tk

window = tk.Tk()
side = True # left is true, right is false

# Formats float to remove trailing zeros 
def floatToString(inputValue):
    return ('%.3f' % inputValue).rstrip("0").rstrip(".")
    
def add():
    global side
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "+"
    side = False
        

def subtract():
    global side
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "-"
    side = False

def multiply():
    global side
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "x"
    side = False

def divide():
    global side
    if lbl_ans["text"] != "":
        temp = lbl_ans["text"]
        clear()
        lbl_left["text"] = temp
    lbl_op["text"] = "/"
    side = False

def one():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "1"
    else:
        lbl_right["text"] += "1"

def two():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "2"
    else:
        lbl_right["text"] += "2"

def three():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "3"
    else:
        lbl_right["text"] += "3"

def four():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "4"
    else:
        lbl_right["text"] += "4"

def five():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "5"
    else:
        lbl_right["text"] += "5"

def six():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "6"
    else:
        lbl_right["text"] += "6"

def seven():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "7"
    else:
        lbl_right["text"] += "7"

def eight():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "8"
    else:
        lbl_right["text"] += "8"

def nine():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "9"
    else:
        lbl_right["text"] += "9"

def zero():
    global side
    if lbl_ans["text"] != "":
        clear()
    if side:
        lbl_left["text"] += "0"
    else:
        lbl_right["text"] += "0"

def decimal():
    global side
    if side and "." not in lbl_left["text"]:
        lbl_left["text"] += "."
    elif not side and "." not in lbl_right["text"]:
        lbl_right["text"] += "."

def clear():
    global side
    lbl_left["text"] = ""
    lbl_right["text"] = ""
    lbl_op["text"] = ""
    lbl_ans["text"] = ""
    side = True

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

def sign():
    global side
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


window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

lbl_left = tk.Label(master=window, text="")
lbl_left.grid(row=0, column=0)

lbl_op = tk.Label(master=window, text="")
lbl_op.grid(row=0, column=1)

lbl_right = tk.Label(master=window, text="")
lbl_right.grid(row=0, column=2)

lbl_ans = tk.Label(master=window, text="")
lbl_ans.grid(row=0, column=3)

btn_subtract = tk.Button(master=window, text="-", command=subtract)
btn_subtract.grid(row=4, column=3, sticky="nsew")

btn_add = tk.Button(master=window, text="+", command=add)
btn_add.grid(row=5, column=3, sticky="nsew")

btn_multiply = tk.Button(master=window, text="x", command=multiply)
btn_multiply.grid(row=3, column=3, sticky="nsew")

btn_divide = tk.Button(master=window, text="/", command=divide)
btn_divide.grid(row=2, column=3, sticky="nsew")

btn_sign = tk.Button(master=window, text="+/-", command=sign)
btn_sign.grid(row=1, column=1, sticky="nsew")

btn_clear = tk.Button(master=window, text="clear", command=clear)
btn_clear.grid(row=1, column=2, sticky="nsew")

btn_equal = tk.Button(master=window, text="=", command=equal)
btn_equal.grid(row=1, column=3, sticky="nsew")

btn_one = tk.Button(master=window, text="1", command=one)
btn_one.grid(row=2, column = 0, sticky="nsew")

btn_two = tk.Button(master=window, text="2", command=two)
btn_two.grid(row=2, column = 1, sticky="nsew")

btn_three = tk.Button(master=window, text="3", command=three)
btn_three.grid(row=2, column = 2, sticky="nsew")

btn_four = tk.Button(master=window, text="4", command=four)
btn_four.grid(row=3, column = 0, sticky="nsew")

btn_five = tk.Button(master=window, text="5", command=five)
btn_five.grid(row=3, column = 1, sticky="nsew")

btn_six = tk.Button(master=window, text="6", command=six)
btn_six.grid(row=3, column = 2, sticky="nsew")

btn_seven = tk.Button(master=window, text="7", command=seven)
btn_seven.grid(row=4, column = 0, sticky="nsew")

btn_eight = tk.Button(master=window, text="8", command=eight)
btn_eight.grid(row=4, column = 1, sticky="nsew")

btn_nine = tk.Button(master=window, text="9", command=nine)
btn_nine.grid(row=4, column = 2, sticky="nsew")

btn_zero = tk.Button(master=window, text="0", command=zero)
btn_zero.grid(row=5, column = 1, sticky="nsew")

btn_decimal = tk.Button(master=window, text=".", command=decimal)
btn_decimal.grid(row=5, column = 2, sticky="nsew")

window.mainloop()