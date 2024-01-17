from django.apps import AppConfig


class DoctorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' 
    #BigAutoField to store 64-bit integers(Used when many rows are expected)
    name = 'doctors'
