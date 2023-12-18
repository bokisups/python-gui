import tkinter as tk
from tkinter import messagebox

fruit_prices = {"apple": 0.54, "pear": 0.63, "grape": 0.95, "banana": 1.14, "lemon": 1.03}

def calculate_cost():
    selected_fruit = fruit_var.get()
    weight = weight_entry.get()

    try:
        weight = float(weight)
        if selected_fruit in fruit_prices:
            cost = fruit_prices[selected_fruit] * weight
            messagebox.showinfo("Total Cost", f"Total cost for {weight} kg of {selected_fruit}: ${cost:.2f}")
        else:
            messagebox.showwarning("Invalid Fruit", "Please select a valid fruit.")
    except ValueError:
        messagebox.showerror("Invalid Weight", "Please enter a valid weight (numeric value).")

# Create the main window
window = tk.Tk()
window.title("Fruit Cost Calculator")

# Create a label for fruit selection
fruit_label = tk.Label(window, text="Select Fruit:")
fruit_label.pack()

# Create a dropdown menu for fruit selection
fruit_var = tk.StringVar(window)
fruit_var.set(list(fruit_prices.keys())[0])  # Set the default value
fruit_menu = tk.OptionMenu(window, fruit_var, *fruit_prices.keys())
fruit_menu.pack()

# Create a label for weight input
weight_label = tk.Label(window, text="Enter Weight (kg):")
weight_label.pack()

# Create an entry widget for weight input
weight_entry = tk.Entry(window)
weight_entry.pack()

# Create a button to calculate the cost
calculate_button = tk.Button(window, text="Calculate Cost", command=calculate_cost)
calculate_button.pack()

# Start the Tkinter event loop
window.mainloop()
