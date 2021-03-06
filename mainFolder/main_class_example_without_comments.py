"""
Program: this_file_name.py
Author:  Firstname Lastname
Date: MM/DD/YYYY

Change this description to be more relevant.
This program creates a function that prints 'Hello World'
as output.  The function is then called.
"""

PI = 3.14159265358979323

def hello_world():
    print('hello world!')

def get_pi(x):
    if (x):
        return PI
    else:
        return 0

def get_user_input_once():
    user_input = input("please enter a value")
    return user_input

def get_user_input_twice():
    user_input_one = input("please enter a value")
    user_input_two = input("please enter a different value")
    return_string = "You input " + user_input_one + " and " + user_input_two + "."
    return return_string

if __name__ == '__main__':
    #call our functions
    hello_world()
    boolean_value_variable = True
    #store it as a variable since get_pi returns a value
    pi_value = get_pi(boolean_value_variable)
    #cast it as a string before printing!
    print("The value of pi is " + str(pi_value))

