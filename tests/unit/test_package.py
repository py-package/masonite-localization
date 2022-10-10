from masonite.tests import TestCase

from src.localization.facades import Localization


class TestLocalization(TestCase):

    def setUp(self):
        super().setUp()
        session = self.application.make("session")
        session.start("cookie")

    def test_current_locale(self):
        self.assertEqual(Localization.current_locale(), 'en')

    def test_set_locale(self):
        Localization.set_locale('np')
        self.assertEqual(Localization.current_locale(), 'np')

    def test_translation(self):
        self.assertEqual(Localization.translation('greet'), 'Hello')
        self.assertEqual(Localization.translation('address.street'), 'Pepsicola')
        Localization.set_locale('np')
        self.assertEqual(Localization.translation('greet'), 'नमस्ते')
        self.assertEqual(Localization.translation('address.street'), 'पेप्सिकोला')
