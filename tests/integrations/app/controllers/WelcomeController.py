"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from src.localization.facades import Localization


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        Localization.set_locale("np")
        print(Localization.current_locale())
        return view.render("welcome")
