from django.apps import AppConfig


class ProblemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'problems'

"""
Without this file (or without including your app in INSTALLED_APPS),
Django wouldn’t know to look in the problems directory for models, 
migrations, templates (if configured), or static files. 
The AppConfig class is the official way to bundle together
all of that configuration.
"""