n = int(input("Enter number: "))
i = 2
flag = 0
while i < n:
    if n % i == 0:
        flag = 1
        break
    i = i + 1
if n > 1 and flag == 0:
    print("Prime number")
else:
    print("Not a prime number")