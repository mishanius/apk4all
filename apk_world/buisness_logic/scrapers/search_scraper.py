from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel
import urllib
import base64

class SearchScraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, SrcKeyword):
        SrcKeyword = urllib.parse.quote(SrcKeyword)
        UrlScraperObj.__init__(self, "https://appsapk.com/?s={0}".format(SrcKeyword))

    def app_scrape(self):
        apps=[]
        try:
            for i in self.data.find_all("article"):
                item_container = i.find_all("div", {"class": "meta-image"})[0].find("a")
                title = item_container.get('title')
                # i.find_all("header")[0].find("h2", {"class": "entry-title"}).find("a").string
                # TODO rating
                image = item_container.find("img").get('src')
                DetailsLink = base64.b64encode(bytes(item_container.get('href'), 'utf-8')).decode('utf-8')
                app = AppModel(Title=title, Image=image, DetailsLink=DetailsLink)
                apps.append(app)
        except Exception as e:
            x=5
        return apps