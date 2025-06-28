def grade_filter():
    """
    Filters the grades based on a given threshold.

    Parameters:
    grade (Any): grade (integers or floats or 'stop').
    threshold (list): The threshold value.

    Returns:
    list: A list of grades that are above the threshold.
    """
    threshold = [2, 3, 4, 5]
    grade_list = []
    while True:
        try:
            grade = float(input("Enter a grade (or type 'stop' to finish): "))
            if grade in threshold:
                grade_list.append(int(grade))
        except ValueError:
            break
    return grade_list


if __name__ == "__main__":
    grades = grade_filter()
    print("Filtered grades:", grades)
    
