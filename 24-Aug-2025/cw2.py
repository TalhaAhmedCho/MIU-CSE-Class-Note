import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry('450x300')

def add():
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 + num2
    label2.configure(text=str(result))

def subtract():
    num3 = int(n1.get())
    num4 = int(n2.get())
    result = num3 - num4
    label2.configure(text=str(result))

def multiply():
    num5 = int(n1.get())
    num6 = int(n2.get())
    result = num5 * num6
    label2.configure(text=str(result))

def divide():
    num7 = int(n1.get())
    num8 = int(n2.get())
    result = num7 / num8
    label2.configure(text=str(result))

n1 = tk.StringVar()
n2 = tk.StringVar()

entry1 = tk.Entry(root, textvariable=n1)
entry1.grid(column=0, row=1)

btn1 = tk.Button(root, text="+", bg="lightblue", command=add)
btn1.grid(column=1, row=1)

btn2 = tk.Button(root, text="-", bg="lightblue", command=subtract)
btn2.grid(column=2, row=1)

btn3 = tk.Button(root, text="*", bg="lightblue", command=multiply)
btn3.grid(column=3, row=1)

btn4 = tk.Button(root, text="/", bg="lightblue", command=divide)
btn4.grid(column=4, row=1)

entry2 = tk.Entry(root, textvariable=n2)
entry2.grid(column=5, row=1)

label2 = tk.Label(root, text="Result")
label2.grid(column=6, row=1)

root.mainloop()