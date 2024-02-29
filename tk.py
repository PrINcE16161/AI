import tkinter as tk
from tkinter.ttk import Label, Style

import pyttsx3


class App:
    def __init__(self, master) -> None:
        self.master = master

        self.style = Style(self.master)

        self.style.configure("My.TLabel", font=('Arial', 100))

        Label(
            self.master,
            text="🤖",
            style="My.TLabel", foreground="black"
        ).pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Voice Assistant")
    app = App(root)
    root.mainloop()