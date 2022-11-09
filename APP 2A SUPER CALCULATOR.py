# APP 2A SUPER CALCULATOR
# DIFF: EASY BUT LENGTHY
# Addition = 0
# Subtraction = 1
# Multiplication = 2
# Division = 3
# Floor division = 4
# Exponention = 5
# Modulus = 6
# Negation = 7
# Compare = 8
# State of Number = 9
def add():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    sum = number1 + number2
    return sum
def sub():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    sub = number1 - number2
    return sub
def multi():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    mult = number1 * number2
    return mult
def div():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    if number2 != 0:
        div  = number1 / number2
        return div
    else:
        return 'Invalid input : Division by zero'
def floor():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    if number2 != 0:
        floor  = number1 / number2
        return floor
    else:
        return 'Invalid input : Division by zero'
def exp():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    if number1 < 0 and number2 < 1:
        return 'Invalid input: Root of negative number'
    else:
        expo = number1 ** number2
        return expo
def mod():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    if number2 != 0:
        modulus  = number1 / number2
        return modulus
    else:
        return 'Invalid input : Division by zero'
def neg():
    number1 = float(input("Number 1: "))
    negatiate = -1* number1
    return negatiate
def comp():
    number1 = float(input("Number 1: "))
    number2 = float(input('Number 2: '))
    if number1 > number2:
        return 'Number 1 is greater'
    elif number1 < number2:
        return 'Number 2 is greater'
    else:
        return 'Both are equal'
def state():
    number1 = float(input("Number 1: "))
    if number1 > 0:
        return 'Number is positive'
    else:
        return 'Number is negative'

decision = float(input('Which Operation you want to perform? (0=Addition, 1=Subtraction, 2=Multiplication, '
                 '3=Division, 4= Floor division, ''5= Exponentiation/ Root Operation, 6= Modulus, 7= Negation, '
                  '8= Compare, 9= State of the number):'))
if decision == 0:
    calc = add()
elif decision == 1:
    calc = sub()
elif decision == 2:
    calc = multi()
elif decision == 3:
    calc = div()
elif decision == 4:
    calc = floor()
elif decision == 5:
    calc = exp()
elif decision == 6:
    calc = mod()
elif decision == 7:
    calc = neg()
elif decision == 8:
    calc = comp()
elif decision == 9:
    calc = state()
if 0<= decision <= 9:
    print(calc)
else:
    print('Invalid operation choice')
