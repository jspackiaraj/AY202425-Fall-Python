def compare_loads(before: list, after: list) -> list:
    """
    This function compares two lists of loads and returns the difference between the corresponding elements.
    
    :param before: A list of loads before an event.
    :param after: A list of loads after an event.
    :return: A list of differences between the loads at each point.
    """
    return [after_load - before_load for before_load, after_load in zip(before, after)]

if __name__ == "__main__":
    # Example loads before and after the event
    before = [10, 15, 20, 25]
    after = [12, 14, 18, 30]
    load_differences = compare_loads(before, after)
    print(f"Load differences: {load_differences}")