import tkinter as tk

# Track User Input
user_expression = ""

# Update Display
def press_key(key):
    global user_expression
    user_expression += str(key)
    display.config(text=user_expression)

# Clear Display
def clear_display():
    global user_expression
    user_expression = ""
    display.config(text=user_expression)

# Calculate Result
def calculate_result():
    global user_expression
    result = eval(user_expression)
    display.config(text=result)
    user_expression = str(result)

# Main window
window = tk.Tk()
window.title("Calculator")

# Display Label
display = tk.Label(window, bg="white", anchor="e", font=("Arial", 20), bd=2, relief="groove")
display.grid(row=0, column=0, columnspan=4, ipady=20, sticky="we")

# Make Buttons
button_params = {"width":5, "height":2, "font":("Arial", 14)}
def make_buttons(text, row, col, cmd=None, bg=None):
    if cmd is None:
        cmd = lambda: press_key(text)
    return tk.Button(window, text=text, command=cmd, bg=bg, **button_params).grid(row=row, column=col)

# Number Buttons
make_buttons("0", 4, 0)
make_buttons("1", 1, 0)
make_buttons("2", 1, 1)
make_buttons("3", 1, 2)
make_buttons("4", 2, 0)
make_buttons("5", 2, 1)
make_buttons("6", 2, 2)
make_buttons("7", 3, 0)
make_buttons("8", 3, 1)
make_buttons("9", 3, 2)

# Operators
make_buttons("+", 1, 3)
make_buttons("-", 2, 3)
make_buttons("*", 4, 1)
make_buttons("/", 4, 2)

# Equal Button
make_buttons("=", 4, 3, cmd=calculate_result)

# Clear Button
make_buttons("C", 3, 3, cmd=clear_display, bg="red")

window.mainloop()