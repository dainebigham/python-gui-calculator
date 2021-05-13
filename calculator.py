import tkinter as tk

def main(): 
    window = tk.Tk()

    greeting = tk.Label(window, text="Hello, Welcom to PyCalc")
    T = tk.Text(window, height=2, width=30)
    button_clr = tk.Button(window, text=' C ').grid(row=0, column=0, padx=5, pady=5)
    button_div = tk.Button(window, text=' / ').grid(row=0, column=2, padx=5, pady=5)
    button_mult = tk.Button(window, text=' * ').grid(row=0, column=3, padx=5, pady=5)
    button_sub = tk.Button(window, text=' - ').grid(row=1, column=3, padx=5, pady=5)
    button_add = tk.Button(window, text=' + ').grid(row=2, column=3, padx=5, pady=5)
    button_mod = tk.Button(window, text=' % ').grid(row=3, column=3, padx=5, pady=5)
    button_dec = tk.Button(window, text=' . ').grid(row=4, column=2, padx=5, pady=5)
    button_enter = tk.Button(window, text=' = ').grid(row=4, column=3, padx=5, pady=5)
    button1 = tk.Button(window, text=' 1 ').grid(row=1, column=0, padx=5, pady=5)
    button2 = tk.Button(window, text=' 2 ').grid(row=1, column=1, padx=5, pady=5)
    button3 = tk.Button(window, text=' 3 ').grid(row=1, column=2, padx=5, pady=5)
    button4 = tk.Button(window, text=' 4 ').grid(row=2, column=0, padx=5, pady=5)
    button5 = tk.Button(window, text=' 5 ').grid(row=2, column=1, padx=5, pady=5)
    button6 = tk.Button(window, text=' 6 ').grid(row=2, column=2, padx=5, pady=5)
    button7 = tk.Button(window, text=' 7 ').grid(row=3, column=0, padx=5, pady=5)
    button8 = tk.Button(window, text=' 8 ').grid(row=3, column=1, padx=5, pady=5)
    button9 = tk.Button(window, text=' 9 ').grid(row=3, column=2, padx=5, pady=5)
    button0 = tk.Button(window, text=' 0 ').grid(row=4, column=1, padx=5, pady=5)
    
    #for i in window.children:
        #window.children[i].pack()

    window.mainloop()
main()