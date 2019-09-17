import tkinter as tk
import re

class OneLine(tk.Tk):
    """
    Simple app to remove line breaks
    and make just single line of text from input.
    """
    def __init__(self): # Tkinter main window
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
        # checkbar with other options
        self.test = tk.BooleanVar() 
        self.test.set(False)
        self.choices = tk.Checkbutton(self, text="Remove multiple spaces", variable=self.test)
        self.choices.pack()
        # exec button
        self.button = tk.Button(self, text="NO END", command=self.noEnd)
        self.button.pack()
        # output field
        self.result = tk.Text(self, height=5, width=100)
        self.result.pack()
        # button to quit the app
        self.button = tk.Button(self, text="exit", padx=20, command=self.destroy)
        self.button.pack(anchor="e")
        

    def noEnd(self): # function to remove line breaks
        # obtaining replacement string
        replaceCharacter = self.replacement.get()
        # reading the input with avoiding the last linebreak
        inputText = self.entry.get('1.0','end-1c')
        # checking if multiple spaces are enabled
        removeSpaces = self.test.get()
        # replacing line breaks
        outputText = inputText.replace("\n", replaceCharacter)
        # removing multiple spaces if enabled
        if removeSpaces == True:
            outputText = re.sub(' +', ' ', outputText)
        # emptying output field before writing the result
        self.result.delete('1.0','end-1c')
        # writing output
        self.result.insert('1.0', outputText)

#initializing the main loop
app = OneLine()
app.mainloop()
