s = input("Enter a string: ")
duplicate = ""
for ch in s:
    if s.count(ch) > 1 and ch not in duplicate:
        duplicate += ch
print("Duplicate characters:", duplicate)