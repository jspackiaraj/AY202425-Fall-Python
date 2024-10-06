def merge_survey_data(data1: list, data2: list) -> list:
    """
    This function merges two lists of survey data, removing duplicates.
    
    :param data1: First list of survey data.
    :param data2: Second list of survey data.
    :return: A merged list containing only unique survey points.
    """
    return list(set(data1 + data2))

if __name__ == "__main__":
    # Example survey data sets
    data1 = [10, 20, 30, 40]
    data2 = [30, 40, 50, 60]
    merged_data = merge_survey_data(data1, data2)
    print(f"Merged data: {merged_data}")