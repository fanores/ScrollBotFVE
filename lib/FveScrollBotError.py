"""FVE ScrollBot Error/Exception"""


class FveScrollBotError(Exception):
    """Base class for exceptions in FveScrollBot project."""
    pass


class FveHttpError(FveScrollBotError):
    """Exceptions raised for HTTP errors."""

    def __init__(self, message):
        self.message = message


class FveXmlError(FveScrollBotError):
    """Exceptions raised for XML errors."""

    def __init__(self, message):
        self.message = message
