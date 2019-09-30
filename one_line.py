import tkinter as tk
import re


class OneLine(tk.Tk):
    """
    Simple app to remove line breaks
    and make just single line of text from input.
    """

    def __init__(self):  # Tkinter main window
        tk.Tk.__init__(self)
        # window title
        self.title('One Line')
        # field for input text
        self.entry = tk.Text(self, height=10, width=100)
        self.entry.pack()
        # input of character or string to replace end of the line
        self.replacement = tk.Label(self, text="Replacement for the end of the line:", width=100)
        self.replacement.pack()
        self.replacement = tk.Entry(self, width=20)
        self.replacement.pack()
        # removing multiple spaces
        self.multiSpace = tk.BooleanVar()
        self.multiSpace.set(False)
        self.choices = tk.Checkbutton(self, text="Remove multiple spaces", variable=self.multiSpace)
        self.choices.pack()
        # exec button
        self.button = tk.Button(self, text="NO END", command=self.no_end)
        self.button.pack()
        # output field
        self.result = tk.Text(self, height=5, width=100)
        self.result.pack()
        # button to quit the app
        self.button = tk.Button(self, text="exit", padx=20, command=self.destroy)
        self.button.pack(anchor="e")

    def no_end(self):  # function to remove line breaks
        # obtaining replacement string
        replace_character = self.replacement.get()
        # reading the input with avoiding the last linebreak
        input_text = self.entry.get('1.0', 'end-1c')
        # checking if multiple spaces are enabled
        remove_spaces = self.multiSpace.get()
        # removing multiple consecutive linebreaks on empty lines
        input_text = re.sub("\n+", '\n', input_text)
        # removing linebreak and tabulator at the beginning of string, if any and avoiding only linebreak input
        if len(input_text) > 0:
            while input_text[0] == "\n" or input_text[0] == "\t":
                input_text = input_text[1:]
                if len(input_text) < 1:
                    break
        # removing linebreak and tabulator at the end of string, if any and avoiding only linebreak input
        if len(input_text) > 0:
            while input_text[-1] == "\n" or input_text[-1] == "\t":
                input_text = input_text[:-1]
                if len(input_text) < 1:
                    break
        # replacing tabulators with single spaces
        input_text = re.sub("\t", ' ', input_text)
        # replacing line breaks
        output_text = input_text.replace("\n", replace_character)
        # removing multiple spaces if enabled
        if remove_spaces is True:
            output_text = re.sub(' +', ' ', output_text)
        # emptying output field before writing the result
        self.result.delete('1.0', 'end-1c')
        # writing output
        self.result.insert('1.0', output_text)


# initializing the main loop
app = OneLine()
app.mainloop()
