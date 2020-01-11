from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from board.models import Event

admin.site.register(Event, SimpleHistoryAdmin)