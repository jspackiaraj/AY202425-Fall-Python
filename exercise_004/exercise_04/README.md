Here's a `README.md` file that explains the `pH_calculator.py` program in detail:

---

# pH Calculator

## Question

Write a program to calculate the pH of a solution given its hydrogen ion concentration. The program should store a list of common substances and their corresponding pH values (e.g., Lemon juice = 2.0, Water = 7.0, Bleach = 12.6). It should then classify the solution as acidic, neutral, or basic based on the calculated pH.

## Overview

The `pH_calculator.py` script calculates the pH of a solution based on the provided hydrogen ion concentration. It also classifies the solution as acidic, neutral, or basic. Additionally, the script includes a reference list of common substances and their typical pH values.

## How It Works

1. **Calculate pH**:
   - The pH of a solution is calculated using the formula:
     \[
     \text{pH} = -\log_{10}[\text{H}^+]
     \]
   - The script uses the `math.log10()` function to compute the logarithm base 10 of the hydrogen ion concentration.

2. **Classify Solution**:
   - Based on the calculated pH value:
     - pH < 7: The solution is classified as **acidic**.
     - pH = 7: The solution is classified as **neutral**.
     - pH > 7: The solution is classified as **basic**.

3. **Common Substances**:
   - The script includes a list of common substances with their pH values for reference:
     - Lemon juice = 2.0
     - Water = 7.0
     - Bleach = 12.6

## How to Use

1. **Save the Script**:
   - Save the provided Python code as `pH_calculator.py`.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `pH_calculator.py` is saved.
   - Run the script with the command:
     ```
     python pH_calculator.py
     ```

3. **Provide Input**:
   - When prompted, enter the hydrogen ion concentration in mol/L.

4. **View Results**:
   - The script will display the calculated pH value and classify the solution as acidic, neutral, or basic.

## Example

**Input**:
```
Enter the hydrogen ion concentration (in mol/L): 1e-5
```

**Output**:
```
Common substances and their pH values:
Lemon juice = 2.0
Water = 7.0
Bleach = 12.6
The pH of the solution is: 5.00
The solution is classified as: acidic
```

## Script Details

- **`calculate_ph(hydrogen_ion_concentration)`**:
  - Takes hydrogen ion concentration as input and returns the pH value.
  
- **`classify_ph(pH)`**:
  - Takes the pH value as input and classifies it as acidic, neutral, or basic.

- **`main()`**:
  - Displays common substances with their pH values.
  - Prompts the user for input and displays the calculated pH and classification.

## Error Handling

- The script checks for valid hydrogen ion concentration inputs (greater than 0).
- Handles invalid inputs and displays appropriate error messages.
