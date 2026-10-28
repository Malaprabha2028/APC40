a = [10, 25, 5, 40, 15]
large = small = a[0]
for x in a:
    if x > large:
        large = x
    if x < small:
        small = x
print("Largest =", large)
print("Smallest =", small)