import tkinter as tk
from math import *

convert_constant = 1

btn_params = {
    'padx': 16, 'pady': 1, 'bd': 4, 'fg': 'white', 'bg': 'black',
    'font': ('arial', 18), 'width': 2, 'height': 2, 'relief': 'flat', 'activebackground': "black"
}

def fsin(arg):
    return sin(arg * convert_constant)
def fcos(arg):
    return cos(arg * convert_constant)
def ftan(arg):
    return tan(arg * convert_constant)

class Calculator:
    def __init__(self, master):
        self.expression = ""
        self.text_input = tk.StringVar()
        self.master = master
        top_frame = tk.Frame(master, width=650, height=10, bd=10, relief='flat', bg='gray')
        top_frame.pack(side=tk.TOP)
        bottom_frame_buttons = tk.Frame(master, width=650, height=470, bd=2, relief='flat', bg='black')
        bottom_frame_buttons.pack(side=tk.BOTTOM)
        txt_display = tk.Entry(
            top_frame, font=('arial', 36), relief='flat', bg='black', fg='white',
            textvariable=self.text_input, width=60, bd=12, justify='right'
        )
        txt_display.pack()

        buttons = [
            ('C', '+/-', 'sqrt', '%', '7', '8', '9', '/'),
            ('sin', 'cos', 'tan', 'log', '4', '5', '6', '*'),
            ('1/x', 'x^2', 'x^y', 'n!', '1', '2', '3', '-'),
            ('(', ')', 'exp', 'π', '0', '.', '=', '+')
        ]

        for i, button_row in enumerate(buttons):
            for j, button_text in enumerate(button_row):
                command = lambda btn=button_text: self.btn_click(btn)
                if button_text == 'sin':
                    command = lambda btn='fsin(': self.btn_click(btn)
                elif button_text == 'cos':
                    command = lambda btn='fcos(': self.btn_click(btn)
                elif button_text == 'tan':
                    command = lambda btn='ftan(': self.btn_click(btn)
                elif button_text == 'log':
                    command = lambda btn='log(': self.btn_click(btn)
                elif button_text == '1/x':
                    command = lambda btn='1/(': self.btn_click(btn)
                elif button_text == 'x^2':
                    command = lambda btn='**2': self.btn_click(btn)
                elif button_text == 'x^y':
                    command = lambda btn='**': self.btn_click(btn)
                elif button_text == 'n!':
                    command = lambda btn='factorial(': self.btn_click(btn)
                elif button_text == 'exp':
                    command = lambda btn='exp(': self.btn_click(btn)
                elif button_text == 'π':
                    command = lambda btn='pi': self.btn_click(btn)
                elif button_text == 'sqrt':
                    command = lambda btn='sqrt(': self.btn_click(btn)
                elif button_text == '%':
                    command = lambda btn='%(': self.btn_click(btn)

                button = tk.Button(
                    bottom_frame_buttons, **btn_params, text=button_text,
                    command=command
                )
                button.grid(row=i, column=j)

    def btn_click(self, item):
        if item == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
            self.text_input.set(self.expression)
        elif item == '%':
            try:
                result = eval(self.expression) / 100
                self.expression = str(result)
            except:
                self.expression = "Error"
            self.text_input.set(self.expression)
        elif item == 'C':
            self.expression = ""
            self.text_input.set("")
        elif item == '+/-':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
                self.text_input.set(self.expression)
        else:
            self.expression += str(item)
            self.text_input.set(self.expression)

root = tk.Tk()
calc = Calculator(root)
root.title("Calculator")
root.geometry("650x490+50+50")
root.resizable(False, False)
root.mainloop()
