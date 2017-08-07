from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apk_world.utils.apk_logger import logger
from django.conf import settings
import base64
from apk_world.buisness_logic.scrapers.search_scraper import SearchScraper
from apk_world.buisness_logic.scrapers.itm_scraper import ItmScraper
from apk_world.buisness_logic.scrapers.download_scraper import DownloadScraper
from rest_framework.views import APIView
from apk_world.serializers import SearchedAppSerializer, AppSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):
    template = loader.get_template('index.html')

    context = {
        'media': settings.MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

class Search(APIView):
    def get(self, request, pk, format=None):
        logger.debug("search")
        s = SearchScraper(pk)
        apps = s.app_scrape()
        serializer_class = SearchedAppSerializer(apps, many=True)
        return Response(serializer_class.data)

class GetItem(APIView):
    def post(self, request,name, format=None):
        serializer = SearchedAppSerializer(data=request.data)
        if serializer.is_valid():
            s = DownloadScraper(serializer.validated_data)
            app = s.app_scrape()
            serializer_class = AppSerializer(app)
            return Response(serializer_class.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, name, format=None):
        name = base64.b64decode(name).decode('utf-8')
        s = ItmScraper(name)
        app = s.app_scrape()
        if app:
            serializer_class = AppSerializer(app)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer_class.data)



