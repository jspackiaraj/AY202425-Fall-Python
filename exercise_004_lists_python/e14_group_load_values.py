def group_load_values(loads: list) -> tuple:
    """
    This function groups load values into point loads (below 10 kN) and distributed loads (10 kN or above).
    
    :param loads: A list of load values.
    :return: A tuple containing two lists: one for point loads and one for distributed loads.
    """
    point_loads = [load for load in loads if load < 10]
    super_point_loads = [load for load in loads if load >= 10]
    return point_loads, super_point_loads

if __name__ == "__main__":
    # Example list of load values
    loads = [5, 12, 8, 15, 6]
    point_loads, super_point_loads = group_load_values(loads)
    print(f"Point loads: {point_loads}, Super Point loads: {super_point_loads}")