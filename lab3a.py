#!/usr/bin/env python3

# Author ID: [sshrestha80]

def return_text_value():
    return "Good Morning Terry"

def return_number_value():
    number1 = 10
    number2 = 5
    return number1 + number2


if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
