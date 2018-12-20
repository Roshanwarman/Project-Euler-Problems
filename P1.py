a = []

for x in range (1000):
    if((x%3 == 0) or (x%5 == 0)):
        a.append(x)

y = 0
for x in range(len(a)):
    y+= a[x]
print(y)
