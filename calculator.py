import tkinter as tk
import math

num1 = ''
num2 = ''
operator = ''
firstTime = True

def Addition(num1, num2):
    try:
        return str(float(num1) + float(num2))
    except ValueError:
        return "Error"

def Subtraction(num1, num2):
    try:
        return str(float(num1) - float(num2))
    except ValueError:
        return "Error"

def Multiplication(num1, num2):
    try:
        return str(float(num1) * float(num2))
    except ValueError:
        return "Error"

def Division(num1, num2):
    try:
        if float(num2) == 0:
            return "Error: Div by 0"
        return str(float(num1) / float(num2))
    except ValueError:
        return "Error"

def SquareRoot(num):
    try:
        val = float(num)
        if val < 0:
            return "Error: Neg Sqrt"
        return str(math.sqrt(val))
    except ValueError:
        return "Error"

def Logarithm(num):
    try:
        val = float(num)
        if val <= 0:
            return "Error: Log <= 0"
        return str(math.log10(val))
    except ValueError:
        return "Error"

def OpChecker(operator, num1, num2):
    if operator == '+':
        return Addition(num1,num2)
    if operator == '-':
        return Subtraction(num1,num2)
    if operator == '/':
        return Division(num1, num2)
    if operator == '*':
        return Multiplication(num1, num2)
    
    return ''

def On_Exitbutton_Click():
    window.destroy()

def On_Number_Click(number):
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += str(number)
    else:
        num2 += str(number)
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Decimal_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        if '.' not in num1:
            num1 += '.'
    else:
        if '.' not in num2:
            num2 += '.'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)


def On_Operator_Click(op):
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        if num1: # Only set operator if num1 is not empty
            firstTime = False
            operator = op
    else:
        if num1 and num2: # Perform calculation if both numbers exist
            num1 = OpChecker(operator, num1, num2)
            operator = op
            num2 = ''
        else: # If only num1 exists, just change the operator
            operator = op
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Equal_Click():
    global num1
    global num2
    global firstTime
    global operator
    if not firstTime and num1 and num2 and operator:
        num1 = OpChecker(operator, num1, num2)
        operator = ''
        num2 = ''
        firstTime = True # Reset for new calculation
    Numbers.config(text=num1)

def On_Clear_Click():
    global num1
    global num2
    global operator
    global firstTime
    num1 = ''
    num2 = ''
    operator = ''
    firstTime = True
    Numbers.config(text='')

def On_Sqrt_Click():
    global num1
    global num2
    global firstTime
    global operator
    if num1:
        num1 = SquareRoot(num1)
        num2 = ''
        operator = ''
        firstTime = True
        Numbers.config(text=num1)
    elif num2 and not firstTime: # If operating on the second number before equals
        num2 = SquareRoot(num2)
        Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Log_Click():
    global num1
    global num2
    global firstTime
    global operator
    if num1:
        num1 = Logarithm(num1)
        num2 = ''
        operator = ''
        firstTime = True
        Numbers.config(text=num1)
    elif num2 and not firstTime: # If operating on the second number before equals
        num2 = Logarithm(num2)
        Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

window = tk.Tk()
window.title("Simple Calculator")

Numbers = tk.Label(window, text = num1 + ' ' + operator + ' ' + num2, font=('Arial', 24), anchor='e', bg='lightgray', padx=10, pady=10)
Numbers.grid(row=0, column=0, columnspan=5, sticky='ew') # Use grid for better layout

# Create buttons using a loop for numbers and a dictionary for operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('C', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():
        button = tk.Button(window, text=text, command=lambda t=text: On_Number_Click(t), height=3, width=7)
    elif text == '.':
        button = tk.Button(window, text=text, command=On_Decimal_Click, height=3, width=7)
    elif text in ['+', '-', '*', '/']:
        button = tk.Button(window, text=text, command=lambda t=text: On_Operator_Click(t), height=3, width=7)
    elif text == '=':
        button = tk.Button(window, text=text, command=On_Equal_Click, height=3, width=7, bg='lightblue')
    elif text == 'sqrt':
        button = tk.Button(window, text='sqrt', command=On_Sqrt_Click, height=3, width=7, bg='lightgreen')
    elif text == 'log':
        button = tk.Button(window, text='log', command=On_Log_Click, height=3, width=7, bg='lightgreen')
    elif text == 'C':
        button = tk.Button(window, text='C', command=On_Clear_Click, height=3, width=7, bg='orange')
    
    button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

# Configure grid to expand with window
for i in range(5):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

ExitButton = tk.Button(window, text = "EXIT", command = On_Exitbutton_Click, height = 2, bg='salmon')
ExitButton.grid(row=5, column=0, columnspan=5, sticky='ew', padx=2, pady=2)

window.mainloop()
import tkinter as tk
import math

num1 = ''
num2 = ''
operator = ''
firstTime = True

def Addition(num1, num2):
    try:
        return str(float(num1) + float(num2))
    except ValueError:
        return "Error"

def Subtraction(num1, num2):
    try:
        return str(float(num1) - float(num2))
    except ValueError:
        return "Error"

def Multiplication(num1, num2):
    try:
        return str(float(num1) * float(num2))
    except ValueError:
        return "Error"

def Division(num1, num2):
    try:
        if float(num2) == 0:
            return "Error: Div by 0"
        return str(float(num1) / float(num2))
    except ValueError:
        return "Error"

def SquareRoot(num):
    try:
        val = float(num)
        if val < 0:
            return "Error: Neg Sqrt"
        return str(math.sqrt(val))
    except ValueError:
        return "Error"

def Logarithm(num):
    try:
        val = float(num)
        if val <= 0:
            return "Error: Log <= 0"
        return str(math.log10(val))
    except ValueError:
        return "Error"

def OpChecker(operator, num1, num2):
    if operator == '+':
        return Addition(num1,num2)
    if operator == '-':
        return Subtraction(num1,num2)
    if operator == '/':
        return Division(num1, num2)
    if operator == '*':
        return Multiplication(num1, num2)
    
    return ''

def On_Exitbutton_Click():
    window.destroy()

def On_Number_Click(number):
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += str(number)
    else:
        num2 += str(number)
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Decimal_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        if '.' not in num1:
            num1 += '.'
    else:
        if '.' not in num2:
            num2 += '.'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)


def On_Operator_Click(op):
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        if num1: # Only set operator if num1 is not empty
            firstTime = False
            operator = op
    else:
        if num1 and num2: # Perform calculation if both numbers exist
            num1 = OpChecker(operator, num1, num2)
            operator = op
            num2 = ''
        else: # If only num1 exists, just change the operator
            operator = op
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Equal_Click():
    global num1
    global num2
    global firstTime
    global operator
    if not firstTime and num1 and num2 and operator:
        num1 = OpChecker(operator, num1, num2)
        operator = ''
        num2 = ''
        firstTime = True # Reset for new calculation
    Numbers.config(text=num1)

def On_Clear_Click():
    global num1
    global num2
    global operator
    global firstTime
    num1 = ''
    num2 = ''
    operator = ''
    firstTime = True
    Numbers.config(text='')

def On_Sqrt_Click():
    global num1
    global num2
    global firstTime
    global operator
    if num1:
        num1 = SquareRoot(num1)
        num2 = ''
        operator = ''
        firstTime = True
        Numbers.config(text=num1)
    elif num2 and not firstTime: # If operating on the second number before equals
        num2 = SquareRoot(num2)
        Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

def On_Log_Click():
    global num1
    global num2
    global firstTime
    global operator
    if num1:
        num1 = Logarithm(num1)
        num2 = ''
        operator = ''
        firstTime = True
        Numbers.config(text=num1)
    elif num2 and not firstTime: # If operating on the second number before equals
        num2 = Logarithm(num2)
        Numbers.config(text=num1 + ' ' + operator + ' ' + num2)

window = tk.Tk()
window.title("Simple Calculator")

Numbers = tk.Label(window, text = num1 + ' ' + operator + ' ' + num2, font=('Arial', 24), anchor='e', bg='lightgray', padx=10, pady=10)
Numbers.grid(row=0, column=0, columnspan=5, sticky='ew') # Use grid for better layout

# Create buttons using a loop for numbers and a dictionary for operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('C', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():
        button = tk.Button(window, text=text, command=lambda t=text: On_Number_Click(t), height=3, width=7)
    elif text == '.':
        button = tk.Button(window, text=text, command=On_Decimal_Click, height=3, width=7)
    elif text in ['+', '-', '*', '/']:
        button = tk.Button(window, text=text, command=lambda t=text: On_Operator_Click(t), height=3, width=7)
    elif text == '=':
        button = tk.Button(window, text=text, command=On_Equal_Click, height=3, width=7, bg='lightblue')
    elif text == 'sqrt':
        button = tk.Button(window, text='sqrt', command=On_Sqrt_Click, height=3, width=7, bg='lightgreen')
    elif text == 'log':
        button = tk.Button(window, text='log', command=On_Log_Click, height=3, width=7, bg='lightgreen')
    elif text == 'C':
        button = tk.Button(window, text='C', command=On_Clear_Click, height=3, width=7, bg='orange')
    
    button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

# Configure grid to expand with window
for i in range(5):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i, weight=1)

ExitButton = tk.Button(window, text = "EXIT", command = On_Exitbutton_Click, height = 2, bg='salmon')
ExitButton.grid(row=5, column=0, columnspan=5, sticky='ew', padx=2, pady=2)

window.mainloop()
