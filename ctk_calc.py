import customtkinter as tk

calc = tk.CTk()

calc.geometry("360x640")

calc.title("SimpleCalc")

calcTitle = tk.CTkLabel(calc, text='Calculator', font=tk.CTkFont(size=18,weight='bold')); calcTitle.pack(pady=(40,20))

calc.mainloop()