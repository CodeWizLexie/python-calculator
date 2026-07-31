from math import *


def calculate():
    valid_operation = ['+', '-', '*', '/', '**', '%']

    print (valid_operation)

    operation = input('What math operation do you want to use ? ')

    if operation not in valid_operation:
        print (f"Operation {operation} is not valid.")

    else:
        num1 = input('Enter your first number: ')
        num2 = input('Enter your second number: ')
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError as e:
            print(f"Caught a ValueError as: {e}. Try using a number instead.")

    if operation == '/' and num2 == 0:
        print('You cannot divide by zero!')
        calculate()

    if operation == '+':
        # Addition
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        # Subtraction
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        # Multiplication
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        # Division
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    elif operation == '**':
        # Power
        print('{} ** {} = '.format(num1, num2))
        print(num1 ** num2)
    
    elif operation == '%':
        # Modulus
        print('{} % {} = '.format(num1, num2))
        print(num1 % num2)

    else:
        print('You have not typed a valid operator, please run the program again.')
        
    again()

# Define again() function to prompt user whether they want to use the calculator again
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    
    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()


# Call calculate() outside of the function
calculate()