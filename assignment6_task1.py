import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Simple Calculator")


entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ["1", "2", "3", "/"],
    ["4", "5", "6", "*"],
    ["7", "8", "9", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack()
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", width=4, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()