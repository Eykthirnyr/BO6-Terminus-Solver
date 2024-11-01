import sys
import tkinter as tk
from tkinter import messagebox

# Dependency Check
try:
    from PIL import Image, ImageTk
except ImportError:
    import subprocess
    def install_pillow():
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        messagebox.showinfo("Dependency Installed", "Pillow has been installed. Please restart the application.")
        sys.exit()

    root = tk.Tk()
    root.withdraw()  # Hide the root window
    response = messagebox.askyesno("Missing Dependency", "The Pillow library is required but not installed.\nDo you want to install it now?")
    if response:
        install_pillow()
    else:
        messagebox.showwarning("Dependency Missing", "Cannot proceed without installing the required dependency.")
        sys.exit()

class QuestSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Black Ops 6: Zombies - Terminus - Main Quest SOLVER")
        self.configure(bg='black')

        self.symbols = ['0', '10', '11', '20', '21', '22']
        self.selected_values = {'X': None, 'Y': None, 'Z': None}
        self.images = {}
        self.selected_buttons = {'X': None, 'Y': None, 'Z': None}

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self, text="Black Ops 6: Zombies - Terminus - Main Quest SOLVER",
            fg='#FFD700', bg='black', font=("Segoe UI", 18, "bold")
        )
        title_label.pack(pady=20)

        self.create_symbol_selector('X')
        self.create_symbol_selector('Y')
        self.create_symbol_selector('Z')

        self.create_results_table()

    def create_symbol_selector(self, variable):
        frame = tk.Frame(self, bg='black')
        frame.pack(pady=10)

        label = tk.Label(
            frame, text=f"Select Symbol for {variable}:",
            fg='#00FFFF', bg='black', font=("Segoe UI", 14)
        )
        label.pack()

        symbols_frame = tk.Frame(frame, bg='black')
        symbols_frame.pack()

        for symbol in self.symbols:
            try:
                img = Image.open(f"{symbol}.png").resize((80, 80), Image.LANCZOS)
            except FileNotFoundError:
                messagebox.showerror("Image Not Found", f"Image file '{symbol}.png' not found.")
                sys.exit()
            photo = ImageTk.PhotoImage(img)
            self.images[f"{variable}_{symbol}"] = photo  # Keep a reference

            btn = tk.Button(
                symbols_frame, image=photo, bg='black',
                borderwidth=2, relief='flat'
            )
            btn.config(
                command=lambda s=symbol, v=variable, b=btn: self.select_symbol(v, int(s), b)
            )
            btn.pack(side='left', padx=5, pady=5)

    def select_symbol(self, variable, value, btn):
        self.selected_values[variable] = value

        # Deselect previous button
        if self.selected_buttons[variable]:
            self.selected_buttons[variable].config(borderwidth=2, relief='flat', bg='black')

        # Highlight current button
        btn.config(borderwidth=2, relief='solid', bg='green')

        self.selected_buttons[variable] = btn

        self.compute_results()

    def create_results_table(self):
        frame = tk.Frame(self, bg='black')
        frame.pack(pady=20)

        self.results_label = tk.Label(
            frame, text="Code", fg='white', bg='black', font=("Segoe UI", 16)
        )
        self.results_label.pack()

        self.results_values = tk.Label(
            frame, text="-   -   -", fg='white', bg='black', font=("Segoe UI", 24)
        )
        self.results_values.pack()

    def compute_results(self):
        X = self.selected_values['X']
        Y = self.selected_values['Y']
        Z = self.selected_values['Z']

        if X is not None and Y is not None and Z is not None:
            line1 = abs(2 * X + 11)
            line2 = abs((2 * Z + Y) - 5)
            line3 = abs((Y + Z) - X)

            self.results_values.config(text=f"{line1}   {line2}   {line3}")
        else:
            self.results_values.config(text="-   -   -")

if __name__ == "__main__":
    app = QuestSolver()
    app.mainloop()
