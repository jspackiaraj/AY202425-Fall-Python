def find_max_deflection(deflections: list) -> float:
    """
    This function returns the maximum deflection value from a list of deflections.
    
    :param deflections: A list of deflection values (in millimeters).
    :return: The maximum deflection value.
    """
    return max(deflections)

if __name__ == "__main__":
    # Example list of deflection values in mm
    deflections = [0, -10, -20, -25, -15, 0]
    max_deflection = find_max_deflection(deflections)
    print(f"The maximum deflection is: {max_deflection} mm")