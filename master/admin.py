from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from master.models import User, Team

admin.site.register(User, SimpleHistoryAdmin)
admin.site.register(Team, SimpleHistoryAdmin)