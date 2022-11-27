import math

a = input()

res = 0
degree = 0

for i in reversed(range(0, len(a))):
    res += (int(a[i]) * int(math.pow(2, degree)))
    degree += 1

print(res)