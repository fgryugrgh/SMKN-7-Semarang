import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Numpad")

# Define button labels
buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "C", "0", "⏎"
]

# Create a function to handle button clicks
def on_button_click(value):
    print(f"Button {value} clicked")

# Create and place buttons
for index, label in enumerate(buttons):
    row = index // 3  # Determine row
    col = index % 3    # Determine column
    btn = tk.Button(root, text=label, width=5, height=2,
                    command=lambda v=label: on_button_click(v))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
