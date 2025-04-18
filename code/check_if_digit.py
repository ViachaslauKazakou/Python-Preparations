def is_digit(val: str) -> bool:
    ''' input - string
        output - boolean'''
    try:
        float(val)
        return True
    except ValueError:
        return False

import re

def is_digit2(val: str) -> bool:
    ''' input - string
        output - boolean'''
    # Regular expression to match a valid floating-point number
    pattern = re.compile(r'^-?\d+(\.\d+)?$')
    return bool(pattern.match(val))

def is_digit3(val: str) -> bool:
    ''' input - string
        output - boolean'''
    if not val:
        return False

    # Check for optional leading minus sign
    if val[0] == '-':
        val = val[1:]

    # Split the string by the decimal point
    parts = val.split('.')

    # There should be at most one decimal point
    if len(parts) > 2:
        return False

    # Check if all parts are digits
    if not all(part.isdigit() for part in parts):
        return False

    # Ensure at least one part has digits
    # if not any(part for part in parts):
    #     return False

    return True

if __name__ == '__main__':
    for val in ['1', 'a', '0', '10', '10.0', '10.0.0', '1.0', "-100", "-100.r0", "-100.0.0"]:
        # print(f"Check {val} as digit: {is_digit2(val)}")
        print(f"Check {val} as digit: {is_digit3(val)}")
