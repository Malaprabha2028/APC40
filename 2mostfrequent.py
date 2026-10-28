s = input("Enter a string: ")
chars = []
for ch in s:
    if ch not in chars:
        chars.append(ch)
chars.sort(key=s.count, reverse=True)
if len(chars) >= 2:
    print("Second most frequent:", chars[1])
    print("Frequency:", s.count(chars[1]))
else:
    print("No second frequent character")