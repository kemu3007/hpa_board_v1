from django.db import models

from master.models import Team


class Event(models.Model):
    event_name = models.CharField('イベント名', max_length=20)
    start_date = models.DateTimeField('開始時刻', null=True, blank=True)
    end_date = models.DateTimeField('終了時刻', null=True, blank=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    contents = models.TextField()