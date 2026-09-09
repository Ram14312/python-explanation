from .exceptions import CalculationError


def calculate_total(marks):
    if not marks:
        raise CalculationError("Cannot calculate a total without marks.")
    return sum(marks)


def calculate_percentage(total, subject_count):
    if subject_count <= 0:
        raise CalculationError("Subject count must be greater than zero.")
    return (total / (subject_count * 100)) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def calculate_status(marks):
    return "Pass" if all(mark >= 35 for mark in marks) else "Fail"


def create_result(student):
    marks = student["marks"]
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))

    return {
        "name": student["name"],
        "total": total,
        "percentage": percentage,
        "grade": calculate_grade(percentage),
        "status": calculate_status(marks),
    }
