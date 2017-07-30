from django.contrib import admin
from streamit.models import Show


class ShowAdmin(admin.ModelAdmin):
    list_display = ('suid', 'key', 'm3u8', 'on_air')
    readonly_fields = ('uid', 'key')

admin.site.register(Show, ShowAdmin)


