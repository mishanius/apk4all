from apk_world.models import AppModel
from urllib.request import Request, urlopen

class DownloadScraper(object):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, itm):
        self.app = AppModel(**itm)
        # self.app.DownloadLink = "http://c3.la4.download.9appsinstall.com:7080/group2/M00/81/B3/RA0DAFlTx2iAC0__BV7aWD5bz6s908.apk?pid=13249&title=Clash-of-Clans_v9.105.9pakage.apk&a=9999"
        url = self.app.DetailsLink
        try:
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(url, headers=hdr)
            response = urlopen(req)
            self.app.DownloadLink = response.url
        except Exception as e:
            self.app.DownloadLink = ""