def addition(a, b):
    print(a + b)
def subtraction(a, b):
    print(a - b)
def multiplication(a, b):
    print(a * b)
def division(a, b):
    if b == 0:
        print("error")
    else:
        print(a / b)
s = True
while True:
    w = int(input("""You cen preform:
    1)addition
    2)subtraction
    3)multiplication
    4)division
    or
    5)Exet
    """))
    if w == 5:
        break
    x = int(input("First number: "))
    y = int(input("Second number: "))
    if w == 1:
        addition(x, y)
    elif w == 2:
        subtraction(x, y)
    elif w == 3:
        multiplication(x, y)
    elif w == 4:
        division(x, y)





