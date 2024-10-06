   
def find_common_loads(loads1: list, loads2: list) -> list:
    """
    This function finds the common load values between two lists.
    
    :param loads1: First list of load values.
    :param loads2: Second list of load values.
    :return: A list of common load values.
    """
    return list(set(loads1) & set(loads2))

if __name__ == "__main__":
    # Example load values in two lists
    loads1 = [10, 20, 30, 40]
    loads2 = [30, 40, 50, 60]
    common_loads = find_common_loads(loads1, loads2)
    print(f"Common loads: {common_loads}")