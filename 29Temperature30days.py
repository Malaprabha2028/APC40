temp = []
for i in range(30):
    temp.append(float(input("Enter temperature: ")))
avg = sum(temp) / 30
print("Hottest:", max(temp))
print("Coldest:", min(temp))
print("Average:", avg)
print("Above average:", sum(x > avg for x in temp))
print("Below average:", sum(x < avg for x in temp))