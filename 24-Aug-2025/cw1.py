import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry('450x300')

# 1st Row
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

# 2nd Row
def subtract():
    num3 = int(n3.get())
    num4 = int(n4.get())
    result = num3 - num4
    label4.configure(text=str(result)) 

n3 = tk.StringVar()
n4 = tk.StringVar()

entry3 = tk.Entry(root, textvariable=n3)
entry3.grid(column=0, row=2)

label3 = tk.Label(root, text="-")
label3.grid(column=1, row=2)

entry4 = tk.Entry(root, textvariable=n4)
entry4.grid(column=2, row=2)

btn2 = tk.Button(root, text="=", bg="lightblue", command=subtract)
btn2.grid(column=3, row=2)

label4 = tk.Label(root, text="Result")
label4.grid(column=4, row=2)


# 3rd Row
def product():
    num5 = int(n5.get())
    num6 = int(n6.get())
    result = num5 * num6
    label6.configure(text=str(result))

n5 = tk.StringVar()
n6 = tk.StringVar()

entry5 = tk.Entry(root, textvariable=n5)
entry5.grid(column=0, row=3)

label5 = tk.Label(root, text="*")
label5.grid(column=1, row=3)

entry6 = tk.Entry(root, textvariable=n6)
entry6.grid(column=2, row=3)

btn3 = tk.Button(root, text="=", bg="lightblue", command=product)
btn3.grid(column=3, row=3)

label6 = tk.Label(root, text="Result")
label6.grid(column=4, row=3)

# 4th Row
def divide():
    num5 = int(n7.get())
    num6 = int(n8.get())
    result = num5 / num6
    label8.configure(text=str(result))

n7 = tk.StringVar()
n8 = tk.StringVar()

entry5 = tk.Entry(root, textvariable=n7)
entry5.grid(column=0, row=4)

label5 = tk.Label(root, text="/")
label5.grid(column=1, row=4)

entry6 = tk.Entry(root, textvariable=n8)
entry6.grid(column=2, row=4)

btn3 = tk.Button(root, text="=", bg="lightblue", command=divide)
btn3.grid(column=3, row=4)

label8 = tk.Label(root, text="Result")
label8.grid(column=4, row=4)

root.mainloop()