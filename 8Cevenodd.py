a = []
for i in range(15):
    a.append(int(input("Enter number: ")))
even = odd = 0
for x in a:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even =", even)
print("Odd =", odd)