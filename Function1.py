
def greeting(name):             #  The function needs to be defined first
    print("Hello", name)

# Main Program
input_name = input("Enter your name:\n")    # The 1st line of code that isnt in a definition is where the program starts.
# Enter your name is displayed and the input is saved in input_name variable

greeting(input_name)             # Before the function is called # The next line is then run which is a call to the
# greeting () function and the value of input_name is passed in which is trish
# Since we call the function greeting() we now go to the function and the value of input_name is passed in. Then we
# go to the next line print and the name that was passed in by input_name to name is printed to the screen

# once it has run the greeting function () it goes to the next line of code which is the end of the program

print("Thanks", name) # this will throw an error as this is outside of the function but if you move it into the function
# it will run. This is called scope. We have Global and Local Scope.

# If a variable is created inside the main body of program it is a GLOBAL variable and has global scope. That means it
# can be used anywhere.

# So if we rewrite the program and put the variable inside the Main body of the program

def greeting():
    print("Hello", name)

# Main Program
name = input("Enter your name:\n") # The variable name is global
greeting()                         # We dont need a parameter for greeting() since it can reference the global variable

#  THIS CAN BECOME MESSY SO BE SURE YOU WANT THESE GLOBAL, the name variable is still used so what if we want to ask the
#  user for another name - check out python for beginners course Functions - 4:58
#  Lets try example again with local scope

def greeting(name):             #  The function needs to be defined first
    print("Hello", name)

#  Main Program
name1 = input("Enter your name:\n")
greeting(name1)
name2 = input("Enter your name:\n")
greeting(name2)

# The above asks for name 1 and sends to function and prints Hello Name1 then the same with name2

# Reasons to create functions
# You want to reuse that chunk of code over and over

# Organise your code by logical units


# We want a simple function that adds two numbers and returns the result
# def keyword # function name # 2 parameters a & b
def addition(a, b):
    return a + b # The return keyword is used to return a value or even a s sequence of values. # This code here is the Function definition

# Main Program
def main():
    num1 = float(input("Enter your first number:\n"))
    num2 = float(input("Enter your second number:\n"))

# call the function
    result = addition(num1, num2)
    print("The result is", result)

main()

# Much better, much neater

