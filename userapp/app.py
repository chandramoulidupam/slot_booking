from django.apps import AppConfig


class UserappAppConfig(AppConfig):
    name = "userapp"

    def ready(self):
        from userapp import signals # pylint: disable=unused-variable
