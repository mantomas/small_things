#!/usr/bin/env python3

import tkinter as tk
import re
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import BOTH


class OneLine(tk.Tk):
    """
    Simple app to remove line breaks

    make just single line of text from input,
    with custom linebreaks replacement.
    """

    def __init__(self):
        tk.Tk.__init__(self)

        self.title('One Line')

        self.entry = ScrolledText(self, height=10, width=100)
        self.entry.pack(fill=BOTH, expand=True)
        # input of character or string to replace end of the line
        self.replacement = tk.Label(
            self, text="Replacement for the end of the line:", width=100)
        self.replacement.pack()
        self.replacement = tk.Entry(self, width=20)
        self.replacement.pack()
        # removing multiple spaces
        self.multiSpace = tk.BooleanVar()
        self.multiSpace.set(False)
        self.choices = tk.Checkbutton(
            self, text="Remove multiple spaces", variable=self.multiSpace)
        self.choices.pack()
        # exec button
        self.button = tk.Button(self, text="NO END", command=self.no_end)
        self.button.pack()
        # output field
        self.result = ScrolledText(self, height=5, width=100)
        self.result.pack(fill=BOTH, expand=True)
        # button to quit the app
        self.button = tk.Button(
            self, text="exit", padx=20, command=self.destroy
            )
        self.button.pack(anchor="e")

    def no_end(self):  # function to remove line breaks
        # obtaining replacement string
        replace_character = self.replacement.get()
        # reading the input with avoiding the last linebreak
        input_text = self.entry.get('1.0', 'end-1c').strip()
        # checking if multiple spaces are enabled
        remove_spaces = self.multiSpace.get()
         # replacing tabulators with single spaces
        input_text = re.sub("\t+", ' ', input_text)
        # removing multiple consecutive linebreaks on empty lines
        input_text = re.sub("\n+", '\n', input_text)
        # replacing line breaks
        output_text = input_text.replace("\n", replace_character)
        # removing multiple spaces if enabled
        if remove_spaces is True:
            output_text = re.sub(' +', ' ', output_text)
        # emptying output field before writing the result
        self.result.delete('1.0', 'end-1c')
        # writing output
        self.result.insert('1.0', output_text)


if __name__ == "__main__":
    app = OneLine()
    app.mainloop()
