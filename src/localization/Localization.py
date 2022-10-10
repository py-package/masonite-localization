import json
import os
from masonite.configuration import config
from masonite.utils.location import base_path


class Localization:
    def __init__(self, app) -> None:
        self.app = app
        self.config = config("localization")
        self.session = app.make("session")

    def __get_locale(self):
        if self.session.has("localization"):
            locale = self.session.get("localization")
        else:
            locale = self.config.get("localization", "en")
            self.session.set("localization", locale)
        return locale

    def setup_view(self) -> None:
        self.app.make("view").share(
            {
                "__": self.translation,
            }
        )

    def translation(self, key: str) -> str:

        if not key:
            return ""

        locale_path = os.path.join(base_path(), "lang", self.__get_locale() + ".json")

        if not os.path.exists(locale_path):
            raise Exception("Locale file does not exist")

        with open(locale_path, "r") as json_file:
            data = json.load(json_file)

        keys = key.split(".")

        value = data
        for key in keys:
            value = value.get(key, "")
            if value == "":
                break

        return value

    def current_locale(self) -> str:
        return self.__get_locale()

    def set_locale(self, locale: str) -> None:
        self.session.set("localization", locale)

    def is_locale(self, locale: str) -> bool:
        return self.__get_locale() == locale
