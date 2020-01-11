from django.db import models
from master.models import  BaseModelMixin

# Create your models here.
class StaticPage(BaseModelMixin):
    class PageType(models.IntegerChoices):
        Top = 1, 'top'
        EventContents = 2, 'eventContents'
        Supporter = 3, 'supporter'
    pagetype = models.SmallIntegerField(choices=PageType.choices)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=20)
    html_text = models.TextField()

    def __str__(self):
        return f'{self.pagetype} - {self.title}'