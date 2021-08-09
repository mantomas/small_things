#!/usr/bin/env python3

import tkinter as tk
import re
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import BOTH


class OneLine(tk.Tk):
    """
    Simple app to remove line-breaks

    make just single line of text from input,
    with custom line-breaks replacement.
    """

    def __init__(self):
        """app window

        - input text field
        - line-break replacemen (implicit single space)
        - remove inner whitespaces (implicit YES)
        - output text field (auto copy to clipboard)
        """
        tk.Tk.__init__(self)

        self.title("One Line")

        self.entry = ScrolledText(self, height=10, width=100)
        self.entry.pack(fill=BOTH, expand=True)

        self.replacement = tk.Label(self,
                                    text="End of line replacement:",
                                    width=100
                                    )
        self.replacement.pack()
        self.replacement = tk.Entry(self, width=20)
        self.replacement.pack()

        self.multiSpaces = tk.BooleanVar()
        self.multiSpaces.set(True)
        self.choices = tk.Checkbutton(
            self, text="Remove multiple spaces", variable=self.multiSpaces
        )
        self.choices.pack()

        self.button = tk.Button(
            self, text="NO BREAK & copy to clipboard", command=self.no_break
        )
        self.button.pack()

        self.result = ScrolledText(self, height=5, width=100)
        self.result.pack(fill=BOTH, expand=True)

        self.button = tk.Button(
            self, text="copy to clipboard", command=self.copy_to_clipboard
        )
        self.button.pack()

        self.button = tk.Button(self,
                                text="exit",
                                padx=20,
                                command=self.destroy)
        self.button.pack(anchor="e")

    def no_break(self):
        """remove line-breaks

        and replace them with set value
        single space if not defined
        """
        # settings
        replace_character = self.replacement.get()
        remove_spaces = self.multiSpaces.get()
        input_text = list(self.entry.get("1.0", "end-1c").split("\n"))

        # processing - tabs to spaces
        input_text = [re.sub("\t+", " ", line.strip()) for line in input_text]
        # will remove consecutive spaces if set so
        input_text = [
            re.sub(" +", " ", line.strip()) if remove_spaces else line.strip()
            for line in input_text
            ]
        # remove empty lines
        input_text = [line for line in input_text if line != ""]

        # joining to one line
        if replace_character:
            output_text = replace_character.join(input_text)
        else:
            output_text = " ".join(input_text)

        # writing result - add to clipboard
        self.result.delete("1.0", "end-1c")
        self.result.insert("1.0", output_text)
        self.clipboard_clear()
        self.clipboard_append(output_text)

    def copy_to_clipboard(self):
        edited_output = self.result.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(edited_output)


if __name__ == "__main__":
    app = OneLine()
    app.mainloop()
