import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minesweeper")

# default values
rows = 10
cols = 10
mines = 10

# Create the grid
grid_frame = tk.Frame(root)
grid_frame.pack()

def set_custom_size(row, col, mine):
    global rows, cols, mines
    rows = row
    cols = col
    mines = mine
    restart_game()

def restart_game():
    for widget in grid_frame.winfo_children():
        widget.destroy()
    create_grid()

def create_grid():
    for row in range(rows):
        for col in range(cols):
            button = ttk.Button(grid_frame, text=" ", width=3, command=lambda row=row, col=col: on_button_click(row, col))
            button.grid(row=row, column=col, sticky="nsew")

def on_button_click(row, col):
    # You can add game logic here if needed
    pass

# Create the menu
menu_bar = tk.Menu(root)
size_menu = tk.Menu(menu_bar, tearoff=0)
size_menu.add_command(label="Easy (9x9 board with 10 mines)", command=lambda: set_custom_size(9, 9, 10))
size_menu.add_command(label="Medium (16x16 board with 40 mines)", command=lambda: set_custom_size(16, 16, 40))
size_menu.add_command(label="Expert (16x30 board with 99 mines)", command=lambda: set_custom_size(16, 30, 99))
size_menu.add_command(label="Custom", command=set_custom_size)

menu_bar.add_cascade(label="Size", menu=size_menu)

# Add a "Rules" menu option
def show_rules():
    rules_window = tk.Toplevel(root)
    rules_window.title("Minesweeper Rules")
    rules_text = "Enter rules here."
    rules_label = tk.Label(rules_window, text=rules_text, wraplength=400, justify="left")
    rules_label.pack()

menu_bar.add_command(label="Rules", command=show_rules)

root.config(menu=menu_bar)

# Create custom size input fields
row_label = tk.Label(root, text="Rows:")
row_label.pack()
row_entry = tk.Entry(root)
row_entry.insert(0,"0")
row_entry.pack()

col_label = tk.Label(root, text="Columns:")
col_label.pack()
col_entry = tk.Entry(root)
col_entry.insert(0, "0")
col_entry.pack()

mine_label = tk.Label(root, text="Mines:")
mine_label.pack()
mine_entry = tk.Entry(root)
mine_entry.insert(0, "0")
mine_entry.pack()

custom_size_button = tk.Button(
    root,
    text="Set Custom Size",
    command=lambda: set_custom_size(int(row_entry.get()), int(col_entry.get()), int(mine_entry.get()))
)
custom_size_button.pack()

create_grid()

root.mainloop()






