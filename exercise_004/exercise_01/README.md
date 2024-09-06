# Molecular Weight Calculator

## Question
Write a program that calculates the molecular weight of a compound given its molecular formula. Use a dictionary to store the atomic weights of elements (e.g., H = 1.008, O = 15.999, etc.). The program should take a molecular formula as input and calculate the total molecular weight. Test your program with water (H2O) and carbon dioxide (CO2).

## Concept
Molecular weight calculation is essential in chemistry for determining the mass of a compound based on its molecular formula. The molecular weight is the sum of the atomic weights of all atoms in the molecule.

## Methods Used
- **Dictionary**: To map element symbols to their atomic weights.
- **Iteration**: To traverse the molecular formula and sum up the atomic weights based on the number of atoms of each element.

## Description
The program takes a molecular formula as input and calculates its molecular weight by summing the atomic weights of the constituent elements. The dictionary stores atomic weights, which are used to look up each element's weight during the calculation.

## Other Applications
This method can be extended to calculate the molar mass of complex compounds, handle isotopes, or even be adapted for use in stoichiometry calculations in chemical reactions.
