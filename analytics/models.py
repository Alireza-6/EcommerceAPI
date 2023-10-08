from django.contrib.admin.models import LogEntry
from django.db import models


# class FootPrint(models.Model):
#     ...

class ActionHistory(LogEntry):
    class Meta:
        proxy = True
