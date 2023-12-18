import tkinter as tk
from tkinter import messagebox

fruit_prices = {"apple": 0.54, "pear": 0.63, "grape": 0.95, "banana":1.14, "lemon": 1.03}

with open("stored_cost.txt", "r") as stored_file:
        content = stored_file.read
def calculate_cost():
    selected_fruit = fruit_var.get()
    weight = weight_entry.get()
    try:
        weight = float(weight)
        if selected_fruit in fruit_prices:
            cost = fruit_prices[selected_fruit] * weight
            messagebox.showinfo("Price:",f"Total for {weight} kg of {selected_fruit}: ${cost:.2f}")
        else:
            messagebox.showwarning("Invalid Fruit, enter code again")
    except ValueError:
        messagebox.showerror("Invalid Weight")

    stored_view.config(text=f"Summary: {selected_fruit}, Cost: {cost:.2f}")

    with open("stored_cost.txt", "a") as stored_file:
        stored_file.write(f"{selected_fruit}, {cost}")


window =tk.Tk()
window.title("Fruit cost calculator")

fruit_label = tk.Label(window, text="Select Fruit")
fruit_label.pack()

fruit_var = tk.StringVar(window)
fruit_var.set(list(fruit_prices.keys())[0])
fruit_menu = tk.OptionMenu(window, fruit_var,*fruit_prices.keys())
fruit_menu.pack()

weight_label = tk.Label(window, text="Enter weight (kg): ")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

calculate_button = tk.Button(window, text="Calculate cost", command=calculate_cost)
calculate_button.pack()

stored_view = tk.Label(window, text=content)
stored_view.pack()

window.mainloop()