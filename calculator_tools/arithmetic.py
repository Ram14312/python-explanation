from  .exceptions import InvalidOperationError


def _validate_number(value, name):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise InvalidOperationError(f"{name} must be a number.")


def add(a,b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a+b

def subtract(a,b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a-b

def multiply(a,b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a*b

def divide(a,b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b==0:
        raise InvalidOperationError("Cannot divide by zero.")
    return a/b

def percentage(value, total):
    _validate_number(value, "value")
    _validate_number(total, "total")
    if total == 0:
        raise InvalidOperationError("The total cannot be zero when calculating a percentage.")
    return (value / total) * 100

