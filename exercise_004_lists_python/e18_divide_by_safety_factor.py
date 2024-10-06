def divide_loads_by_safety_factor(loads: list, safety_factor: float) -> list:
    """
    This function divides each load value by a given safety factor.
    
    :param loads: A list of load values.
    :param safety_factor: The safety factor by which to divide each load.
    :return: A list of loads divided by the safety factor.
    """
    return [load / safety_factor for load in loads]

if __name__ == "__main__":
    # Example list of loads and safety factor
    loads = [15, 30, 45, 60]
    safety_factor = 1.5
    safe_loads = divide_loads_by_safety_factor(loads, safety_factor)
    print(f"Loads divided by safety factor: {safe_loads}")