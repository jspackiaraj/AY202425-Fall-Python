def sort_load_values(loads: list) -> list:
    """
    This function sorts a list of load values in ascending order.
    
    :param loads: A list of load values.
    :return: A sorted list of load values.
    """
    return sorted(loads)

if __name__ == "__main__":
    # Example list of load values
    loads = [20, 5, 15, 10, 25]
    sorted_loads = sort_load_values(loads)
    print(f"Sorted loads: {sorted_loads}")