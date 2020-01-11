from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


# Create your models here.
class BaseModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # set changeReason
    history = HistoricalRecords(inherit=True)

class Team(models.Model):
    class TeamType(models.IntegerChoices):
        Student = 1, 'student'
        Adult = 2, 'adult'
    name = models.CharField('チーム名', max_length=30)
    team_type = models.SmallIntegerField(choices=TeamType.choices, default=TeamType.Student)
    is_authorized = models.BooleanField('認証', default=False)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    email = models.EmailField("メールアドレス", unique=True)
    is_team_leader = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def can_create_event(self):
        return self.team and self.team.is_authorized



