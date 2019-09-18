from django.db import models


class Site(models.Model):
    name = models.URLField()

    def __str__(self):
        return '%s ' % self.name


class ElapsedTime(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    time_elapsed = models.FloatField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)