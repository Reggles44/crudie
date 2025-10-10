from django.db import models


class FooBar(models.Model):
    id = models.AutoField(primary_key=True)
    foo = models.CharField()
    bar = models.IntegerField()

    class Meta:
        db_table = "foobar"
