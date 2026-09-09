"""Run this file to demonstrate the student_processor package."""

from student_processor import (
    CalculationError,
    InvalidMarksError,
    MissingStudentInfoError,
    create_result,
    create_student,
)
from student_processor.logging import configure_logger


def process_students(student_data):
    logger = configure_logger()

    for name, marks in student_data:
        try:
            student = create_student(name, marks)
            result = create_result(student)
            print(
                f"{result['name']}: Total={result['total']}, "
                f"Percentage={result['percentage']:.2f}%, "
                f"Grade={result['grade']}, Status={result['status']}"
            )
        except (InvalidMarksError, MissingStudentInfoError, CalculationError) as error:
            logger.error("Skipping student %r: %s", name, error)


if __name__ == "__main__":
    students = [
        ("Anika", [88, 92, 76, 81, 90]),
        ("Ravi", [75, "absent", 80, 65, 70]),  # logged, then processing continues
        ("Meera", [40, 35, 66, 72, 58]),
        ("", [80, 70, 90, 85, 88]),  # missing name: logged
        ("Dev", [100, 90, 105, 75, 85]),  # invalid mark: logged
    ]
    process_students(students)
