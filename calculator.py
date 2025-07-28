import tkinter as tk
num1 = ''
num2 = ''
operator = ''
firstTime = True
def Addition(num1, num2):
    return str(int(num1) + int(num2))
def Subtraction(num1, num2):
    return str(int(num1) - int(num2))
def Multiplication(num1, num2):
    return str(int(num1) * int(num2))
def Division(num1, num2):
    return str(int(num1) / int(num2))
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
def On_Nine_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '9'
    else:
        num2 += '9'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Eight_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '8'
    else:
        num2 += '8'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Seven_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '7'
    else:
        num2 += '7'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Six_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '6'
    else:
        num2 += '6'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Five_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '5'
    else:
        num2 += '5'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Four_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '4'
    else:
        num2 += '4'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Three_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '3'
    else:
        num2 += '3'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Two_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '2'
    else:
        num2 += '2'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_One_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '1'
    else:
        num2 += '1'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Zero_Click():
    global num1
    global num2
    global firstTime
    if firstTime:
        num1 += '0'
    else:
        num2 += '0'
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Addition_Click():
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        firstTime = False
        operator = '+'
    else:
        num1 = OpChecker(operator, num1, num2)
        operator = '+'
        num2 = ''
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Subtraction_Click():
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        firstTime = False
        operator = '-'
    else:
        num1 = OpChecker(operator, num1, num2)
        operator = '-'
        num2 = ''
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Multiplication_Click():
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        firstTime = False
        operator = '*'
    else:
        num1 = OpChecker(operator, num1, num2)
        operator = '*'
        num2 = ''
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Division_Click():
    global num1
    global num2
    global firstTime
    global operator
    if firstTime:
        firstTime = False
        operator = '/'
    else:
        num1 = OpChecker(operator, num1, num2)
        operator = '/'
        num2 = ''
    Numbers.config(text=num1 + ' ' + operator + ' ' + num2)
def On_Equal_Click():
    global num1
    global num2
    global firstTime
    global operator
    if not firstTime:
        num1 = OpChecker(operator, num1, num2)
        operator = ''
        num2 = ''
    Numbers.config(text=num1)

    window = tk.Tk()


Numbers = tk.Label(text = num1 + ' ' + operator + ' ' + num2)
Numbers.pack(side=tk.TOP)
NineButton = tk.Button(text = "9", command = On_Nine_Click, height = 3)
NineButton.pack(side=tk.LEFT)
EightButton = tk.Button(text = "8", command = On_Eight_Click, height = 3)
EightButton.pack(side=tk.LEFT)
SevenButton = tk.Button(text = "7", command = On_Seven_Click, height = 3)
SevenButton.pack(side=tk.LEFT)
SixButton = tk.Button(text = "6", command = On_Six_Click, height = 3)
SixButton.pack(side=tk.LEFT)
FiveButton = tk.Button(text = "5", command = On_Five_Click, height = 3)
FiveButton.pack(side=tk.LEFT)
FourButton = tk.Button(text = "4", command = On_Four_Click, height = 3)
FourButton.pack(side=tk.LEFT)
ThreeButton = tk.Button(text = "3", command = On_Three_Click, height = 3)
ThreeButton.pack(side=tk.LEFT)
TwoButton = tk.Button(text = "2", command = On_Two_Click, height = 3)
TwoButton.pack(side=tk.LEFT)
OneButton = tk.Button(text = "1", command = On_One_Click, height = 3)
OneButton.pack(side=tk.LEFT)
ZeroButton = tk.Button(text = "0", command = On_Zero_Click, height = 3)
ZeroButton.pack(side=tk.LEFT)
AdditionButton = tk.Button(text='+', command = On_Addition_Click, height = 3)
AdditionButton.pack(side=tk.LEFT)
SubtractionButton = tk.Button(text='-', command = On_Subtraction_Click, height = 3)
SubtractionButton.pack(side=tk.LEFT)
MultiplicationButton = tk.Button(text='*', command = On_Multiplication_Click, height = 3)
MultiplicationButton.pack(side=tk.LEFT)
DivisionButton = tk.Button(text='/', command = On_Division_Click, height = 3)
DivisionButton.pack(side=tk.LEFT)
EqualButton = tk.Button(text='=', command = On_Equal_Click, height = 3)
EqualButton.pack(side=tk.LEFT)


ExitButton = tk.Button(text = "EXIT", command = On_Exitbutton_Click)
ExitButton.pack(side=tk.BOTTOM, ipadx = 25)

window.mainloop()





