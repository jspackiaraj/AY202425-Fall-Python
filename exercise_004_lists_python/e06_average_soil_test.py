def calculate_average_soil_test(results: list) -> float:
    """
    This function calculates the average of a list of soil test results.
    
    :param results: A list of soil test values.
    :return: The average soil test result as a float.
    """
    return sum(results) / len(results) if results else 0.0

if __name__ == "__main__":
    # Example soil test results
    results = [80, 95, 88, 92, 85]
    average_result = calculate_average_soil_test(results)
    print(f"The average soil test result is: {average_result}")