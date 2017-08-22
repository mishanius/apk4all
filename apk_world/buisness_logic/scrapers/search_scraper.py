from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel
import urllib
import base64
import re

class SearchScraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, SrcKeyword):
        self.SrcKeyword = urllib.parse.quote(SrcKeyword)
        # UrlScraperObj.__init__(self, "https://appsapk.com/?s={0}".format(SrcKeyword))
        UrlScraperObj.__init__(self, "https://www.9apps.com/search/tag-{0}-1/".format(SrcKeyword))


    def app_scrape(self):
        apps = []
        try:
            search_container = self.data.find("div",{"class":"hot-app-list"})
            for i in search_container.find_all("li"):
                item_container = i.find("div", {"class": "item"}).find("a")
                title = item_container.find("div", {"class": "info"}).find("span", {"class":"name"}).text
                # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
                # TODO rating
                image = item_container.find("img").get('dataimg')
                DetailsLink = base64.b64encode(bytes("2"+item_container.get('href'), 'utf-8')).decode('utf-8')
                app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
                apps.append(app)
        except Exception as e:
            x=5
        if not apps:
            apps = self.russian_scrape()
        return apps

    def russian_scrape(self):
        apps=[]
        SrcKeyword = re.sub(r'%20', '+', self.SrcKeyword)
        urlS=UrlScraperObj("http://top-android.org/search/?q={0}".format(SrcKeyword))
        try:
            searchContainer = urlS.data.find("div", {"class": "mside"})
            for i in searchContainer.find_all("div", {"class": "short"}):
                heading = i.find("div", {"class": "heading"})
                title = heading.find("div",{"class":"app-info"}).find("a").text
                title = re.sub(r'\n', '', title)
                # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
                # TODO rating
                image = "http://top-android.org"+heading.find("a").find("img").get("src")
                DetailsLink = heading.find("a").get('href')
                DetailsLink=base64.b64encode(bytes("1"+DetailsLink,'utf8')).decode('utf-8')
                app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
                apps.append(app)
        except Exception as e:
            x=5
        return apps


        # old  appsapk scrape
        # def app_scrape(self):
        #     apps=[]
        #     try:
        #         for i in self.data.find_all("article"):
        #             item_container = i.find_all("div", {"class": "meta-image"})[0].find("a")
        #             title = item_container.get('title')
        #             # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
        #             # TODO rating
        #             image = item_container.find("img").get('src')
        #             DetailsLink = base64.b64encode(bytes("0"+item_container.get('href'), 'utf-8')).decode('utf-8')
        #             app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
        #             apps.append(app)
        #     except Exception as e:
        #         x=5
        #     if not apps:
        #         apps = self.russian_scrape()
        #     return apps