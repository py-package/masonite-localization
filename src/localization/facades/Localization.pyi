from masonite.request.request import Request

class Localization:
    def current_locale() -> str:
        """Returns the current locale."""
        ...
    def set_locale(self, locale: str) -> str:
        """Sets the current locale."""
        ...
    def is_locale(self, locale: str) -> bool:
        """Returns true if the current locale is the same as the locale passed."""
        ...
