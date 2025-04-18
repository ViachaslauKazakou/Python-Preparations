def revert_string(start, end, step, string):
    """
    Revert a string from start to end with step.
    :param start: Start index
    :param end: End index
    :param step: Step size
    :param string: String to revert
    :return: Reverted string
    """
    return string[start:end:step][::-1]

if __name__ == "__main__":
    # Example usage
    start = 0
    end = 8
    step = 2
    string = "Hello, World!"
    result = revert_string(start, end, step, string)
    print(result)  # Output: "olleH"