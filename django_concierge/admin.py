from django.contrib import admin

from django_concierge.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass
