fruit = {"apple": 0.54, "pear": 0.63, "grape": 0.95, "banana": 1.14, "lemon": 1.03}
code = [1, 2, 3, 4, 5]

code_fruit_mapping = dict(zip(code, fruit.keys()))

total_cost = 0

while True:
    code_choice = int(input("Choose a fruit by entering its code (or enter 0 to finish): "))
    
    if code_choice == 0:
        break 

    if code_choice not in code_fruit_mapping:
        print("Invalid code. Please choose a valid code.")
        continue

    fruit_name = code_fruit_mapping[code_choice]
    weight = float(input(f"Enter weight for {fruit_name} in kilograms: "))

    # Calculate cost for the selected fruit and add it to the total cost
    cost = fruit[fruit_name] * weight
    total_cost += cost

# Print the total cost
print(f"Total cost for the selected fruits: ${total_cost:.2f}")
