import math

a2 = []
for x in range(round(math.sqrt(600851475143 ))):
    if((600851475143 % (x+1)) == 0):
        a2.append(x)
print(a2[-2:])
