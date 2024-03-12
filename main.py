import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.result_var = tk.StringVar()

        # Entry widget to display the results
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=('Helvetica', 16), bd=10, insertwidth=4, width=14, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            '(', ')', 'C', 'π'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            btn = tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.button_click(b))
            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Bind keyboard events
        master.bind('<KeyPress>', self.key_pressed)

    def button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == "C":
            self.result_var.set("")
        elif button_text == "π":
            self.result_var.set(current_text + str(math.pi))
        elif button_text == "sqrt":
            try:
                result = math.sqrt(float(current_text))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + button_text)

    def key_pressed(self, event):
        key = event.char
        allowed_chars = "0123456789+-*/.()"

        if key in allowed_chars:
            self.button_click(key)
        elif key == '\r':  # Check for Enter key
            self.button_click("=")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
