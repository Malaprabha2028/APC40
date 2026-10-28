s = input("Enter a string: ")

for ch in s:
    if s.count(ch) > 1:
        if s.index(ch) == s.index(ch):
            print(ch, end=" ")