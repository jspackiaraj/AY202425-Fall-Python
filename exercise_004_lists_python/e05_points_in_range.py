def find_points_in_range(points: list, start: float, end: float) -> list:
    """
    This function finds all points that lie within a given range.
    
    :param points: A list of survey points (represented as [distance, elevation]).
    :param start: The start of the range.
    :param end: The end of the range.
    :return: A list of points within the specified range.
    """
    return [point for point in points if start <= point[0] <= end]

if __name__ == "__main__":
    # Example list of survey points
    points = [[0, 0], [50, 5], [100, 10], [150, 8], [200, 3], [250, 5], [300, 0]]
    # Range from 100 to 200 meters
    filtered_points = find_points_in_range(points, 100, 200)
    print(f"Points within the range are: {filtered_points}")