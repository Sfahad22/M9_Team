# M9_Team

# This is a simple calculator program. Users can perform calculations such as addition, subtraction, multiplication, and division. 
# Users enter two numbers, the operator, and the results will be displayed.
# Updated on: November 24
# Updated by: Martin, Fahad
#
#
# This block of code imports * from tkinder (import * is used to import all the variables, functions, and classes into the current calculator module).
# Then the title of root is set as "simple Calculator."
from tkinter import *

root = Tk()

root.title("Simple Calculator")

# This sets the size of the calculator and the grid of buttons.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Defines the function: button_click with the parameter number. When a number button is clicked it will add that number to the current one.
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# When the clear button is pressed the line will delete and the calculation ends.
def button_clear():
    e.delete(0, END)

# Defines the function: button_operator. When an operator button is clicked such as +, -, *, or / it will save that number and operator before performing a calculation. 
# It also converts the first number from a string to an integer.
def button_operator(operator):
    first_number = e.get()
    global f_num
    global num_operator
    f_num = int(first_number)
    num_operator = operator
    e.delete(0, END)

# These lines of code are where the calculation happens.

# When the equal button is pressed the following conditional statements will be executed.
# The function will check which operator was pressed and perform the calculation with that value.
# It also converts the second number from a string to an integer before performing the calculation.
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))
# If the "+" operator is pressed the program will add the first and second numbers.
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))
# If the "*" operator is pressed the program will multiply the first and second numbers.
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))
# If the "/" operator is pressed the program will divide the first and second numbers.
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))
# If the "-" operator is pressed the program will subtract the first and second numbers.
    else:
        e.insert(0, "Invalid!!!")
# If none of the operators are selected it will print "Invalid!!!"

# # Lambda function is used for this code.
# I believe these buttons are created to select if the user wants to enter a number from 0-9 and if they want to add, equal, or want to clear it.
#
#
# NOTE: We did not cover Lambda functions in class. A Lambda Function 
# in Python programming is an anonymous function
# or a function having no name. It is a small and restricted function 
# having no more than one line. In the case below, the Lambda function code
# is calling the code/function button_click() with the numbers 0-9 as the 
# parameter. Just like a normal function, a Lambda function can have multiple
# arguments with one expression. 

button_1 =  Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 =  Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 =  Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 =  Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 =  Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 =  Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 =  Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 =  Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 =  Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 =  Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add =  Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal =  Button(root, text="   =   ", padx=79, pady=20, command=button_equal)
button_clear =  Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# This is the same as the above code but this button is used to subtract, multiply, and divide. To understand it better they also provided buttons with symbols of subtract, multiply & divide. 

# See the description of a Lambda function above
button_subtract =  Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply =  Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide =  Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# The below code assigns buttons in the row and in columns to make it understandable & easier for users.

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# mainloop function is associated with GUI, Tkinter programming library is used.

root.mainloop()
