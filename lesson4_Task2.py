n = int(input("Enter your factorial: "))
c = 1
for i in range(1, n+1):
    c = c * i
print(n,"! =",c)