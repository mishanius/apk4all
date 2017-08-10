from apk_world.models import AppModel
from rest_framework import serializers


class SearchedAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppModel
        fields = ('Title', 'Image', 'DetailsLink')

class AppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppModel
        fields = ('Title', 'Image', 'DetailsLink', 'FrDescription', 'Description', 'DownloadLink','images')