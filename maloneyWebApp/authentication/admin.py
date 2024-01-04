from django.contrib import admin

# # Register your models here.
# from .models import *

# admin.site.register(AddLeaseProperty)
# admin.site.register(AgeGroup)


from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config('authentication').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass