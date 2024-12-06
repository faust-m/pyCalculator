import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.BUFFER_MAX = 14
        self.result_text = tk.StringVar(value="0")

        # Set window attributes
        self.geometry("300x400")
        self.title("Calculator")
        self.configure(padx=3, pady=3)
        self.resizable(False, False)

        # Configure the grid
        self.columnconfigure((0, 1, 2, 3), weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Create widgets in the grid
        self._create_widgets()

        # Create key bindings
        self._create_bindings()
    

    def _create_widgets(self) -> None:
        # Result field
        result_label = ttk.Label(self, textvariable=self.result_text,
                                 background="white", anchor="e",
                                 font=("Courier", 25), relief="sunken",
                                 border=2, padding=(0, 12, 5, 0))
        result_label.grid(column=0, columnspan=4, row=0, sticky="nsew")

        # Buttons
        ce_button = ttk.Button(self, text="CE", padding=(0, 0, 0, 0), 
                               command=self.clear_entry)
        ce_button.grid(column=0, row=1, sticky="nsew")
        c_button = ttk.Button(self, text="C", padding=(0, 10, 0, 10),
                              command=self.clear)
        c_button.grid(column=1, row=1, sticky="nsew")
        bs_button = ttk.Button(self, text="<-", padding=(0, 10, 0, 10),
                               command=self.backspace)
        bs_button.grid(column=2, row=1, sticky="nsew")
        bs_button.bind()
        div_button = ttk.Button(self, text="/", padding=(0, 10, 0, 10),
                                command=self.divide)
        div_button.grid(column=3, row=1, sticky="nsew")
        seven_button = ttk.Button(self, text="7", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(7))
        seven_button.grid(column=0, row=2, sticky="nsew")
        eight_button = ttk.Button(self, text="8", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(8))
        eight_button.grid(column=1, row=2, sticky="nsew")
        nine_button = ttk.Button(self, text="9", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(9))
        nine_button.grid(column=2, row=2, sticky="nsew")
        mul_button = ttk.Button(self, text="X", padding=(0, 10, 0, 10),
                                command=self.multiply)
        mul_button.grid(column=3, row=2, sticky="nsew")
        four_button = ttk.Button(self, text="4", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(4))
        four_button.grid(column=0, row=3, sticky="nsew")
        five_button = ttk.Button(self, text="5", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(5))
        five_button.grid(column=1, row=3, sticky="nsew")
        six_button = ttk.Button(self, text="6", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(6))
        six_button.grid(column=2, row=3, sticky="nsew")
        sub_button = ttk.Button(self, text="-", padding=(0, 10, 0, 10),
                                command=self.subtract)
        sub_button.grid(column=3, row=3, sticky="nsew")
        one_button = ttk.Button(self, text="1", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(1))
        one_button.grid(column=0, row=4, sticky="nsew")
        two_button = ttk.Button(self, text="2", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(2))
        two_button.grid(column=1, row=4, sticky="nsew")
        three_button = ttk.Button(self, text="3", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(3))
        three_button.grid(column=2, row=4, sticky="nsew")
        add_button = ttk.Button(self, text="+", padding=(0, 10, 0, 10),
                                command=self.add)
        add_button.grid(column=3, row=4, sticky="nsew")
        sign_button = ttk.Button(self, text="+/-", padding=(0, 10, 0, 10),
                                 command=self.sign)
        sign_button.grid(column=0, row=5, sticky="nsew")
        zero_button = ttk.Button(self, text="0", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(0))
        zero_button.grid(column=1, row=5, sticky="nsew")
        point_button = ttk.Button(self, text=".", padding=(0, 10, 0, 10),
                                  command=self.dec_point)
        point_button.grid(column=2, row=5, sticky="nsew")
        equal_button = ttk.Button(self, text="=", padding=(0, 10, 0, 10),
                                  command=self.equals)
        equal_button.grid(column=3, row=5, sticky="nsew")


    def _create_bindings(self) -> None:
        # todo
        # finish bindings
        for i in range(0, 10):
            self.bind(str(i), func=lambda i: self.num_press(i))


    def clear_entry(self) -> None:
        # todo
        print("Clear Entry pressed")

    
    def clear(self) -> None:
        # todo
        print("Clear pressed")


    def backspace(self) -> None:
        # todo
        print("Backspace pressed")


    def divide(self) -> None:
        # todo
        print("Divide pressed")


    def multiply(self) -> None:
        # todo
        print("Multiply pressed")


    def subtract(self) -> None:
        # todo
        print("Subtract pressed")


    def add(self) -> None:
        # todo
        print("Add pressed")


    def equals(self) -> None:
        # todo
        print("Equals pressed")


    def dec_point(self) -> None:
        # todo
        print("Decimal Point pressed")


    def sign(self) -> None:
        # todo
        print("Sign pressed")


    def num_press(self, value: int) -> None:
        # todo
        # make sure buffer doesn't overflow
        print(f"{value} pressed")
        cur_val = self.result_text.get()
        if (cur_val != "0") and (len(cur_val) < self.BUFFER_MAX):
            self.result_text.set(cur_val + str(value))
        else:
            self.result_text.set(str(value))

