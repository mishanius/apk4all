from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from apk_world.utils.apk_logger import logger
from django.conf import settings
import base64
from apk_world.buisness_logic.scrapers.search_scraper import SearchScraper
from apk_world.buisness_logic.scrapers.itm_scraper import ItmScraper
from apk_world.buisness_logic.scrapers.download_scraper import DownloadScraper
from apk_world.buisness_logic.scrapers.top_15_scraper import Top15Scraper
from rest_framework.views import APIView
from apk_world.serializers import SearchedAppSerializer, AppSerializer
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.renderers import JSONRenderer
# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    s = Top15Scraper()
    games = s.game_scrape()
    apps = s.app_scrape()
    gamesList = [ob.as_json() for ob in games]
    appsList = [ob.as_json() for ob in apps]
    context = {
        'media': settings.MEDIA_URL,
        'topGames': json.dumps(gamesList),
        'gamesList':games,
        'topApps': json.dumps(appsList)
    }
    return HttpResponse(template.render(context, request))

class Search(APIView):
    def get(self, request, pk, format=None):
        logger.debug("search")
        s = SearchScraper(pk)
        apps = s.app_scrape()
        serializer_class = SearchedAppSerializer(apps, many=True)
        return Response(serializer_class.data)

class topApps(APIView):
    def get(self, request, format=None):
        s = Top15Scraper()
        apps = s.app_scrape()
        serializer_class = SearchedAppSerializer(apps, many=True)
        return Response(serializer_class.data)

class GetItem(APIView):
    def post(self, request,name, format=None):
        serializer = SearchedAppSerializer(data=request.data)
        if serializer.is_valid():
            s = DownloadScraper(serializer.validated_data)
            app = s#s.app_scrape()
            serializer_class = AppSerializer(app)
            return Response(serializer_class.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, name, format=None):
        prefixs = int(base64.b64decode(name).decode('utf-8')[0])
        name = base64.b64decode(name).decode('utf-8')[1:]
        s = ItmScraper(name, prefixs)
        app = s.app_scrape()
        if app:
            serializer_class = AppSerializer(app)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer_class.data)

class GetDwonload(APIView):
    def post(self, request, format=None):
        serializer = SearchedAppSerializer(data=request.data)
        if serializer.is_valid():
            s = DownloadScraper(serializer.validated_data)
        # download_url = "http://c3.la4.download.9appsinstall.com:7080/group2/M00/81/B3/RA0DAFlTx2iAC0__BV7aWD5bz6s908.apk?pid=13249&title=Clash-of-Clans_v9.105.9pakage.apk&a=9999"
            serializer_class = AppSerializer(s.app)
            return Response(serializer_class.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, name, format=None):
        prefixs = int(base64.b64decode(name).decode('utf-8')[0])
        name = base64.b64decode(name).decode('utf-8')[1:]
        s = ItmScraper(name, prefixs)
        app = s.app_scrape()
        if app:
            serializer_class = AppSerializer(app)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer_class.data)



