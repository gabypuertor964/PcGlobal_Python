from django.apps import AppConfig


class LandingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing'

    # Configurar Nombre Personalizado
    verbose_name="Clientes"
