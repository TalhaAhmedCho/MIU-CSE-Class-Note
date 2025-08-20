import tkinter
root = tkinter.Tk()
root.title("Welcome to Batch 67")
root.geometry("550x300")

calc = tkinter.Label(root, text="1 + 2 + 3 + .... + 10 = ?")
calc.grid()

scc = tkinter.Label(root, text="Calculate the sum of numbers from 1 to 10")
scc.grid(column=1, row=1)

def clicked():
    scc.configure(text="100 + 99 + 98 + .... + 1 = ?")

btn = tkinter.Button(root, text="Click Me", fg="red", bg="LightBlue", command=clicked)
btn.grid(column=1, row=3)

root.mainloop()
