def reverse_survey_points(points: list) -> list:
    """
    This function reverses the order of survey points in the list.
    
    :param points: A list of survey points.
    :return: The reversed list of points.
    """
    return points[::-1]

if __name__ == "__main__":
    # Example list of survey points
    points = [[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]
    reversed_points = reverse_survey_points(points)
    print(f"The reversed order of survey points is: {reversed_points}")