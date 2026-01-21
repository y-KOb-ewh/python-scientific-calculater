import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Scientific Calculator")
        self.root.geometry("400x600")

        # ディスプレイ部分
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # ボタンの配置定義
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            'sin', 'cos', 'tan', 'log',
            '(', ')', 'sqrt', '='
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_click(x)
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_click(self, char):
        if char == '=':
            try:
                # evalは便利ですが、セキュリティ上注意が必要な関数です
                # math関数の名前を適切に置換して計算
                expression = self.result_var.get().replace('sin', 'math.sin').replace('cos', 'math.cos').replace('log', 'math.log10').replace('sqrt', 'math.sqrt')
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "計算式が正しくありません")
        elif char == 'C':
            self.result_var.set("")
        else:
            current = self.result_var.get()
            self.result_var.set(current + str(char))

if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()