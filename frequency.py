s = input("Enter a string: ")
ch = input("Enter character to find: ")
count = 0
for x in s:
   if x == ch:
      count += 1
print("Frequency:", count)