def replace_outliers(data: list) -> list:
    """
    This function replaces outliers (values greater than 100) in the list with the average of the remaining values.
    
    :param data: A list of soil test data.
    :return: A list where outliers are replaced with the average value.
    """
    # Filter out values greater than 100 to calculate the average
    non_outliers = [x for x in data if x <= 100]
    avg_value = sum(non_outliers) / len(non_outliers) if non_outliers else 0
    
    # Replace values greater than 100 with the average
    return [x if x <= 100 else avg_value for x in data]

if __name__ == "__main__":
    # Example soil test data
    data = [80, 105, 90, 120, 95]
    updated_data = replace_outliers(data)
    print(f"Data after replacing outliers: {updated_data}")