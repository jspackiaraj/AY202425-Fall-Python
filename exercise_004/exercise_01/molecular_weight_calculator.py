# Molecular Weight Calculator
atomic_weights = {
    'H': 1.008,
    'O': 15.999,
    'C': 12.011
}

def calculate_molecular_weight(formula):
    total_weight = 0
    i = 0
    while i < len(formula):
        element = formula[i]
        i += 1
        if i < len(formula) and formula[i].isdigit():
            count = int(formula[i])
            i += 1
        else:
            count = 1
        total_weight += atomic_weights[element] * count
    return total_weight

formula = input("Enter the molecular formula: ")
molecular_weight = calculate_molecular_weight(formula)
print("Molecular Weight of", formula, "=", molecular_weight)
