class InvalidMarksError(Exception):
    """Raised when marks are missing, not numeric, or outside 0 to 100."""


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""


class CalculationError(Exception):
    """Raised when a result cannot be calculated."""
