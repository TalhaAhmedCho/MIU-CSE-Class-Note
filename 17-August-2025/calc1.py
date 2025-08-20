import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry('450x300')

def add():
    num1 = int(n1.get())
    num2 = int(n2.get())
    result = num1 + num2
    lb4.configure(text=str(result))

n1 =tk.StringVar()
n2 =tk.StringVar()
ne1 = tk.Entry(root,textvariable = n1, font=('calibre',10,'normal'))
ne2 = tk.Entry(root,textvariable = n2, font=('calibre',10,'normal'))
lb3 = tk.Label(root, text = "+")
btn2 = tk.Button(root, text = "=" ,
             fg = "red", bg="white", command=add)
lb4 = tk.Label(root, text = "Sum")

ne1.grid(column=0, row=2)
lb3.grid(column=1, row=2)
ne2.grid(column=2, row=2)
btn2.grid(column=3, row=2)
lb4.grid(column=4, row=2)

root.mainloop()





