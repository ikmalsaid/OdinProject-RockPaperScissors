import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=256
        height=530
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_523=tk.Label(root)
        ft = tkFont.Font(family='Verdana',size=12)
        GLabel_523["font"] = ft
        GLabel_523["fg"] = "#333333"
        GLabel_523["justify"] = "center"
        GLabel_523["text"] = "Calculator"
        GLabel_523.place(x=85,y=50,width=90,height=25)

        GLineEdit_395=tk.Entry(root)
        GLineEdit_395["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GLineEdit_395["font"] = ft
        GLineEdit_395["fg"] = "#333333"
        GLineEdit_395["justify"] = "center"
        GLineEdit_395["text"] = "Entry"
        GLineEdit_395["relief"] = "ridge"
        GLineEdit_395.place(x=10,y=110,width=235,height=47)

        GButton_771=tk.Button(root)
        GButton_771["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_771["font"] = ft
        GButton_771["fg"] = "#000000"
        GButton_771["justify"] = "center"
        GButton_771["text"] = "7"
        GButton_771.place(x=10,y=170,width=55,height=55)
        GButton_771["command"] = self.GButton_771_command

        GButton_499=tk.Button(root)
        GButton_499["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_499["font"] = ft
        GButton_499["fg"] = "#000000"
        GButton_499["justify"] = "center"
        GButton_499["text"] = "8"
        GButton_499.place(x=70,y=170,width=55,height=55)
        GButton_499["command"] = self.GButton_499_command

        GButton_114=tk.Button(root)
        GButton_114["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_114["font"] = ft
        GButton_114["fg"] = "#000000"
        GButton_114["justify"] = "center"
        GButton_114["text"] = "9"
        GButton_114.place(x=130,y=170,width=55,height=55)
        GButton_114["command"] = self.GButton_114_command

        GButton_674=tk.Button(root)
        GButton_674["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_674["font"] = ft
        GButton_674["fg"] = "#000000"
        GButton_674["justify"] = "center"
        GButton_674["text"] = "/"
        GButton_674.place(x=190,y=170,width=55,height=55)
        GButton_674["command"] = self.GButton_674_command

        GButton_840=tk.Button(root)
        GButton_840["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_840["font"] = ft
        GButton_840["fg"] = "#000000"
        GButton_840["justify"] = "center"
        GButton_840["text"] = "4"
        GButton_840.place(x=10,y=240,width=55,height=55)
        GButton_840["command"] = self.GButton_840_command

        GButton_271=tk.Button(root)
        GButton_271["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "5"
        GButton_271.place(x=70,y=240,width=55,height=55)
        GButton_271["command"] = self.GButton_271_command

        GButton_735=tk.Button(root)
        GButton_735["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_735["font"] = ft
        GButton_735["fg"] = "#000000"
        GButton_735["justify"] = "center"
        GButton_735["text"] = "*"
        GButton_735.place(x=190,y=240,width=55,height=55)
        GButton_735["command"] = self.GButton_735_command

        GButton_152=tk.Button(root)
        GButton_152["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_152["font"] = ft
        GButton_152["fg"] = "#000000"
        GButton_152["justify"] = "center"
        GButton_152["text"] = "6"
        GButton_152.place(x=130,y=240,width=55,height=55)
        GButton_152["command"] = self.GButton_152_command

        GButton_424=tk.Button(root)
        GButton_424["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_424["font"] = ft
        GButton_424["fg"] = "#000000"
        GButton_424["justify"] = "center"
        GButton_424["text"] = "1"
        GButton_424.place(x=10,y=310,width=55,height=55)
        GButton_424["command"] = self.GButton_424_command

        GButton_470=tk.Button(root)
        GButton_470["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_470["font"] = ft
        GButton_470["fg"] = "#000000"
        GButton_470["justify"] = "center"
        GButton_470["text"] = "2"
        GButton_470.place(x=70,y=310,width=55,height=55)
        GButton_470["command"] = self.GButton_470_command

        GButton_71=tk.Button(root)
        GButton_71["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "3"
        GButton_71.place(x=130,y=310,width=55,height=55)
        GButton_71["command"] = self.GButton_71_command

        GButton_399=tk.Button(root)
        GButton_399["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_399["font"] = ft
        GButton_399["fg"] = "#000000"
        GButton_399["justify"] = "center"
        GButton_399["text"] = "-"
        GButton_399.place(x=190,y=310,width=55,height=55)
        GButton_399["command"] = self.GButton_399_command

        GButton_878=tk.Button(root)
        GButton_878["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_878["font"] = ft
        GButton_878["fg"] = "#000000"
        GButton_878["justify"] = "center"
        GButton_878["text"] = "0"
        GButton_878.place(x=10,y=380,width=115,height=55)
        GButton_878["command"] = self.GButton_878_command

        GButton_462=tk.Button(root)
        GButton_462["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_462["font"] = ft
        GButton_462["fg"] = "#000000"
        GButton_462["justify"] = "center"
        GButton_462["text"] = "."
        GButton_462.place(x=130,y=380,width=55,height=55)
        GButton_462["command"] = self.GButton_462_command

        GButton_351=tk.Button(root)
        GButton_351["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_351["font"] = ft
        GButton_351["fg"] = "#000000"
        GButton_351["justify"] = "center"
        GButton_351["text"] = "+"
        GButton_351.place(x=190,y=380,width=55,height=55)
        GButton_351["command"] = self.GButton_351_command

        GButton_344=tk.Button(root)
        GButton_344["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_344["font"] = ft
        GButton_344["fg"] = "#000000"
        GButton_344["justify"] = "center"
        GButton_344["text"] = "Clear"
        GButton_344.place(x=10,y=450,width=115,height=55)
        GButton_344["command"] = self.GButton_344_command

        GButton_920=tk.Button(root)
        GButton_920["bg"] = "#d0d0d0"
        ft = tkFont.Font(family='Verdana',size=12)
        GButton_920["font"] = ft
        GButton_920["fg"] = "#000000"
        GButton_920["justify"] = "center"
        GButton_920["text"] = "Equal"
        GButton_920.place(x=130,y=450,width=115,height=55)
        GButton_920["command"] = self.GButton_920_command

    def GButton_771_command(self):
        GLineEdit_395[text] += '7'


    def GButton_499_command(self):
        print("command")


    def GButton_114_command(self):
        print("command")


    def GButton_674_command(self):
        print("command")


    def GButton_840_command(self):
        print("command")


    def GButton_271_command(self):
        print("command")


    def GButton_735_command(self):
        print("command")


    def GButton_152_command(self):
        print("command")


    def GButton_424_command(self):
        print("command")


    def GButton_470_command(self):
        print("command")


    def GButton_71_command(self):
        print("command")


    def GButton_399_command(self):
        print("command")


    def GButton_878_command(self):
        print("command")


    def GButton_462_command(self):
        print("command")


    def GButton_351_command(self):
        print("command")


    def GButton_344_command(self):
        print("command")


    def GButton_920_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()