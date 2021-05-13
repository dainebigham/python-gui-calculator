import tkinter as tk

# function to load any button clicks into a global variable that will be displayed on screen
def press(item): 
    global expression

    # concatenate button presses into variable expression
    expression += str(item)
    # set StringVar equation to value of expression variable
    equation.set(expression)

# funtion to clear the global variable expression to default 
def clear():
    global expression

    # set expression to no text and set equation to expression
    expression = ""
    equation.set(expression)

# function to run the current calculation and get result
def enter():
    global expression

    # use eval() function to evaluate the expression and turn it into a string
    total = str(eval(expression))
    # set equation to the value of the result of the eval() function
    equation.set(total)
    # reset global expression variable
    expression = ""

# create window, set window title, size, and constant size
window = tk.Tk()
window.title("PyCalc")
window.geometry("210x255")
window.resizable(False, False)

# global variable expression and StringVar equation
expression = ""
equation = tk.StringVar()

# create text display window and set its value to be that of StringVar equation
text = tk.Entry(window, textvariable=equation, width=32).grid(row=0, column=0, columnspan=4, padx=5, pady=5)
# create layout of calculator window using grid manager and call correct funtion and arguments for button presses
button_clr = tk.Button(window, text=' C ', width=10, command=lambda: clear()).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
button_div = tk.Button(window, text=' / ', width=3, command=lambda: press('/')).grid(row=2, column=2, padx=5, pady=5)
button_mult = tk.Button(window, text=' * ', width=3, command=lambda: press('*')).grid(row=2, column=3, padx=5, pady=5)
button_sub = tk.Button(window, text=' - ', width=3, command=lambda: press('-')).grid(row=3, column=3, padx=5, pady=5)
button_add = tk.Button(window, text=' + ', width=3, command=lambda: press('+')).grid(row=4, column=3, padx=5, pady=5)
button_mod = tk.Button(window, text=' % ', width=3, command=lambda: press('%')).grid(row=5, column=3, padx=5, pady=5)
button_dec = tk.Button(window, text=' . ', width=3, command=lambda: press('>')).grid(row=6, column=0, padx=5, pady=5)
button_enter = tk.Button(window, text=' = ', width=10, command=enter).grid(row=6, column=2, columnspan=2, padx=5, pady=5)
button1 = tk.Button(window, text=' 1 ', command=lambda: press('1'), width=3).grid(row=3, column=0, padx=5, pady=5)
button2 = tk.Button(window, text=' 2 ', command=lambda: press('2'), width=3).grid(row=3, column=1, padx=5, pady=5)
button3 = tk.Button(window, text=' 3 ', command=lambda: press('3'), width=3).grid(row=3, column=2, padx=5, pady=5)
button4 = tk.Button(window, text=' 4 ', command=lambda: press('4'), width=3).grid(row=4, column=0, padx=5, pady=5)
button5 = tk.Button(window, text=' 5 ', command=lambda: press('5'), width=3).grid(row=4, column=1, padx=5, pady=5)
button6 = tk.Button(window, text=' 6 ', command=lambda: press('6'), width=3).grid(row=4, column=2, padx=5, pady=5)
button7 = tk.Button(window, text=' 7 ', command=lambda: press('7'), width=3).grid(row=5, column=0, padx=5, pady=5)
button8 = tk.Button(window, text=' 8 ', command=lambda: press('8'), width=3).grid(row=5, column=1, padx=5, pady=5)
button9 = tk.Button(window, text=' 9 ', command=lambda: press('9'), width=3).grid(row=5, column=2, padx=5, pady=5)
button0 = tk.Button(window, text=' 0 ', command=lambda: press('0'), width=3).grid(row=6, column=1, padx=5, pady=5)

# start the calculator window
window.mainloop()