from torrent9explorer import Utils 
from threading import Thread
import time


class Explorer:

    INSTANCE = None
    SITE_URL = ""
    ITEMS = []
    LINE_SEPARATOR = "+ " + ("-" * 4) + " + " + ("-" * 12) + " + " + (
        "-" * 50) + " + " + ("-" * 9) + " + " + ("-" * 6) + " + " + ("-" * 6) + " +"

    def initialize(self, siteUrl):
        from torrent9explorer import Terminal

        Explorer.INSTANCE = self
        Explorer.SITE_URL = siteUrl

        self.terminal = Terminal()
        self.terminal.cmdloop()

    def executeSearch(self, urls, stack, cut):
        from torrent9explorer import Downloader, Regexer
        print("Loading...")

        self.items = []

        for url in urls:
            print("Downloading url: " + url)
            html = Downloader(url).getAsString()
            self.items.extend(Regexer.createItemFromHtml(html))

        progression = 0
        for item in self.items:

            if ((progression % stack) == 0):
                print("\n")
                print(Explorer.LINE_SEPARATOR)
                print("| {:4} | {:12} | {:50} | {:9} | {:6} | {:6} |".format(
                    "ID", "TYPE", "NAME", "SIZE", "SEED", "LEECH"))
                print(Explorer.LINE_SEPARATOR)
            progression = progression + 1

            try:
                print("| {:4} | {:12} | {:50} | {:9} | {:6} | {:6} |".format(
                    item.getId(), item.getType(), item.getName()[:47] + (item.getName()[47:] and '...'), item.getSize(), item.getSeed(), item.getLeech()))
            except Exception as exception:
                pass

            if ((progression % stack) == 0):  # Next loop
                print(Explorer.LINE_SEPARATOR)

            if (progression == cut):
                print("Cut at " + str(cut) + " element(s)")
                break

        Explorer.ITEMS.extend(self.items)

    @staticmethod
    def get():
        return Explorer.INSTANCE


class Searcher:

    SEARCH_BASE = "/search_torrent/{query}/page-{page}"

    def __init__(self, query, limit=1):
        self.query = query
        self.limit = limit - 1

    def prepare(self):
        self.urls = []

        for page in range(0, self.limit + 1):
            self.urls.append(
                Explorer.SITE_URL + Searcher.SEARCH_BASE.format(query=Utils.slugify(self.query), page=page))

        return self

    def getUrls(self):
        return self.urls


class PageAnalyzer:

    def __init__(self):
        self.ids = []
        self.items = []

    def appendId(self, id):
        if (id not in self.ids):
            self.ids.append(id)

    def prepare(self):
        for item in Explorer.ITEMS:
            if(item.getId() in self.ids):
                self.items.append(item)
        return self

    def download(self):
        from torrent9explorer import Downloader, Regexer

        for item in self.items:
            pageContent = Downloader(
                Explorer.SITE_URL + item.getUrl()).getAsString()

            Utils.safePrint("Analyzing page with id '" + str(item.getId()) + "' (name: \"" + item.getName() + "\")")             
            item.setPageContent(pageContent)

            if (Utils.is_empty(pageContent) or pageContent == None):
                continue
            else:
                filePath = Regexer.extractDownloadLinkFromHtml(pageContent)
                
                if (filePath == None):
                    print("No downloadable button found at this page...")
                    continue
                
                url = Explorer.SITE_URL + filePath
                try:
                    Downloader(url).downloadFile(item.getName() + ".torrent")
                except Exception as exception:
                    print("Failed to download file \"" + item.getName() + "\", error: " + str(exception))
