import tkinter as tk

class Odlamovac(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Odlamovač')
        self.entry = tk.Text(self, height=10, width=100)
        self.entry.pack()
        self.nahradnik = tk.Label(self, text="Znak pro nahrazení konce řádku:", width=100)
        self.nahradnik.pack()
        self.nahradnik = tk.Entry(self, width=20)
        self.nahradnik.pack()
        self.button = tk.Button(self, text="ODLOMIT", command=self.odlom)
        self.button.pack()
        self.vystup = tk.Text(self, height=5, width=100)
        self.vystup.pack()
        self.button = tk.Button(self, text="KONEC", command=self.destroy)
        self.button.pack()
        

    def odlom(self):
        nahrada = self.nahradnik.get()
        vstup = self.entry.get('1.0','end-1c')
        odlomeno = vstup.replace("\n", nahrada)
        self.vystup.delete('1.0','end-1c')
        self.vystup.insert('1.0', odlomeno)

app = Odlamovac()
app.mainloop()
