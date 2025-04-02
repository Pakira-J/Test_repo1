# This is a simple Python script that prints a message to the console.
# Objective : Take a string input and print it in reverse order.
# Author : Joydeep Pakira
# Date : 2023-10-05
def reverse_string(input_string):
    """
    This function takes a string as input and returns it in reverse order.
    """
    return input_string[::-1]

print("Welcome to the string reversal program!")
user_input = input("Please enter a string to reverse: ")
reversed_string = reverse_string(user_input)
print(f"The reversed string is: {reversed_string}")