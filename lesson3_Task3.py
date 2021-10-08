print("ax^2+bx+c=0")
c = 11
print("c =", c)
a = int(input("a = "))
b = int(input("b = "))
if (b**2-4*a*c) > 0:
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print("x1 =", x1)
    print("x2 =", x2)
elif (b**2-4*a*c) < 0:
    print("x != R")
elif (b**2-4*a*c) == 0:
    x = -b/(2*a)
    print("x =", x)