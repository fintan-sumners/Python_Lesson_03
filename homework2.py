while True:
    x = input("Enter True or False (case-insensitive) for x: ")
    if x.lower() == 'true':
        x = True
        break
    elif x.lower() == 'false':
        x = False
        break
    else:
        print('Invalid input. Please enter True or False.')

while True:
    y = input("Enter True or False (case-insensitive) for y: ")
    if y.lower() == 'true':
        y = True
        break
    elif y.lower() == 'false':
        y = False
        break
    else:
        print('Invalid input. Please enter True or False.')

print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)