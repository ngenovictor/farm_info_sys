import math

from django.contrib.gis import admin as gis_admin
from leaflet import admin as leaflet_admin

from .models import Land


def getCoordsM2(coordinates):
    d2r = 0.017453292519943295  # Degrees to radiant
    area = 0.0
    for coord in range(0, len(coordinates)):
        point_1 = coordinates[coord]
        point_2 = coordinates[(coord + 1) % len(coordinates)]
        area += ((point_2[0] - point_1[0]) * d2r) * (
            2 + math.sin(point_1[1] * d2r) + math.sin(point_2[1] * d2r)
        )
    area = area * 6378137.0 * 6378137.0 / 2.0
    return math.fabs(area)


def getGeometryM2(geometry):
    area = 0.0
    if geometry.num_coords > 2:
        # Outer ring
        area += getCoordsM2(geometry.coords[0])
        # Inner rings
        for counter, coordinates in enumerate(geometry.coords):
            if counter > 0:
                area -= getCoordsM2(coordinates)
    return area


@gis_admin.register(Land)
class LandAdmin(leaflet_admin.LeafletGeoAdmin):
    def area(self, obj):
        m2_square = getGeometryM2(obj.geo_area)
        acres = m2_square * 0.000247105
        return f"{m2_square:.2f} m² ({acres:.2f} acres)"

    list_display = ("name", "description", "parent_land", "area")
