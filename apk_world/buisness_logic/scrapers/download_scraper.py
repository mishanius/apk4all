from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel
import urllib
import base64

class DownloadScraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, itm):
        if isinstance(itm, dict):
            UrlScraperObj.__init__(self, "https://apkpure.com"+itm['DetailsLink'])
            self.itm = itm
        else:
            self.itm = None

    def app_scrape(self):
        app=None
        try:
            DownloadLink = self.data.find("div", {"class": "fast-download-box"}).find("a", {"id": "download_link"}).get('href')
            app = AppModel(**self.itm)
            app.DownloadLink = DownloadLink
            app.DetailsLink = "njasndasndlajldsjnladn"
        except Exception as e:
            x=5
        return app