import tkinter as tk

# create 360x640 window
gui = tk.Tk()
gui.title('SimpleCalc')
gui.geometry('360x640')

# functions
def calculate(formula):
    print(eval(str(formula)))
    pass

def button_key(pressed):
    print(str(pressed))
    pass

def clear_screen():
    pass

# widgets


# run window
gui.mainloop()