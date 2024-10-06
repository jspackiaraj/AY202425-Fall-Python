def insert_missing_data(data: list, positions: list) -> list:
    """
    This function inserts `None` at the specified positions in the list.
    
    :param data: A list of data points.
    :param positions: A list of positions where `None` should be inserted.
    :return: The updated list with `None` inserted at the specified positions.
    """
    for pos in positions:
        data.insert(pos, None)
    return data

if __name__ == "__main__":
    # Example survey data and missing positions
    data = [0, 5, 10, 15, 20]
    positions = [1, 3]
    updated_data = insert_missing_data(data, positions)
    print(f"Data after inserting missing values: {updated_data}")