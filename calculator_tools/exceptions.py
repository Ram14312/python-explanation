class InvalidOperationError(Exception):
    """Raised when calculator input or an operation is not valid."""

    def __init__(self, message):
        super().__init__(message)
