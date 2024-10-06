def calculate_cumulative_load(loads: list) -> list:
    """
    This function calculates the cumulative load at each point along a beam.
    
    :param loads: A list of load values.
    :return: A list representing the cumulative load at each point.
    """
    cumulative = []
    total = 0
    for load in loads:
        total += load
        cumulative.append(total)
    return cumulative

if __name__ == "__main__":
    # Example list of loads
    loads = [10, 15, 10, 5]
    cumulative_load = calculate_cumulative_load(loads)
    print(f"Cumulative load: {cumulative_load}")