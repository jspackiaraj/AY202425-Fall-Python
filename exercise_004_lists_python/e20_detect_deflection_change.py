def detect_deflection_change(deflections: list, threshold: float) -> list:
    """
    This function detects where significant changes in deflection occur.
    
    :param deflections: A list of deflection values (in millimeters).
    :param threshold: The threshold for detecting significant changes in deflection.
    :return: A list of indices where the change in deflection exceeds the threshold.
    """
    significant_changes = []
    for i in range(1, len(deflections)):
        if abs(deflections[i] - deflections[i - 1]) > threshold:
            significant_changes.append(i)
    return significant_changes

if __name__ == "__main__":
    # Example deflection values and threshold
    deflections = [0, -5, -7, -15, -5, 0]
    threshold = 5
    changes = detect_deflection_change(deflections, threshold)
    print(f"Indices with significant deflection changes: {changes}")