"""A simple package for validating students and calculating their results."""

from .exceptions import CalculationError, InvalidMarksError, MissingStudentInfoError
from .result_calculations import create_result
from .student_operations import create_student

__all__ = [
    "CalculationError",
    "InvalidMarksError",
    "MissingStudentInfoError",
    "create_student",
    "create_result",
]
