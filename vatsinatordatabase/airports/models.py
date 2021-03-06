from django.db import models


class Airport(models.Model):
    """
    The Airport model represents a single airport.
    """
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    iata = models.CharField(max_length=3)
    icao = models.CharField(max_length=4, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()

    def __unicode__(self):
        return unicode("%s %s, %s, %s" % (self.icao, self.name, self.city, self.country))
