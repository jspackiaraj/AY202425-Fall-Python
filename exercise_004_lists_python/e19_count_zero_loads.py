def count_zero_loads(loads: list) -> int:
    """
    This function counts the number of zero loads in a list.
    
    :param loads: A list of load values.
    :return: The number of zero loads in the list.
    """
    return loads.count(0)

if __name__ == "__main__":
    # Example list of loads
    loads = [10, 0, 20, 0, 30]
    zero_count = count_zero_loads(loads)
    print(f"Number of zero loads: {zero_count}")