#!/usr/bin/env python3
"""
Simple app to remove line-breaks

make just single line of text from input,
with custom line-breaks replacement.

Classes: OneLine
"""

import tkinter as tk
import re
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import BOTH


class OneLine(tk.Tk):
    """Tkinter app window

    Methods:
        __init__()
        no_break()
        copy_to_clipboard

    Fields:
        input text field
        line-break replacemen (implicit single space)
        remove inner whitespaces (implicit YES)
        output text field (auto copy to clipboard)
    """

    def __init__(self):
        """OneLine class constructor"""
        tk.Tk.__init__(self)
        #  window title
        self.title("One Line")
        #  text input field
        self.entry = ScrolledText(self, height=10, width=100)
        self.entry.pack(fill=BOTH, expand=True)
        #  replacement field title
        self.replacement = tk.Label(self,
                                    text="End of line replacement:",
                                    width=100
                                    )
        self.replacement.pack()
        #  input field for linebreak replacement
        self.replacement = tk.Entry(self, width=20)
        self.replacement.pack()
        #  checkbox for multiple spaces removal
        self.multiSpaces = tk.BooleanVar()
        self.multiSpaces.set(True)
        self.choices = tk.Checkbutton(
            self, text="Remove multiple spaces", variable=self.multiSpaces
        )
        self.choices.pack()
        #  main button for text conversion and sending result to clipboard
        self.button = tk.Button(
            #  call for main conversion function
            self, text="NO BREAK & copy to clipboard", command=self.no_break
        )
        self.button.pack()
        #  text output field (editable)
        self.result = ScrolledText(self, height=5, width=100)
        self.result.pack(fill=BOTH, expand=True)
        #  buton to copy output to clipboard (e.g. after editing)
        self.button = tk.Button(
            #  call for helper function
            self, text="copy to clipboard", command=self.copy_to_clipboard
        )
        self.button.pack()
        #  app exit button
        self.button = tk.Button(self,
                                text="exit",
                                padx=20,
                                command=self.destroy)
        self.button.pack(anchor="e")

    def no_break(self):
        """Remove line-breaks 

        This method gets the input from the first text area and
        sends the result to the output field.
        Reads replacement from its input field (implicit single space).
        """
        # settings - reads the  values from input fields
        replace_character = self.replacement.get()
        remove_spaces = self.multiSpaces.get()
        input_text = list(self.entry.get("1.0", "end-1c").split("\n"))

        # processing - tabs to spaces
        input_text = [re.sub("\t+", " ", line.strip()) for line in input_text]
        # remove consecutive spaces if set so
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
        """This method reads the current state of the output area
        and saves it to the clipboard
        """
        edited_output = self.result.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(edited_output)


if __name__ == "__main__":
    """Main application loop"""
    app = OneLine()
    app.mainloop()
