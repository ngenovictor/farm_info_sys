from django.db import models


# Create your models here.
class CowBreed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Cow(models.Model):
    name_id = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    breed = models.ForeignKey(CowBreed, on_delete=models.DO_NOTHING)
    date_of_birth = models.DateTimeField()
    father = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
    mother = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)
