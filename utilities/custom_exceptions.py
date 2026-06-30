class BrowserNotSupported(Exception):
    """Raised when an unsupported browser is requested."""
    pass


class ElementNotFound(Exception):
    """Raised when an expected element cannot be found."""
    pass