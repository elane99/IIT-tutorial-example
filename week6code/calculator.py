def average_of_three(a, b, c):
    return (a + b + c) / 3
import tkinter as tk

def average_of_three(a, b, c):
    return (a + b + c) / 3

def compute():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())
        avg = average_of_three(m1, m2, m3)
        result_var.set(f"Average: {avg:.1f}")
        status_var.set("Passed" if avg >= 50 else "Failed")
    except ValueError:
        result_var.set("")
        status_var.set("Invalid input.")

root = tk.Tk()
root.title("Student Marks Calculator")

tk.Label(root, text="Mark 1:").grid(row=0, column=0, padx=6, pady=6)
entry1 = tk.Entry(root, width=8)
entry1.grid(row=0, column=1, padx=6, pady=6)

tk.Label(root, text="Mark 2:").grid(row=1, column=0, padx=6, pady=6)
entry2 = tk.Entry(root, width=8)
entry2.grid(row=1, column=1, padx=6, pady=6)

tk.Label(root, text="Mark 3:").grid(row=2, column=0, padx=6, pady=6)
entry3 = tk.Entry(root, width=8)
entry3.grid(row=2, column=1, padx=6, pady=6)

tk.Button(root, text="Compute Average", command=compute).grid(row=3, column=0, columnspan=2, pady=8)

result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=2)

status_var = tk.StringVar(value="")
tk.Label(root, textvariable=status_var, font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=4)

root.mainloop()
