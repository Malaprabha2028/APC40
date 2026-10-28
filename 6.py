import math

x = float(input("Enter x: "))
n = int(input("Enter n: "))
s = 0
for i in range(n + 1):
    term = (x ** (2 * i)) / math.factorial(2 * i)

    if i % 2 == 0:
        s = s + term
    else:
        s = s - term

print("Cos(x) =", s)