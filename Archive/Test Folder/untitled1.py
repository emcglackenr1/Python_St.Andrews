def refine_data(data, expected_format, admissible_values=None, admissible_range=None):
    """
    Refine the data by checking format, removing duplicates, and applying further refinements.

    Args:
        data (list): The list of data to be refined.
        expected_format (type or tuple of types): The expected format(s) of the data (e.g., int, str).
        admissible_values (list, optional): A list of admissible values.
        admissible_range (tuple, optional): A tuple representing the admissible range (e.g., (min_val, max_val)).

    Returns:
        list: The refined data.
    """
    refined_data = []

    # Step 1: Check format and remove duplicates
    for item in data:
        if isinstance(item, expected_format) and item not in refined_data:
            refined_data.append(item)

    # Step 2: Further refinement based on admissible values or range
    if admissible_values:
        refined_data = [item for item in refined_data if item in admissible_values]
    elif admissible_range:
        min_val, max_val = admissible_range
        refined_data = [item for item in refined_data if min_val <= item <= max_val]

    return refined_data
    