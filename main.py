from calculator_tools import (
    InvalidOperationError,
    add,
    celsius_to_fahrenheit,
    convert_length,
    divide,
    mean,
    median,
    multiply,
    percentage,
    subtract,
)

print("Arithmetic:")
print("4 + 5 =", add(4, 5))
print("5 - 4 =", subtract(5, 4))
print("2 * 3 =", multiply(2, 3))
print("4 / 2 =", divide(4, 2))
print("25 is", percentage(25, 200), "% of 200")

print("\nStatistics:")
print("Mean =", mean([10, 20, 30]))
print("Median =", median([9, 1, 5, 3]))

print("\nConversions:")
print("25°C =", celsius_to_fahrenheit(25), "°F")
print("2.5 km =", convert_length(2.5, "km", "m"), "m")

print("\nHandled errors:")
for action in (lambda: divide(10, 0), lambda: mean([]), lambda: convert_length(1, "m", "kg")):
    try:
        action()
    except InvalidOperationError as error:
        print(error)
