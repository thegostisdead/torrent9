#

class Torrent9Item():
    
    INCREMENT = 0

    def __init__(self, type, url, name, size, seed, leech):
        self.id = Torrent9Item.incrementId()
        self.type = type
        self.url = url
        self.name = name.replace("<span style=\"color:#337ab7\">", "").replace("</span>", "") # Search add "blue text" to match search query 
        self.size = size
        self.seed = seed
        self.leech = leech
        self.pageContent = ""

        switcher = {
            "desktop": "Series",
            "video-camera": "Movie",
            "music": "Music",
            "book": "eBook",
        }
        
        self.type = switcher.get(type, "--:" + type)

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def getUrl(self):
        return self.url

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getSeed(self):
        return self.seed

    def getLeech(self):
        return self.leech

    def getPageContent(self):
        return self.pageContent

    def setPageContent(self, content):
        self.pageContent = content
    
    @staticmethod
    def incrementId():
        Torrent9Item.INCREMENT = Torrent9Item.INCREMENT + 1
        return Torrent9Item.INCREMENT
