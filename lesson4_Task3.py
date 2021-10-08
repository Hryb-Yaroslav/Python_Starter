number = int(input())
a = "\ "
b = "|"
c = "_"
C = "_"
d = " "
D = " "
number -= 1
for i in range(0, number):
    if i > -1:
        c = c+C
    if i > 0:
        d = d+D
    print(b+d+a)
    if i == number-1:
        print(b+c+a)