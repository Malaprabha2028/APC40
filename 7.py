import math
n = int(input("Enter number: "))
r = int(math.sqrt(n))
if r * r == n:
    if r > 1:
        for i in range(2, r):
            if r % i == 0:
                print("Square root is not prime")
                break
        else:
            print("Square root is prime")
    else:
        print("Square root is not prime")
else:
    print("Not a perfect square")