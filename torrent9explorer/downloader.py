from urllib.request import urlretrieve
import re
import unicodedata
import urllib


class Downloader:

    def __init__(self, url):
        self.url = url

    def downloadFile(self, file):
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        try:
            urlretrieve(self.url, file)
            return True
        except Exception as exception:
            return False

    def getAsString(self):
        try:
            socket = urllib.request.urlopen(self.url)
            data = socket.read()
            socket.close()

            return data.decode("utf8")
        except Exception as exception:
            return str(exception)
