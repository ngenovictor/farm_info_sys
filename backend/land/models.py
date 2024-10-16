from django.contrib.gis.db import models as gis_models
from django.db import models


# Create your models here.
class Land(gis_models.Model):
    """
    Model for Land
    """

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    geo_area = gis_models.PolygonField()
    parent_land = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True)
