import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry('450x300')

def add():
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 + num2
    label2.configure(text=str(result))

n1 = tk.StringVar()
n2 = tk.StringVar()

entry1 = tk.Entry(root, textvariable=n1)
entry1.grid(column=0, row=1)

label1 = tk.Label(root, text="+")
label1.grid(column=1, row=1)

entry2 = tk.Entry(root, textvariable=n2)
entry2.grid(column=2, row=1)

btn1 = tk.Button(root, text="=", bg="lightblue", command=add)
btn1.grid(column=3, row=1)

label2 = tk.Label(root, text="Result")
label2.grid(column=4, row=1)

root.mainloop()