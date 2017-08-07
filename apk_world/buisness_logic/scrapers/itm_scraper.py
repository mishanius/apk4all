from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel
import urllib
import mtranslate

class ItmScraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, itm):
        if isinstance(itm, dict):
            UrlScraperObj.__init__(self, itm['DetailsLink'])
            self.itm = itm
        else:
            UrlScraperObj.__init__(self, itm)
            self.itm = None

    def app_scrape(self):
        app = None
        try:
            item_container = self.data.find("main", {"class": "main-box"}).find("article")
            if self.itm:
                app = AppModel(**self.itm)
            else:
                Title = item_container.find("header", {"class": "entry-header"}).find("h1").text
                Image = item_container.find("div", {"class": "app-icon"}).find("img").get('src')
                try:
                    DownloadLink = item_container.find("div", {"class": "entry-content"}).find_all("p")[-1].find("a").get('href')
                except Exception as e:
                    DownloadLink = self.data.find("a", {"class": "download"}).get('href')
                DetailsLink = DownloadLink
                # TODO rating
                Rating =0
                app = AppModel(Title = Title, Image = Image, DownloadLink = DownloadLink, DetailsLink = DetailsLink)
            app.Description = self.scrape_description(item_container.find("div", {"class": "entry-content"}))
                # item_container.find("div", {"class": "entry-content"}).find_all("p")[1].text
            x = mtranslate.translate(app.Description, "ru", "auto")
            app.FrDescription = x
        except Exception as e:
            x=5
        return app

    def scrape_description(self, item_container):
        description = ""
        try:
            if item_container.find("div", {"class": "more-block"}):
                description += item_container.find("div", {"class": "more-block"}).text
                item_container = self.data
            for i in item_container.find_all("p", {'class': None, "style": None}):
                if i.find("img") or i.find("a") or i.find("script") or i.find("p"):
                    continue
                elif len(i.text)>5:
                    description += "\n"+i.text
        except Exception as e:
            x=5
        return description