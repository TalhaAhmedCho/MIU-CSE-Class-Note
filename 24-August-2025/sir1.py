import tkinter as tk
 
field_text = ""
 
def add_to_field(sth):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)
 
def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    field_text = result
 
def clear():
    global field_text
    field_text = ""
    field.delete("1.0", "end")
 
# Main Window
window = tk.Tk()
window.geometry("300x350")
window.title("Simple Calculator")
 
# Text field
field = tk.Text(window, height=2, width=21, font=("Times New Roman", 20), bg="#e6f7ff")
field.grid(row=1, column=1, columnspan=4)
 
# Number Buttons (Light Blue)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_1.grid(row=2, column=1)
 
btn_2 = tk.Button(window, text="2", command=lambda: add_to_field(2), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_2.grid(row=2, column=2)
 
btn_3 = tk.Button(window, text="3", command=lambda: add_to_field(3), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_3.grid(row=2, column=3)
 
btn_4 = tk.Button(window, text="4", command=lambda: add_to_field(4), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_4.grid(row=3, column=1)
 
btn_5 = tk.Button(window, text="5", command=lambda: add_to_field(5), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_5.grid(row=3, column=2)
 
btn_6 = tk.Button(window, text="6", command=lambda: add_to_field(6), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_6.grid(row=3, column=3)
 
btn_7 = tk.Button(window, text="7", command=lambda: add_to_field(7), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_7.grid(row=4, column=1)
 
btn_8 = tk.Button(window, text="8", command=lambda: add_to_field(8), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_8.grid(row=4, column=2)
 
btn_9 = tk.Button(window, text="9", command=lambda: add_to_field(9), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_9.grid(row=4, column=3)
 
btn_0 = tk.Button(window, text="0", command=lambda: add_to_field(0), width=5, font=("Times New Roman", 15), bg="#cce7ff")
btn_0.grid(row=5, column=1)
 
# Operation Buttons (green)
btn_plus = tk.Button(window, text="+", command=lambda: add_to_field("+"), width=5, font=("Times New Roman", 15), bg="#ffcc80")
btn_plus.grid(row=2, column=4)
 
btn_minus = tk.Button(window, text="-", command=lambda: add_to_field("-"), width=5, font=("Times New Roman", 15), bg="#ffcc80")
btn_minus.grid(row=3, column=4)
 
btn_times = tk.Button(window, text="", command=lambda: add_to_field(""), width=5, font=("Times New Roman", 15), bg="#ffcc80")
btn_times.grid(row=4, column=4)
 
btn_division = tk.Button(window, text="/", command=lambda: add_to_field("/"), width=5, font=("Times New Roman", 15), bg="#ffcc80")
btn_division.grid(row=5, column=4)
 
# Special Buttons
btn_clear = tk.Button(window, text="C", command=clear, width=5, font=("Times New Roman", 15), bg="red", fg="white")
btn_clear.grid(row=5, column=3)
 
btn_decimal = tk.Button(window, text=".", command=lambda: add_to_field("."), width=5, font=("Times New Roman", 15), bg="#99ffcc")
btn_decimal.grid(row=5, column=2)
 
btn_open_parenthesis = tk.Button(window, text="(", command=lambda: add_to_field("("), width=5, font=("Times New Roman", 15), bg="#d9b3ff")
btn_open_parenthesis.grid(row=6, column=1)
 
btn_close_parenthesis = tk.Button(window, text=")", command=lambda: add_to_field(")"), width=5, font=("Times New Roman", 15), bg="#d9b3ff")
btn_close_parenthesis.grid(row=6, column=2)
 
btn_equal = tk.Button(window, text="=", command=calculate, width=5, font=("Times New Roman", 15), bg="#80ff80")
btn_equal.grid(row=6, column=4)

btn_percent = tk.Button(window, text="%", command=lambda: add_to_field("/100"),width=5, font=("Times New Roman", 15), bg="#80ff80")
btn_percent.grid(row=6, column=3) 
window.mainloop()