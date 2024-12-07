import math
import platform
import re
import tkinter as tk
from tkinter import ttk
from opstack import Opstack

class CalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.BUFFER_MAX = 14
        self.result_text = tk.StringVar()
        self.result_text.trace_add("write", self._result_updated)
        self.stack = Opstack()
        self.errored = False
        self.last_was_op = False

        # Set window attributes
        self.geometry("300x400")
        self.resizable(False, False)
        self.title("Calculator")
        self.configure(padx=3, pady=3)

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

        # Row 1 buttons
        ce_button = ttk.Button(self, text="CE", padding=(0, 10, 0, 10), 
                               command=self.clear_entry, takefocus=False)
        ce_button.grid(column=0, row=1, sticky="nsew")
        c_button = ttk.Button(self, text="C", padding=(0, 10, 0, 10),
                              command=self.clear, takefocus=False)
        c_button.grid(column=1, row=1, sticky="nsew")
        bs_button = ttk.Button(self, text="<-", padding=(0, 10, 0, 10),
                               command=self.backspace, name="backspace",
                               takefocus=False)
        bs_button.grid(column=2, row=1, sticky="nsew")
        div_button = ttk.Button(self, text="/", padding=(0, 10, 0, 10),
                                command=lambda: self.push_op("/"),
                                name="divide", takefocus=False)
        div_button.grid(column=3, row=1, sticky="nsew")

        # Row 2 buttons
        seven_button = ttk.Button(self, text="7", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(7), name="7",
                                  takefocus=False)
        seven_button.grid(column=0, row=2, sticky="nsew")
        eight_button = ttk.Button(self, text="8", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(8), name="8",
                                  takefocus=False)
        eight_button.grid(column=1, row=2, sticky="nsew")
        nine_button = ttk.Button(self, text="9", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(9), name="9",
                                 takefocus=False)
        nine_button.grid(column=2, row=2, sticky="nsew")
        mul_button = ttk.Button(self, text="X", padding=(0, 10, 0, 10),
                                command=lambda: self.push_op("*"),
                                name="multiply", takefocus=False)
        mul_button.grid(column=3, row=2, sticky="nsew")

        # Row 3 buttons
        four_button = ttk.Button(self, text="4", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(4), name="4",
                                 takefocus=False)
        four_button.grid(column=0, row=3, sticky="nsew")
        five_button = ttk.Button(self, text="5", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(5), name="5",
                                 takefocus=False)
        five_button.grid(column=1, row=3, sticky="nsew")
        six_button = ttk.Button(self, text="6", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(6), name="6",
                                takefocus=False)
        six_button.grid(column=2, row=3, sticky="nsew")
        sub_button = ttk.Button(self, text="-", padding=(0, 10, 0, 10),
                                command=lambda: self.push_op("-"),
                                name="subtract", takefocus=False)
        sub_button.grid(column=3, row=3, sticky="nsew")

        # Row 4 buttons
        one_button = ttk.Button(self, text="1", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(1), name="1",
                                takefocus=False)
        one_button.grid(column=0, row=4, sticky="nsew")
        two_button = ttk.Button(self, text="2", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press(2), name="2",
                                takefocus=False)
        two_button.grid(column=1, row=4, sticky="nsew")
        three_button = ttk.Button(self, text="3", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press(3), name="3",
                                  takefocus=False)
        three_button.grid(column=2, row=4, sticky="nsew")
        add_button = ttk.Button(self, text="+", padding=(0, 10, 0, 10),
                                command=lambda: self.push_op("+"), name="add",
                                takefocus=False)
        add_button.grid(column=3, row=4, sticky="nsew")

        # Row 5 buttons
        sign_button = ttk.Button(self, text="+/-", padding=(0, 10, 0, 10),
                                 command=self.sign, takefocus=False)
        sign_button.grid(column=0, row=5, sticky="nsew")
        zero_button = ttk.Button(self, text="0", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press(0), name="0",
                                 takefocus=False)
        zero_button.grid(column=1, row=5, sticky="nsew")
        point_button = ttk.Button(self, text=".", padding=(0, 10, 0, 10),
                                  command=self.dec_point, name="dec_point",
                                  takefocus=False)
        point_button.grid(column=2, row=5, sticky="nsew")
        equal_button = ttk.Button(self, text="=", padding=(0, 10, 0, 10),
                                  command=self.solve, name="equals",
                                  takefocus=False)
        equal_button.grid(column=3, row=5, sticky="nsew")


    def _simulate_button_press(self, button: ttk.Button) -> None:
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
                self.push_op("/")
            case "*":
                self._simulate_button_press(self.children["multiply"])
                self.push_op("*")
            case "-":
                self._simulate_button_press(self.children["subtract"])
                self.push_op("-")
            case "+":
                self._simulate_button_press(self.children["add"])
                self.push_op("+")
            case "\x08":
                self._simulate_button_press(self.children["backspace"])
                self.backspace()
            case "=":
                self._simulate_button_press(self.children["equals"])
                self.solve()
            case "\r":
                self._simulate_button_press(self.children["equals"])
                self.solve()

    
    def push_op(self, op: str) -> None:
        if self.last_was_op:
            self.stack.push(op)
        else:
            if self.stack.count() == 3:
                self.solve()
            value = self.result_text.get()
            if value.startswith("-"):
                self.stack.push(-1 * float(value))
            else:
                self.stack.push(float(value))
            self.stack.push(op)
            self.last_was_op = True
        

    def clear_entry(self) -> None:
        if not self.errored:
            self.result_text.set("")

    
    def clear(self) -> None:
        self.stack.reset()
        self.errored = False
        self.last_was_op = False
        self.clear_entry()


    def backspace(self) -> None:
        if not self.errored:
            self.result_text.set(self.result_text.get()[:-1])


    def solve(self) -> None:
        try:
            if not self.errored:
                if self.stack.count() == 2:
                    self.stack.push(float(self.result_text.get()))
                result = str(self.stack.solve())
                if len(result) > self.BUFFER_MAX:
                    raise OverflowError()
                self.result_text.set(result)
                self.last_was_op = True
        except ZeroDivisionError:
            self.result_text.set("Divide by zero")
            self.errored = True
        except OverflowError:
            self.result_text.set("Overflow")
            self.errored = True
        except:
            self.result_text.set("Error")
            self.errored = True


    def dec_point(self) -> None:
        if not self.errored:
            cur_val = self.result_text.get()
            if cur_val == "" or self.last_was_op:
                self.result_text.set("0.")
            elif "." not in cur_val:
                if len(cur_val) < self.BUFFER_MAX - 1:
                    self.result_text.set(cur_val + ".")
            self.last_was_op = False


    def sign(self) -> None:
        if not self.errored:
            cur_val = self.result_text.get()
            if cur_val.startswith("-"):
                cur_val = cur_val.removeprefix("-")
                self.result_text.set(cur_val)
            elif cur_val != "" and not math.isclose(0.0, float(cur_val)):
                cur_val = "-" + cur_val
                self.result_text.set(cur_val)


    def num_press(self, value: int) -> None:
        if not self.errored:
            cur_val = self.result_text.get()
            if self.last_was_op:
                self.result_text.set(str(value))
            elif (len(cur_val) < self.BUFFER_MAX
                  or (cur_val.startswith("-") and len(cur_val) == self.BUFFER_MAX)):
                self.result_text.set(cur_val + str(value))
            self.last_was_op = False
