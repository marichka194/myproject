from django.contrib import admin
from lessons.models import Person, Log, LogModel


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal information', {'fields': ['name', 'dob']}),
        ('Contacts',             {'fields': ['phone', 'address', 'email', 'skype']})
    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Log)
admin.site.register(LogModel)