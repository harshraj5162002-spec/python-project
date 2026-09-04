import tkinter as tk
import math


# ---------------- Calculator Functions ----------------

def press(value):
    current = display.get()

    if current == "Error":
        display.delete(0, tk.END)

    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    try:
        expression = display.get()

        # Mathematical symbols
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")

        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial
        })

        display.delete(0, tk.END)
        display.insert(0, str(result))

        history.insert(tk.END, f"{expression} = {result}")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square():
    try:
        number = float(display.get())
        result = number ** 2

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square_root():
    try:
        number = float(display.get())
        result = math.sqrt(number)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def factorial():
    try:
        number = int(display.get())
        result = math.factorial(number)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ---------------- Main Window ----------------

root = tk.Tk()
root.title("Advanced Python Calculator")
root.geometry("430x650")
root.resizable(False, False)

# ---------------- Display ----------------

display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(
    padx=10,
    pady=15,
    fill="x"
)

# ---------------- Buttons ----------------

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["√", "x²", "^", "="],
    ["sin", "cos", "tan", "log"],
    ["ln", "π", "e", "n!"]
]


def button_click(value):

    if value == "C":
        clear()

    elif value == "⌫":
        delete()

    elif value == "=":
        calculate()

    elif value == "√":
        square_root()

    elif value == "x²":
        square()

    elif value == "n!":
        factorial()

    elif value == "π":
        press("pi")

    elif value == "e":
        press("e")

    elif value in ["sin", "cos", "tan", "log", "ln"]:
        press(value + "(")

    else:
        press(value)


for row in buttons:
    for value in row:

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 16, "bold"),
            width=6,
            height=2,
            command=lambda v=value: button_click(v)
        )

        button.grid(
            row=buttons.index(row),
            column=row.index(value),
            padx=3,
            pady=3
        )


# ---------------- History ----------------

tk.Label(
    root,
    text="Calculation History",
    font=("Arial", 14, "bold")
).pack(pady=5)

history = tk.Listbox(
    root,
    width=50,
    height=6,
    font=("Arial", 11)
)

history.pack(
    padx=10,
    pady=5
)


# ---------------- Keyboard Support ----------------

root.bind("<Return>", lambda event: calculate())
root.bind("<Escape>", lambda event: clear())

root.mainloop()