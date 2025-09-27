import math
import tkinter as tk
from tkinter import ttk


history = []

def calculate(expr):
    try:
        expr = expr.replace("√", "math.sqrt").replace("^", "**")
        expr = expr.replace("sin", "math.sin(math.radians(")
        expr = expr.replace("cos", "math.cos(math.radians(")
        expr = expr.replace("tan", "math.tan(math.radians(")
        expr = expr.replace("log", "math.log10(")
        expr = expr + ")" * expr.count("(") if "math." in expr else expr
        result = eval(expr)
        history.append(f"{expr} = {result}")
        update_history()
        return str(result)
    except:
        return "Error"

def update_history():
    history_box.config(state='normal')
    history_box.delete(1.0, tk.END)
    for line in history[-10:]:
        history_box.insert(tk.END, line + "\n")
    history_box.config(state='disabled')

def button_click(value):
    if value == "=":
        result = calculate(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    elif value == "C":
        entry.delete(0, tk.END)
    elif value == "⌫":
        entry.delete(len(entry.get())-1, tk.END)
    else:
        entry.insert(tk.END, value)

# ----------------------------
# GUI
# ----------------------------
root = tk.Tk()
root.title(" Modern Scientific Calculator")
root.geometry("480x600")
root.configure(bg="#1b1b2f")

# Style for ttk
style = ttk.Style(root)
style.theme_use('clam')

# Entry Display
entry = tk.Entry(root, font=("Helvetica", 24), bd=0, bg="#1b1b2f", fg="white", justify='right', insertbackground='white')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=15, sticky="we")

# History Panel
history_box = tk.Text(root, width=35, height=8, bg="#262626", fg="white", font=("Helvetica", 12), bd=0, state='disabled')
history_box.grid(row=1, column=0, columnspan=5, padx=10, pady=5, sticky="we")

# Buttons Layout
buttons = [
    ["7","8","9","/","sin"],
    ["4","5","6","*","cos"],
    ["1","2","3","-","tan"],
    ["0",".","^","+","log"],
    ["√","(",")","⌫","C"],
    ["="]
]

# Button Colors
colors = {
    "num": "#3e3e8e",
    "op": "#ff9500",
    "func": "#00b894",
    "C": "#d63031",
    "⌫": "#fdcb6e",
    "=": "#6c5ce7"
}

# Create Buttons
row_start = 2
for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        color = colors.get(label, colors["num"])
        btn = tk.Button(root, text=label, font=("Helvetica", 16, "bold"),
                        bg=color, fg="white", activebackground="#555", activeforeground="white",
                        bd=0, relief="ridge", command=lambda x=label: button_click(x))
        btn.grid(row=r+row_start, column=c, padx=5, pady=5, ipadx=12, ipady=12, sticky="nsew")


for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(row_start, row_start+6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
