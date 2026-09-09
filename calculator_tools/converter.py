from .exceptions import InvalidOperationError


def _validate_number(value, name="value"):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise InvalidOperationError(f"{name} must be a number.")


def celsius_to_fahrenheit(celsius):
    _validate_number(celsius, "celsius")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    _validate_number(fahrenheit, "fahrenheit")
    return (fahrenheit - 32) * 5 / 9


def convert_length(value, from_unit, to_unit):
    """Convert a length between metres, kilometres, centimetres, and miles."""
    _validate_number(value)
    units_in_metres = {"m": 1, "km": 1000, "cm": 0.01, "mi": 1609.344}

    if from_unit not in units_in_metres or to_unit not in units_in_metres:
        raise InvalidOperationError(
            "Unsupported length unit. Use m, km, cm, or mi."
        )

    return value * units_in_metres[from_unit] / units_in_metres[to_unit]
