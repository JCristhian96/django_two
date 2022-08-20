from django.contrib import admin
# Models
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    '''Admin View for Person'''
    pass