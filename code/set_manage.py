def set_diff():
    """
    This function calculates the difference between two sets and returns the result.
    """
    set1 = {0, 1, 2, 3, 4, 5, 6,7,8,9}
    set2 = set(input("Enter a set: "))
    print(set2-set1)    
    # Calculate the difference
    diff = set1.difference(set2)
    print(diff)
    
    return diff

    
if __name__ == "__main__":
    # Example usage
    result = set_diff()
    print("Set difference:", result)