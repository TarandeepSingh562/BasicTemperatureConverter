from tkinter import *
from tkinter import messagebox

#Creates a class
class MyGUI:
    def __init__(self):
        root = Tk()
        root.geometry("400x200")
        root.title("Temperature Conversion")

        # creates a Frame
        frame = Frame(root)
        frame.pack(fill = BOTH, expand = True)

        #creates a label
        label1 = Label(frame, text="Enter number to convert")
        label1.pack(side=TOP, expand=True, fill=BOTH)

        # provides entry box for user
        self.entry = Entry(frame)
        self.entry.pack(side=TOP, expand=True, fill=BOTH)

        # displays the first label
        display1 = Label(frame)
        display1.pack(side=TOP, expand=True, fill=BOTH)

        # creates a button for Convert to convert fahrenheit into celsius
        button1 = Button(frame, text="Convert to Celsius", command=self.convert)
        button1.pack(side=TOP, expand=True, fill=BOTH)

        # creates a button for Convert to convert celsius into fahrenheit
        button2 = Button(frame, text="Convert to Fahrenheit", command=self.convert1)
        button2.pack(side=TOP, expand=True, fill=BOTH)

        # creates a button for Quit to quit the program
        button3 = Button(text="Quit", fg="Red", command=quit)
        button3.pack(side=TOP, expand=True, fill=BOTH)

        root.mainloop()

    def convert(self):
        for char in self.entry.get():
            if not char.isdigit() and char != ".":
                return messagebox.showinfo("Error!", "Please enter a number")
            else:
                Tf = float(self.entry.get())
                Tc = (5 / 9) * (Tf - 32)
                C = "{:12.4f}".format(Tc)
                # creates a messagebox for the answer
                return messagebox.showinfo("Fahrenheit to Celsius conversion",
                                    str(Tf) + " Fahrenheit to Celsius conversion is: " + str(C) + " Celsius")

    def convert1(self):
        for char1 in self.entry.get():
            if not char1.isdigit() and char1 != ".":
                return messagebox.showinfo("Error!", "Please enter a number")
            else:
                tc = float(self.entry.get())
                tf = ((9 / 5) * tc) + 32
                F = "{:12.4f}".format(tf)
                # creates a messagebox for the answer
                return messagebox.showinfo("Celsius to Fahrenheit conversion",
                                    str(tc) + " Celsius to Fahrenheit conversion is: " + str(F) + " Fahrenheit")


my_gui = MyGUI()
