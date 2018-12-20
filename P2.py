a1 = []
a,b = 1,1
while b < 4000000:
    if(b%2 == 0):
        a1.append(b)
    a, b = b, a+b


y = 0
for x in range(len(a1)):
    y+= a1[x]

print(y)
