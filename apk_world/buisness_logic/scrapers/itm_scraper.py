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
            UrlScraperObj.__init__(self, "https://apkpure.com"+itm)
            self.itm = None

    def app_scrape(self):
        app = None
        try:
            if self.itm:
                app = AppModel(**self.itm)
            else:
                Title = self.data.find("div", {"class": "title-like"}).find("h1").text
                Image = self.data.find_all("dt")[0].find("img").get('src')
                DownloadLink = self.data.find("div", {"class": "ny-down"}).find("a").get('href')
                DetailsLink = self.data.find("div", {"class": "ny-down"}).find("a").get('href')
                # TODO rating
                Rating =0
                app = AppModel(Title = Title, Image = Image, DownloadLink = DownloadLink, DetailsLink = DetailsLink)
            app.Description = self.data.find("div", {"id": "describe"}).find("div", {"class": "content"}).text
            x = mtranslate.translate(app.Description, "ru", "auto")
            app.FrDescription = x
        except Exception as e:
            x=5
        return app