names = ["Anjali", "Pranjali"]
ages = [20, 25]
names.append("Diksha")
ages.append(22)
names.remove("Pranjali")
ages.pop(1)
name = input("Search patient: ")
print(name in names)
print("Patients:", names)
print("Ages:", ages)
print("Total patients:", len(names))