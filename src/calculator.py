import math
import re
import tkinter as tk
from tkinter import ttk
from op_queue import OpQueue

class CalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.BUFFER_MAX = 14
        self.result_text = tk.StringVar()
        self.result_text.trace_add("write", self._result_updated)
        self.queue = OpQueue()
        self.errored = False
        self.needs_new_entry = False

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
                                command=lambda: self.calc("/"),
                                name="divide", takefocus=False)
        div_button.grid(column=3, row=1, sticky="nsew")

        # Row 2 buttons
        seven_button = ttk.Button(self, text="7", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press("7"),
                                  name="7", takefocus=False)
        seven_button.grid(column=0, row=2, sticky="nsew")
        eight_button = ttk.Button(self, text="8", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press("8"),
                                  name="8", takefocus=False)
        eight_button.grid(column=1, row=2, sticky="nsew")
        nine_button = ttk.Button(self, text="9", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press("9"),
                                 name="9", takefocus=False)
        nine_button.grid(column=2, row=2, sticky="nsew")
        mul_button = ttk.Button(self, text="X", padding=(0, 10, 0, 10),
                                command=lambda: self.calc("*"),
                                name="multiply", takefocus=False)
        mul_button.grid(column=3, row=2, sticky="nsew")

        # Row 3 buttons
        four_button = ttk.Button(self, text="4", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press("4"),
                                 name="4", takefocus=False)
        four_button.grid(column=0, row=3, sticky="nsew")
        five_button = ttk.Button(self, text="5", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press("5"),
                                 name="5", takefocus=False)
        five_button.grid(column=1, row=3, sticky="nsew")
        six_button = ttk.Button(self, text="6", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press("6"), 
                                name="6", takefocus=False)
        six_button.grid(column=2, row=3, sticky="nsew")
        sub_button = ttk.Button(self, text="-", padding=(0, 10, 0, 10),
                                command=lambda: self.calc("-"),
                                name="subtract", takefocus=False)
        sub_button.grid(column=3, row=3, sticky="nsew")

        # Row 4 buttons
        one_button = ttk.Button(self, text="1", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press("1"),
                                name="1", takefocus=False)
        one_button.grid(column=0, row=4, sticky="nsew")
        two_button = ttk.Button(self, text="2", padding=(0, 10, 0, 10),
                                command=lambda: self.num_press("2"),
                                name="2", takefocus=False)
        two_button.grid(column=1, row=4, sticky="nsew")
        three_button = ttk.Button(self, text="3", padding=(0, 10, 0, 10),
                                  command=lambda: self.num_press("3"),
                                  name="3", takefocus=False)
        three_button.grid(column=2, row=4, sticky="nsew")
        add_button = ttk.Button(self, text="+", padding=(0, 10, 0, 10),
                                command=lambda: self.calc("+"), name="add",
                                takefocus=False)
        add_button.grid(column=3, row=4, sticky="nsew")

        # Row 5 buttons
        sign_button = ttk.Button(self, text="+/-", padding=(0, 10, 0, 10),
                                 command=self.sign, takefocus=False)
        sign_button.grid(column=0, row=5, sticky="nsew")
        zero_button = ttk.Button(self, text="0", padding=(0, 10, 0, 10),
                                 command=lambda: self.num_press("0"),
                                 name="0", takefocus=False)
        zero_button.grid(column=1, row=5, sticky="nsew")
        point_button = ttk.Button(self, text=".", padding=(0, 10, 0, 10),
                                  command=self.dec_point, name="dec_point",
                                  takefocus=False)
        point_button.grid(column=2, row=5, sticky="nsew")
        equal_button = ttk.Button(self, text="=", padding=(0, 10, 0, 10),
                                  command=lambda: self.calc("="),
                                  name="equals", takefocus=False)
        equal_button.grid(column=3, row=5, sticky="nsew")


    def _simulate_button_press(self, button: ttk.Button) -> None:
        button.state(["pressed"])
        button.after(100, lambda: button.state(["!pressed"]))


    def _on_key_down(self, e: tk.Event) -> None:
        match e.char:
            case e.char if re.match(r"\d", e.char):
                self._simulate_button_press(self.children[e.char])
                self.num_press(e.char)
            case ".":
                self._simulate_button_press(self.children["dec_point"])
                self.dec_point()
            case "/":
                self._simulate_button_press(self.children["divide"])
                self.calc("/")
            case "*":
                self._simulate_button_press(self.children["multiply"])
                self.calc("*")
            case "-":
                self._simulate_button_press(self.children["subtract"])
                self.calc("-")
            case "+":
                self._simulate_button_press(self.children["add"])
                self.calc("+")
            case "\x08":
                self._simulate_button_press(self.children["backspace"])
                self.backspace()
            case "=":
                self._simulate_button_press(self.children["equals"])
                self.calc("=")
            case "\r":
                self._simulate_button_press(self.children["equals"])
                self.calc("=")


    def _format_num(self, value: float) -> float | int:
        if math.isclose(0, value - int(value)):
            return int(value)
        return value


    def calc(self, op: str) -> None:
        try:
            if not self.errored:
                if not self.needs_new_entry:
                    self.queue.enqueue(float(self.result_text.get()))
                if op == "=":
                    result = str(self._format_num(self.queue.dequeue()))
                    if len(result) > self.BUFFER_MAX:
                        result = f"{float(result):.2e}"
                    self.result_text.set(result)
                    self.needs_new_entry = False
                else:
                    self.queue.enqueue(op)
                    self.needs_new_entry = True
        except ZeroDivisionError:
            self.result_text.set("Divide by zero")
            self.errored = True
        except OverflowError:
            self.result_text.set("Overflow")
            self.errored = True
        except:
            self.result_text.set("Error")
            self.errored = True
        

    def clear_entry(self) -> None:
        if not self.errored:
            self.result_text.set("")

    
    def clear(self) -> None:
        self.queue.clear()
        self.errored = False
        self.last_was_op = False
        self.clear_entry()


    def backspace(self) -> None:
        if not self.errored:
            text = self.result_text.get()
            if len(text) == 2 and text.startswith("-"):
                self.result_text.set("")
            else:
                text = text[:-1]
                if len(text) > 0 and text[-1] == ".":
                    text = text[:-1]
                self.result_text.set(text)


    def dec_point(self) -> None:
        if not self.errored:
            text = self.result_text.get()
            if text == "" or self.needs_new_entry:
                self.result_text.set("0.")
                self.needs_new_entry = False
            elif "." not in text:
                if len(text) < self.BUFFER_MAX - 1:
                    self.result_text.set(text + ".")


    def sign(self) -> None:
        if not self.errored:
            text = self.result_text.get()
            if text.startswith("-"):
                self.result_text.set(text.removeprefix("-"))
            elif text != "" and not math.isclose(0.0, float(text)):
                self.result_text.set("-" + text)


    def num_press(self, value: str) -> None:
        if not self.errored:
            text = self.result_text.get()
            if self.needs_new_entry:
                self.result_text.set(value)
                self.needs_new_entry = False
            elif len(text) < self.BUFFER_MAX:
                self.result_text.set(text + value)
            elif text.startswith("-") and len(text) == self.BUFFER_MAX:
                self.result_text.set(text + value)