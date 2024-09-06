import math

def calculate_ph(hydrogen_ion_concentration):
    """Calculate the pH of a solution given the hydrogen ion concentration."""
    try:
        pH = -math.log10(hydrogen_ion_concentration)
        return pH
    except ValueError:
        print("Hydrogen ion concentration must be greater than 0.")
        return None

def classify_ph(pH):
    """Classify the pH value as acidic, neutral, or basic."""
    if pH < 7:
        return "acidic"
    elif pH == 7:
        return "neutral"
    else:
        return "basic"

def main():
    # List of common substances and their pH values
    substances = {
        "Lemon juice": 2.0,
        "Water": 7.0,
        "Bleach": 12.6
    }

    # Print list of common substances
    print("Common substances and their pH values:")
    for substance, pH in substances.items():
        print(f"{substance} = {pH}")

    # Input hydrogen ion concentration
    try:
        concentration = float(input("Enter the hydrogen ion concentration (in mol/L): "))
        if concentration <= 0:
            raise ValueError("Hydrogen ion concentration must be greater than 0.")

        # Calculate pH and classify it
        pH = calculate_ph(concentration)
        if pH is not None:
            print(f"The pH of the solution is: {pH:.2f}")
            print(f"The solution is classified as: {classify_ph(pH)}")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")

if __name__ == "__main__":
    main()
