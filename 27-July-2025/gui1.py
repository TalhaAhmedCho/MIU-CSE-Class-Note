import tkinter
root = tkinter.Tk()
root.title("Welcome to batch 67")
root.geometry('550x300')

july = tkinter.Label(root, text = "First July Celebration, 2025 !")
july.grid()
august = tkinter.Label(root, text = "Chhotrishe July")
august.grid(column = 1, row=1)

def clicked():
    august.configure(text = "You are clicking to change text")

btn = tkinter.Button(root, text = "Click me" ,
             fg = "red", bg="lightblue", command=clicked)
btn.grid(column=1, row=3)

root.mainloop()
