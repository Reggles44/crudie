from django.db import models


class Crudie(models.Model):
    service_key = models.CharField(max_length=200)
    data = models.IntegerField()

    class Meta:
        db_table = "crudie"
