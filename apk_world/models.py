from django.db import models
from django.db.models import ForeignKey

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
    img_arr = []

    @property
    def images(self):
        return self.img_arr

    @images.setter
    def images(self, imgs):
        self.img_arr = imgs

    def as_json(self):
        return dict(
            Title=self.Title, Image=self.Image,
            DetailsLink=self.DetailsLink,
            DownloadLink=self.DownloadLink,
            Description=self.Description)



class ImageModel(models.Model):
    related_to_app = ForeignKey(AppModel, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.url
