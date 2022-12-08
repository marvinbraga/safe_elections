from django.contrib import admin

from core.partidos.models import Partido


class PartidoAdmin(admin.ModelAdmin):
    list_display = ["name", "short_name", "number", "type"]
    list_display_links = ["short_name", "number"]


admin.site.register(Partido, PartidoAdmin)
