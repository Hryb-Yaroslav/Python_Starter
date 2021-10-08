a = int(input("Start list: "))
b = int(input("End list: "))
c = 0
d = []
for i in range(a, b+1):
    for g in range(1, b+1):
        q = i / g
        for t in range(1, b+1):
            if q == t:
                c = c + 1
    if c == 2:
        d.append(i)
    c = 0
print(d)
f = input("Calculate the amount this numbers = 1 or calculate multiplication this numbers = 2: ")
if f == "1":
    res = 0
    for amo in d:
       res += amo
elif f == "2":
    res = 1
    for amo in d:
        res = res * amo
print(res)