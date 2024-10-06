def calculate_total_load(loads: list) -> float:
    """
    This function calculates the total load from a list of loads.
    
    :param loads: A list of load values in kilonewtons (kN).
    :return: The total load in kilonewtons (kN).
    """
    return sum(loads)

if __name__ == "__main__":
    # Example loads in kN
    loads = [10, 15, 10, 5]
    total_load = calculate_total_load(loads)
    print(f"The total load on the beam is: {total_load} kN")