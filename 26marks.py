marks = []

for i in range(20):
    marks.append(int(input("Enter marks: ")))
high = max(marks)
low = min(marks)
avg = sum(marks) / 20
above = sum(x > avg for x in marks)
below = sum(x < avg for x in marks)
print("Highest:", high)
print("Lowest:", low)
print("Average:", avg)
print("Above average:", above)
print("Below average:", below)