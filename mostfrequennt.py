s = input("Enter a string: ")
most = s[0]
for ch in s:
    if s.count(ch) > s.count(most):
        most = ch
print("Most frequent character:", most)
print("Frequency:", s.count(most))