from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel
import urllib
import base64
import re

class Top15Scraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self):
        UrlScraperObj.__init__(self, "https://www.9apps.com/android-games-1")

    def game_scrape(self):
        apps=[]
        titles =[]
        try:
            for counter, i in enumerate(self.data.find("div", {"class": "hot-app-list"}).find_all("li")):
                item_container = i
                title = item_container.find("span", {"class":"name"}).text
                if title in titles or counter > 14:
                    continue
                titles.append(title)
                # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
                # TODO rating
                image = item_container.find("img").get('dataimg')
                DetailsLink = base64.b64encode(bytes("2"+item_container.find("a").get('href'), 'utf-8')).decode('utf-8')
                app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
                apps.append(app)
        except Exception as e:
            x=5
        return apps


    def app_scrape(self):
        urlScr = UrlScraperObj("https://www.9apps.com/android-apps-1")
        apps=[]
        titles =[]
        try:
            for counter, i in enumerate(urlScr.data.find("div", {"class": "hot-app-list"}).find_all("li")):
                item_container = i
                title = item_container.find("span", {"class":"name"}).text
                if title in titles or counter > 14:
                    continue
                titles.append(title)
                # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
                # TODO rating
                image = item_container.find("img").get('dataimg')
                DetailsLink = base64.b64encode(bytes("2"+item_container.find("a").get('href'), 'utf-8')).decode('utf-8')
                app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
                apps.append(app)
        except Exception as e:
            x=5
        return apps
