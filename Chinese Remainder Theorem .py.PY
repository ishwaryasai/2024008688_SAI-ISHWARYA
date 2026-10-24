//CHINESEREMAINDERTHEOROM
from math import prod

a = [5, 3, 2]
m = [3, 6, 8]

M = prod(m)
result = 0

for i in range(len(m)):
    Mi = M // m[i]
    inverse = pow(Mi, -1, m[i])
    result += a[i] * Mi * inverse

x = result % M

print("Chinese Remainder =", x)
