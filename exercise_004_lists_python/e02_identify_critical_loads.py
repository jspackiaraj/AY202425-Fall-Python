def identify_critical_loads(loads: list) -> list:
    """
    This function identifies the critical loads (greater than 50 kN) from a list of loads.
    
    :param loads: A list of load values in kilonewtons (kN).
    :return: A list of critical loads greater than 50 kN.
    """
    return [load for load in loads if load > 50]

if __name__ == "__main__":
    # Example list of loads
    loads = [20, 55, 30, 60, 10]
    critical_loads = identify_critical_loads(loads)
    print(f"Critical loads are: {critical_loads}")