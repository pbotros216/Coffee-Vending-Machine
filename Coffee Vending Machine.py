"""
Peter Botros
september 20 2024
"""
# This program stimulates a coffee vending machine. User will be able to customize their coffee selction and price will depend on these customizations.

# Step 1: Define prices for coffee types, cup sizes, and strength multipliers
# Pseudocode:
#   Create a dictionary for coffee types with prices.
#   Create a dictionary for cup sizes with prices.
#   Create a dictionary for coffee strength multipliers.

# prices for coffee types
coffee_prices={
    "espresso": 3.0,
    "black": 1.5,
    "latte":2.0,
    "cappucino": 2.5
}
# Price for cup sizes
cup_sizes={
    "small":1.0,
    "medium":1.5,
    "large":2.0,
}
# Strength multpilier
strength_multiplier={
    "weak":1.0,
    "regular":1.5,
    "stronger":2.0,
}
# Step 2: Create a function to select coffee type
# Pseudocode:
#   Display the available coffee types and their prices.
#   Ask the user to input their choice.
#   If the choice is valid, return the corresponding price.
#   If the choice is invalid, display an error message and default to "black coffee".


def select_coffee_type():
    """
    Allows user to select coffee type and determines price of coffee
    """
    print("select coffee type:")
    for coffee in coffee_prices:
        print (f"- {coffee.capitalize()}: ${coffee_prices[coffee]}")
    coffee_choice= input("enter coffee choice:").lower()
    if coffee_choice in coffee_prices:
        return coffee_prices[coffee_choice]
    else:
        print ("invalid selection! defaulting to 'black'.")
        return coffee_prices["black"]

# Step 3: Create a function to select cup size
# Pseudocode:
#   Display the available cup sizes and their prices.
#   Ask the user to input their choice.
#   If the choice is valid, return the corresponding price.
#   If the choice is invalid, display an error message and default to "small".

def select_cup_sizes():
    """
    Allows user to select cup size and returns price for that size.
    """
    print (" Select coffee size.")
    for size in cup_sizes:
        print(f"- {size.capitalize()}: ${cup_sizes[size]}")

    size_choice=input(" Enter your cup size(small,medium,large):").lower()

    if size_choice in cup_sizes:
        return cup_sizes[size_choice]

    else:
        print ("Invalid choice defaulting to 'medium'.")
        return cup_sizes["small"]
def select_coffee_strength():
    """
    Allows the user to select the strength of their coffee and returns the strength multiplier.
    """
    print("Select coffee strength:")
    for strength in strength_multiplier:
        print(f"- {strength.capitalize()}")

    strength_choice = input("Enter coffee strength (weak, regular, strong): ").lower()

    if strength_choice in strength_multiplier:
        return strength_multiplier[strength_choice]
    else:
        print("Invalid strength! Defaulting to 'regular'.")
        return strength_multiplier["regular"]

def calculate_total_price(coffee_price, size_price, strength_mult):
    """
    Calculates the total price based on coffee type, size, and strength.
    """
    return (coffee_price + size_price) * strength_mult

# Main function to run the coffee vending machine simulation
if __name__ == "__main__":
    print("Welcome to the Coffee Vending Machine!\n")

    # User selects coffee type, cup size, and strength
    coffee_price = select_coffee_type()
    size_price = select_cup_sizes()
    strength_mult = select_coffee_strength()

    # Calculate total price
    total_price = calculate_total_price(coffee_price, size_price, strength_mult)

    # Display the final price
    print(f"-Your total price is: ${total_price:2f}. Enjoy your coffee!")