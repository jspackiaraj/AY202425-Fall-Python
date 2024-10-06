def extract_even_indexed_points(points: list) -> list:
    """
    This function extracts survey points located at even-indexed positions in the list.
    
    :param points: A list of survey points.
    :return: A list of points located at even indices.
    """
    return points[::2]

if __name__ == "__main__":
    # Example list of survey points
    points = [[0, 0], [50, 5], [100, 10], [150, 8], [200, 3]]
    even_indexed_points = extract_even_indexed_points(points)
    print(f"Even-indexed points: {even_indexed_points}")