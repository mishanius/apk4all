from django.db import models

# Create your models here.
class AppModel(models.Model):

    def __str__(self):
        return self.Title

    Title = models.CharField(max_length=300)
    Image = models.CharField(max_length=300)
    DetailsLink = models.CharField(blank=True, max_length=300)
    DownloadLink = models.CharField(blank=True, max_length=300)
    Rating = models.DecimalField(default=1, decimal_places=0, max_digits=1)
    Description = models.CharField(blank=True, max_length=30000)
    FrDescription = models.CharField(blank=True, max_length=30000)
