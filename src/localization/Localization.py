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
        if self.session.has("locale"):
            locale = self.session.get("locale")
        else:
            locale = self.config.get("locale", "en")
            self.session.set("locale", locale)
        return locale

    def setup_view(self) -> None:
        self.app.make("view").share(
            {
                "__": self.__locale,
            }
        )

    def __locale(self, key: str) -> str:

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
        self.session.set("locale", locale)

    def is_locale(self, locale: str) -> bool:
        return self.__get_locale() == locale
