from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from static.models import StaticPage

# Register your models here.
admin.site.register(StaticPage, SimpleHistoryAdmin)