from .exceptions import InvalidOperationError

def _validate_values(values):
    if not isinstance(values, (list, tuple)):
        raise InvalidOperationError("Values must be provided as a list or tuple.")
    if not values:
        raise InvalidOperationError("Values cannot be empty.")
    if any(not isinstance(value, (int, float)) or isinstance(value, bool) for value in values):
        raise InvalidOperationError("Every value must be a number.")


def mean(values):
    _validate_values(values)
    n = len(values)

    temp =0

    for i in values:
        temp = temp+i

    return temp/n

def median(values):
    _validate_values(values)
    sorted_values = sorted(values)
    n = len(sorted_values)
    middle = n // 2

    if n%2 == 0:
        return (sorted_values[middle - 1] + sorted_values[middle]) / 2

    return sorted_values[middle]



