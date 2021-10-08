a = 2
b = 9
c = a
for i in range(a, b+1):
    c = c + i
    if i != b:
        print(i, " + ", end=" ")
    else:
        print(b, " = ", end=" ")
print(c)