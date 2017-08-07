import urllib.request
from bs4 import BeautifulSoup

class UrlScraperObj(object):
    '''return beutifull soap object of the url string or an array of objects if array of urls provided'''
    def __init__(self, urls, nrequsts=1):
        self.requests_list = []
        self.url = urls
        self.data = None
        try:
            response = urllib.request.urlopen(urls)
            self.data = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        except Exception as e:
            self.data = []
