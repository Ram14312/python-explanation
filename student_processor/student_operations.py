from .exceptions import InvalidMarksError, MissingStudentInfoError


SUBJECT_COUNT = 5


def create_student(name, marks):
    """Validate student details and return one student dictionary."""
    if not isinstance(name, str) or not name.strip():
        raise MissingStudentInfoError("Student name is required.")

    if not isinstance(marks, (list, tuple)) or len(marks) != SUBJECT_COUNT:
        raise InvalidMarksError(f"Enter marks for exactly {SUBJECT_COUNT} subjects.")

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise InvalidMarksError("Every mark must be a number.")
        if not 0 <= mark <= 100:
            raise InvalidMarksError("Every mark must be between 0 and 100.")

    return {"name": name.strip(), "marks": list(marks)}
