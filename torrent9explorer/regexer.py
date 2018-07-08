from torrent9explorer import Torrent9Item, Utils
import re


class Regexer():

    CACHE = {}

    @staticmethod
    def createItemFromHtml(html):
        list = []

        regex = r"\<tr\>[ \t\n]*\<td\>\<i\sclass=\"fa\sfa-(.*?)\"\sstyle=\".*?\"\>\<\/i\>[ \t\n]*\<a title=\".*?\"\shref=\"(.*?)\".*?\>(.*?)\<\/a\>\<\/td\>[ \t\n]*\<td\sstyle=\".*?\">(.*?)\<\/td\>[ \t\n]*\<td\sstyle=\".*?\"\>\<span\sclass=\"seed_ok\">(.*?)\<img.*?\>\<\/span\>\<\/td\>[ \t\n]\<td\sstyle=\".*?\"\>(.*?)\<img.*?\>\<\/td\>[ \t\n]*\<\/tr\>"
        matches = re.finditer(regex, str(html), re.MULTILINE | re.DOTALL)

        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            url = match.group(2)

            item = Regexer.CACHE.get(url, None)

            if (item == None):
                item = Torrent9Item(type=match.group(1), url=match.group(2), name=match.group(
                    3), size=match.group(4), seed=match.group(5), leech=match.group(6))
                Regexer.CACHE[url] = item

            list.append(item)

        return list

    @staticmethod
    def extractDownloadLinkFromHtml(html):
        matches = re.search(
            r"\<a\sclass=\"btn\sbtn-danger\sdownload\"\shref=\"([\/download\/\w\/]*?)\"\>.*?\<\/a\>", html, re.DOTALL)

        if (matches):
            return matches.group(1)
        else:
            return None
