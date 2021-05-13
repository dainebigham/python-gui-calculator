import tkinter as tk

def main(): 
    window = tk.Tk()

    greeting = tk.Label(window, text="Hello, Welcom to PyCalc")
    text = tk.Text(window, height=2, width=20).grid(row=0, column=0, columnspan=4, padx=5, pady=5)
    button_clr = tk.Button(window, text=' C ', width=10).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    button_div = tk.Button(window, text=' / ', width=3).grid(row=2, column=2, padx=5, pady=5)
    button_mult = tk.Button(window, text=' * ', width=3).grid(row=2, column=3, padx=5, pady=5)
    button_sub = tk.Button(window, text=' - ', width=3).grid(row=3, column=3, padx=5, pady=5)
    button_add = tk.Button(window, text=' + ', width=3).grid(row=4, column=3, padx=5, pady=5)
    button_mod = tk.Button(window, text=' % ', width=3).grid(row=5, column=3, padx=5, pady=5)
    button_dec = tk.Button(window, text=' . ', width=3).grid(row=6, column=2, padx=5, pady=5)
    button_enter = tk.Button(window, text=' = ', width=3).grid(row=6, column=3, padx=5, pady=5)
    button1 = tk.Button(window, text=' 1 ', width=3).grid(row=3, column=0, padx=5, pady=5)
    button2 = tk.Button(window, text=' 2 ', width=3).grid(row=3, column=1, padx=5, pady=5)
    button3 = tk.Button(window, text=' 3 ', width=3).grid(row=3, column=2, padx=5, pady=5)
    button4 = tk.Button(window, text=' 4 ', width=3).grid(row=4, column=0, padx=5, pady=5)
    button5 = tk.Button(window, text=' 5 ', width=3).grid(row=4, column=1, padx=5, pady=5)
    button6 = tk.Button(window, text=' 6 ', width=3).grid(row=4, column=2, padx=5, pady=5)
    button7 = tk.Button(window, text=' 7 ', width=3).grid(row=5, column=0, padx=5, pady=5)
    button8 = tk.Button(window, text=' 8 ', width=3).grid(row=5, column=1, padx=5, pady=5)
    button9 = tk.Button(window, text=' 9 ', width=3).grid(row=5, column=2, padx=5, pady=5)
    button0 = tk.Button(window, text=' 0 ', width=3).grid(row=6, column=1, padx=5, pady=5)

    window.mainloop()
main()