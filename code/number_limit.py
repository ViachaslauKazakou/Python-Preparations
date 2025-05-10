# The map function applies a given function to each item of an iterable (like a list) and returns a map object (an iterator).
# Example: map(str.upper, ['a', 'b', 'c']) returns an iterator producing 'A', 'B', 'C'.
# In this code, map applies the lambda to each input value until "0" is entered.
# 
# The iter(function, sentinel) form repeatedly calls the function (here, input) and yields its result,
# stopping when the result equals the sentinel value ("0").

# To return the value itself (if it matches the condition), use a conditional expression in the lambda.
b = [x for x in (list(
    map(
        lambda a: int(a) if 39 < int(a) < 51 else None,
        iter(input, "0")
    )
)) if x is not None]
print(b)
4