from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Django AppConfig for the 'about' application.
    This configuration class sets the default auto field type to 'BigAutoField'
    and specifies the name of the application as 'about'.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
