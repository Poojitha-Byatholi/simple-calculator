from tkinter import *
import re
def run_calculator():
    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Modern Calculator")
            master.configure(bg='#121212')
            master.resizable(True, True)

            self.equation = ''

            # Create display frame
            display_frame = Frame(master, bg="#121212")
            display_frame.grid(row=0, column=0, columnspan=4, pady=(20, 10))

            # Display field
            self.screen = Text(display_frame, state='disabled', width=24, height=2,
                               background="#1f1f1f", foreground="#ffffff",
                               font=("Segoe UI", 24, "bold"), bd=0, relief=FLAT,
                               padx=10, pady=10)
            self.screen.pack()

            # Button layout
            button_frame = Frame(master, bg="#121212")
            button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

            buttons = [
                ('7', True), ('8', True), ('9', True), ('⌫', None),
                ('4', True), ('5', True), ('6', True), ('÷', True),
                ('1', True), ('2', True), ('3', True), ('*', True),
                ('.', True), ('0', True), ('+', True), ('-', True),
                ('=', None)
            ]
            count = 0
            for row in range(4):
                for col in range(4):
                    (text, write) = buttons[count]
                    self.createButton(button_frame, text, write).grid(row=row, column=col, padx=6, pady=6)
                    count += 1

            # Equal button at bottom
            self.createButton(button_frame, '=', None, width=32).grid(row=4, column=0, columnspan=4, pady=(10, 0))

        def createButton(self, parent, val, write=True, width=7):
            return Button(parent, text=val,
                          command=lambda: self.click(val, write),
                          width=width, height=2,
                          bg="#2c2c2c", fg="#ffffff",
                          font=("Segoe UI", 16, "bold"),
                          bd=0, relief=RAISED,
                          activebackground="#3a99d8", activeforeground="white",
                          cursor="hand2")

        def click(self, text, write):
            if write is None:
                if text == '=' and self.equation:
                    try:
                        expression = re.sub('÷', '/', self.equation)
                        result = str(eval(expression))
                        self.equation = result
                        self.update_screen(result)
                    except:
                        self.equation = ''
                        self.update_screen("Error")
                elif text == '⌫':
                    self.equation = self.equation[:-1]
                    self.update_screen(self.equation)
            else:
                self.equation += str(text)
                self.update_screen(self.equation)

        def update_screen(self, value):
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)
            self.screen.insert(END, value)
            self.screen.configure(state='disabled')

    root = Tk()
    Calculator(root)
    root.mainloop()

run_calculator()
