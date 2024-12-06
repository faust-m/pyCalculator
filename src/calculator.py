import re
import tkinter as tk
from tkinter import ttk

class CalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.BUFFER_MAX = 14
        self.result_text = tk.StringVar(value="0")
        self.result_text.trace_add("write", self._result_updated)

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

        # Handle key presses
        self.bind("<KeyPress>", self._on_key_down)


    def _result_updated(self, *args) -> None:
        if len(self.result_text.get()) <= self.BUFFER_MAX:
            self.children["result"].configure(font=("Courier", 25))
        else:
            self.children["result"].configure(font=("Courier", 24))
    

    def _create_widgets(self) -> None:
        # Result field
        result_label = ttk.Label(self, textvariable=self.result_text,
                                 background="white", anchor="e",
                                 font=("Courier", 25), relief="sunken",
                                 border=2, padding=(0, 12, 5, 0),
                                 name="result")
        result_label.grid(column=0, columnspan=4, row=0, sticky="nsew")

        # Buttons
        ce_button = ttk.Button(self, text="CE", padding=(0, 10, 0, 10), 
                               command=self.clear_entry)
        ce_button.grid(column=0, row=1, sticky="nsew")
        c_button = ttk.Button(self, text="C", padding=(0, 10, 0, 10),
                              command=self.clear)
        c_button.grid(column=1, row=1, sticky="nsew")
        bs_button = ttk.Button(self, text="<-", padding=(0, 10, 0, 10),
                               command=self.backspace, name="backspace")
        bs_button.grid(column=2, row=1, sticky="nsew")
        div_button = ttk.Button(self, text="/", padding=(0, 10, 0, 10),
                                command=self.divide, name="divide")
        div_button.grid(column=3, row=1, sticky="nsew")
        seven_button = ttk.Button(self, text="7", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(7), name="7")
        seven_button.grid(column=0, row=2, sticky="nsew")
        eight_button = ttk.Button(self, text="8", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(8), name="8")
        eight_button.grid(column=1, row=2, sticky="nsew")
        nine_button = ttk.Button(self, text="9", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(9), name="9")
        nine_button.grid(column=2, row=2, sticky="nsew")
        mul_button = ttk.Button(self, text="X", padding=(0, 10, 0, 10),
                                command=self.multiply, name="multiply")
        mul_button.grid(column=3, row=2, sticky="nsew")
        four_button = ttk.Button(self, text="4", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(4), name="4")
        four_button.grid(column=0, row=3, sticky="nsew")
        five_button = ttk.Button(self, text="5", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(5), name="5")
        five_button.grid(column=1, row=3, sticky="nsew")
        six_button = ttk.Button(self, text="6", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(6), name="6")
        six_button.grid(column=2, row=3, sticky="nsew")
        sub_button = ttk.Button(self, text="-", padding=(0, 10, 0, 10),
                                command=self.subtract, name="subtract")
        sub_button.grid(column=3, row=3, sticky="nsew")
        one_button = ttk.Button(self, text="1", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(1), name="1")
        one_button.grid(column=0, row=4, sticky="nsew")
        two_button = ttk.Button(self, text="2", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(2), name="2")
        two_button.grid(column=1, row=4, sticky="nsew")
        three_button = ttk.Button(self, text="3", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(3), name="3")
        three_button.grid(column=2, row=4, sticky="nsew")
        add_button = ttk.Button(self, text="+", padding=(0, 10, 0, 10),
                                command=self.add, name="add")
        add_button.grid(column=3, row=4, sticky="nsew")
        sign_button = ttk.Button(self, text="+/-", padding=(0, 10, 0, 10),
                                 command=self.sign)
        sign_button.grid(column=0, row=5, sticky="nsew")
        zero_button = ttk.Button(self, text="0", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(0), name="0")
        zero_button.grid(column=1, row=5, sticky="nsew")
        point_button = ttk.Button(self, text=".", padding=(0, 10, 0, 10),
                                  command=self.dec_point, name="dec_point")
        point_button.grid(column=2, row=5, sticky="nsew")
        equal_button = ttk.Button(self, text="=", padding=(0, 10, 0, 10),
                                  command=self.equals, name="equals")
        equal_button.grid(column=3, row=5, sticky="nsew")


    def _simulate_button_press(self, button: ttk.Button):
        button.state(["pressed"])
        button.after(100, lambda: button.state(["!pressed"]))


    def _on_key_down(self, e: tk.Event) -> None:
        match e.char:
            case e.char if re.match(r"\d", e.char):
                self._simulate_button_press(self.children[e.char])
                self.num_press(int(e.char))
            case ".":
                self._simulate_button_press(self.children["dec_point"])
                self.dec_point()
            case "/":
                self._simulate_button_press(self.children["divide"])
                self.divide()
            case "*":
                self._simulate_button_press(self.children["multiply"])
                self.multiply()
            case "-":
                self._simulate_button_press(self.children["subtract"])
                self.subtract()
            case "+":
                self._simulate_button_press(self.children["add"])
                self.add()
            case "=":
                self._simulate_button_press(self.children["equals"])
                self.equals()
            case "\x08":
                self._simulate_button_press(self.children["backspace"])
                self.backspace()


    def clear_entry(self) -> None:
        self.result_text.set("0")

    
    def clear(self) -> None:
        # todo figure out how I'm clearing the operands/operation
        self.clear_entry()


    def backspace(self) -> None:
        self.result_text.set(self.result_text.get()[:-1])
        if self.result_text.get() == "":
            self.clear_entry()


    def divide(self) -> None:
        # todo
        pass


    def multiply(self) -> None:
        # todo
        pass


    def subtract(self) -> None:
        # todo
        pass


    def add(self) -> None:
        # todo
        pass


    def equals(self) -> None:
        # todo
        pass


    def dec_point(self) -> None:
        cur_val = self.result_text.get()
        if (len(cur_val) < self.BUFFER_MAX
            or (cur_val.startswith("-") and len(cur_val) == self.BUFFER_MAX)):
            self.result_text.set(cur_val + ".")


    def sign(self) -> None:
        cur_val = self.result_text.get()
        if cur_val.startswith("-"):
            cur_val = cur_val.removeprefix("-")
            self.result_text.set(cur_val)
        elif cur_val != "0":
            cur_val = "-" + cur_val
            self.result_text.set(cur_val)


    def num_press(self, value: int) -> None:
        cur_val = self.result_text.get()
        if (len(cur_val) < self.BUFFER_MAX
            or (cur_val.startswith("-") and len(cur_val) == self.BUFFER_MAX)):
            if cur_val != "0":
                self.result_text.set(cur_val + str(value))
            else:
                self.result_text.set(str(value))
