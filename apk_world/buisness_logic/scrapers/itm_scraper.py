from apk_world.buisness_logic.scrapers.url_scraper import UrlScraperObj
from apk_world.models import AppModel, ImageModel
import urllib
import mtranslate
import re

class ItmScraper(UrlScraperObj):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, itm, p=0):
        prefixs = ["","http://top-android.org", "https://www.9apps.com"]
        self.site = p
        if isinstance(itm, dict):
            UrlScraperObj.__init__(self, prefixs[p]+itm['DetailsLink'])
            self.itm = itm
        else:
            UrlScraperObj.__init__(self, prefixs[p]+itm)
            self.itm = None

    def app_scrape(self):
        app = None
        if self.site==0:
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
        elif self.site==1:
            app = self.russian_scrape()
        elif self.site == 2:
            app = self.nineAppsScrape()
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

    def russian_scrape(self):
        app=None
        try:
            item_container = self.data.find("div", {"class": "mside"})
            left_item_container = item_container.find("div", {"class": "info-lside"})
            details_container = item_container.find("div", {"class": "info-rside"})
            images=[]
            if self.itm:
                app = AppModel(**self.itm)
            else:
                Title = details_container.find("b", {"class": "dtitle"}).text
                root_url ="http://top-android.org"
                Image = root_url + left_item_container.find("div", {"class": "app-ful-img"}).find("img").get('src')
                download_container = item_container.find("div", {"class": "app-download"})
                DownloadLink = root_url+download_container.find_all("div",{"class":"down-line"})[0].find("a").get('href')
                DetailsLink = DownloadLink
                # TODO rating
                Rating = 0
                app = AppModel(Title=Title, Image=Image, DownloadLink=DownloadLink, DetailsLink=DetailsLink)
                app.img_arr=[]
                app = self.scrape_images(app, details_container.find("div",{"class":"screen-gal"}), "a", "href",root_url)
            ignrtg = ["a","div"]
            app.Description = self.russian_scrape_description(item_container.find("div", {"class": "file-desc"}),"p",""
                                                              ,ignrtg)
            x = mtranslate.translate(app.Description, "en", "auto")
            app.FrDescription = x
        except Exception as e:
            x = 5
        return app

    def scrape_images(self, appModel, img_container, url_tag, url_derective, root_url=""):
        images = []
        for count,i in enumerate(img_container.find_all(url_tag)):
            # have alook at models before touching
            if not root_url+i.get(url_derective) in images and count<5:
                images.append(root_url+i.get(url_derective))
        appModel.images = images
        return appModel


    def russian_scrape_description(self, item_container, text_tag, attrs, ignore_tags):
        description = ""
        try:
            for i in item_container.find_all(text_tag, attrs):
                found_baned = False
                for tag in ignore_tags:
                    if i.find(tag) and not found_baned:
                        found_baned = True
                if not found_baned and len(i.text) > 5:
                    description += "\n" + i.text
        except Exception as e:
            x = 5
        return "<br />".join(re.sub(r'.+?9Apps[\.,\s]?.+[\!\.,][\n\s]+',"",description,re.DOTALL).split("\n"))

    def nineAppsScrape(self):
        app = None
        try:
            item_container = self.data.find("div", {"class": "detail-info-section"})
            main_info = self.data.find("div", {"class": "main-info"})
            details_container = item_container.find("div", {"class": "detail-left"})
            if not details_container:
                details_container=item_container
            images = []
            if self.itm:
                app = AppModel(**self.itm)
            else:
                Title = main_info.find("div", {"class": "text"}).find("span",{"itemprop":"name"}).text
                root_url = "https://www.9apps.com"
                Image = main_info.find("div", {"class": "pic"}).find("img").get('dataimg')
                DownloadLink = root_url + main_info.find("div", {"class": "download"}).find("a").get('href')
                DetailsLink = DownloadLink
                # TODO rating
                Rating = 0
                app = AppModel(Title=Title, Image=Image, DownloadLink=DownloadLink, DetailsLink=DetailsLink)
                app.img_arr = []
                app = self.scrape_images(app, details_container.find("div", {"class": "screen-shot"}), "img", "src")
            ignrtg = ["a", "div"]
            app.Description = self.russian_scrape_description(details_container, "p",
                                                              {"class":"description"}, ignrtg)
            x = mtranslate.translate(app.Description, "ru", "auto")
            app.FrDescription = x
        except Exception as e:
            x = 5
        return app