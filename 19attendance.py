std = ["Amit", "Riya", "Sneha"]
print("Total students:", len(std))
name = input("Search student: ")
print(name in std)
std.append("Rahul")
std.remove("Sneha")
print("Students:", std)