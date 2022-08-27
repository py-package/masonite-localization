"""A LocalizationProvider Service Provider."""

import os
from masonite.packages import PackageProvider
from masonite.utils.location import base_path
from ..Localization import Localization


class LocalizationProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("localization")
            .name("localization")
            .config("config/localization.py", publish=True)
        )

        # check if lang directory exists
        locale_path = os.path.join(base_path(), "lang")
        if not os.path.exists(locale_path):
            # create directory
            os.makedirs(locale_path, exist_ok=True)
            # copy files from stubs to above path
            # stub_path = os.path.join(Path(__file__).parent, "..", "stubs", "en.json")
            # shutil.copyfile(stub_path, os.path.join(locale_path, "en.json"))

    def register(self):
        super().register()

        localization = Localization(app=self.application)
        self.application.bind("localization", localization)
        localization.setup_view()

    def boot(self):
        """Boots services required by the container."""
        pass
