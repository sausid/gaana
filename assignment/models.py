from django.db import models


class Location(models.Model):
    key = models.JSONField(max_length=20, null=True, unique=True)
    unlocs = models.JSONField(default=list, blank=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    alias = models.JSONField(default=list, blank=True)
    regions = models.JSONField(default=list, blank=True)
    coordinates = models.JSONField(default=list, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
