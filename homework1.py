while True:
    try:
        num1 = int(input('Enter the first number: '))
        break
    except ValueError:
        print('Invalid input. Please enter a number.')

while True:
    try:
        num2 = int(input('Enter the second number: '))
        break
    except ValueError:
        print('Invalid input. Please enter a number.')

op1 = input('Please enter the operator (+, -, *, /, %, //), **:')

if op1 == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif op1 == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif op1 == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif op1 == '/':
    if num1 == 0:
        print('Zero cannot be divided')
    elif num2 == 0:
        print('Cannot divide by zero')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
elif op1 == '%':
    print(f'{num1} % {num2} = {num1 % num2}')
elif op1 == '//':
    print(f'{num1} // {num2} = {num1 // num2}')
elif op1 == '**':
    print(f'{num1} ** {num2} = {num1 ** num2}')
else: print('Invalid operator. Please enter a valid operator.')