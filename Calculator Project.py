from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title('Calculator V1')  # Sets the window title
        master.geometry('357x420+0+0')  # Use 'x' instead of '×'
        master.config(bg='black')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=20, bg='gold', font=('Helvetica', 28), textvariable=self.equation).place(x=0, y=0)

        # Buttons for the calculator
        Button(width=10, height=3, text='(', relief='groove', bg='dark grey', command=lambda: self.show('(')).place(x=0, y=50)
        Button(width=10, height=3, text=')', relief='groove', bg='dark grey', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=10, height=3, text='%', relief='groove', bg='dark grey', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=10, height=3, text='1', relief='groove', bg='dark grey', command=lambda: self.show('1')).place(x=0, y=125)
        Button(width=10, height=3, text='2', relief='groove', bg='dark grey', command=lambda: self.show('2')).place(x=90, y=125)
        Button(width=10, height=3, text='3', relief='groove', bg='dark grey', command=lambda: self.show('3')).place(x=180, y=125)
        Button(width=10, height=3, text='4', relief='groove', bg='dark grey', command=lambda: self.show('3')).place(x=0, y=200)
        Button(width=10, height=3, text='5', relief='groove', bg='dark grey', command=lambda: self.show('5')).place(x=90, y=200)
        Button(width=10, height=3, text='6', relief='groove', bg='dark grey', command=lambda: self.show('6')).place(x=180, y=200)
        Button(width=10, height=3, text='7', relief='groove', bg='dark grey', command=lambda: self.show('7')).place(x=0, y=275)
        Button(width=10, height=3, text='8', relief='groove', bg='dark grey', command=lambda: self.show('8')).place(x=90, y=275)
        Button(width=10, height=3, text='9', relief='groove', bg='dark grey', command=lambda: self.show('9')).place(x=180, y=275)
        Button(width=10, height=3, text='0', relief='groove', bg='dark grey', command=lambda: self.show('0')).place(x=90, y=350)
        Button(width=10, height=3, text='.', relief='groove', bg='dark grey', command=lambda: self.show('.')).place(x=180, y=350)
        Button(width=10, height=3, text='+', relief='groove', bg='dark grey', command=lambda: self.show('+')).place(x=270, y=125)
        Button(width=10, height=3, text='-', relief='groove', bg='dark grey', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=10, height=3, text='/', relief='groove', bg='dark grey', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=10, height=3, text='*', relief='groove', bg='dark grey', command=lambda: self.show('*')).place(x=270, y=275)
        Button(width=10, height=3, text='=', relief='groove', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=10, height=3, text='C', relief='groove', bg='red', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''


root = Tk()
app = Calculator(root)
root.mainloop()