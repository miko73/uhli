from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsageAddresList(models.Model):
    UsageLabel = models.CharField(max_length=80, null=True, verbose_name="Žánr")
    UsageCode = models.IntegerField (default=1, null=True)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return "Typy pudov: {0}".format(self.UsageAddresList)

    class Meta:
        verbose_name = "UsageLabel"
        verbose_name_plural = "UsageLabels"
