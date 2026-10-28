import tkinter as tk
from tkinter import ttk


def submit():
    name = name_entry.get()
    div = div_entry.get()
    mob = mob_entry.get()
    branch = branch_entry.get()
    email = email_entry.get()

    with open("data.txt", "a") as f:
        f.write(name + "," + div + "," + mob + "," + branch + "," + email + "\n")

    result.config(text="Record Saved Successfully!")


def read():
    # New page/window
    new_page = tk.Toplevel(root)
    new_page.title("Student Records")
    new_page.geometry("800x400")

    tk.Label(
        new_page,
        text="Student Records",
        font=("Arial", 22)
    ).pack(pady=20)

    table = ttk.Treeview(
        new_page,
        columns=("Name", "Division", "Mobile", "Branch", "Email"),
        show="headings"
    )

    for col in ("Name", "Division", "Mobile", "Branch", "Email"):
        table.heading(col, text=col)

    table.pack(fill="both", expand=True, padx=20, pady=20)

    # Read data
    try:
        with open("data.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")

                if len(data) == 5:
                    table.insert("", "end", values=data)

    except FileNotFoundError:
        tk.Label(new_page, text="No records found").pack()


# Main window
root = tk.Tk()
root.title("Student Application")
root.geometry("500x650")


tk.Label(
    root,
    text="Application Web Page",
    font=("Arial", 24)
).pack(pady=20)


tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Division").pack()
div_entry = tk.Entry(root)
div_entry.pack()

tk.Label(root, text="Mobile").pack()
mob_entry = tk.Entry(root)
mob_entry.pack()

tk.Label(root, text="Branch").pack()
branch_entry = tk.Entry(root)
branch_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()


tk.Button(root, text="Submit", command=submit).pack(pady=15)

tk.Button(root, text="Read", command=read).pack()

result = tk.Label(root, text="")
result.pack(pady=20)


root.mainloop()