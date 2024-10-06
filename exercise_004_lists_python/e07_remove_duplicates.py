def remove_duplicates(loads: list) -> list:
    """
    This function removes duplicate values from a list of loads.
    
    :param loads: A list of load values.
    :return: A list of unique load values.
    """
    return list(set(loads))

if __name__ == "__main__":
    # Example list of loads with duplicates
    loads = [10, 15, 10, 20, 15]
    unique_loads = remove_duplicates(loads)
    print(f"Unique load cases are: {unique_loads}")