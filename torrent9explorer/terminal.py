from torrent9explorer import Utils

from cmd2 import Cmd
import re


class Terminal(Cmd):

    prompt = "t9explore $> "

    def __init__(self):
        Cmd.__init__(self)

    def do_search(self, line):
        from torrent9explorer import Explorer, Searcher
        ''' "name of the serie" limit X '''

        limit = Utils.argument(name="limit", default=1, min=1, line=line)
        stack = Utils.argument(name="stack", default=10, min=1, line=line)
        cut = Utils.argument(name="cut", default=100, min=1, line=line)

        match = re.search(r"^\"(.*?)\"", line, re.MULTILINE)

        if (match == None or len(match.groups()) < 1):
            # TODO: Error
            print("Error, no name found")
            return

        query = match.group(1)

        print("query: " + query + ", limit: " +
              str(limit) + ", stack: " + str(stack) + ", cut: " + str(cut))

        searcher = Searcher(query=query, limit=limit)
        Explorer.get().executeSearch(searcher.prepare().getUrls(), stack, cut)

    def do_dl(self, line):
        from torrent9explorer import PageAnalyzer
        ''' int,int,range-range '''

        if (line == None or not line):
            print("Error, suitable argument")
            return

        pageAnalyzer = PageAnalyzer()

        possibleIds = line.split(",")

        for id in possibleIds:
            # tester si id contient -
            if ("-" in id):
                split = str(id).split("-")

                if (Utils.isStringInt(split[0]) and Utils.isStringInt(split[1])):
                    start = int(split[0])
                    end = int(split[1])

                    if (start < end):
                        itemCount = int(0)

                        for itemId in range(start, end + 1):
                            #print("new id: " + str(itemId))
                            pageAnalyzer.appendId(itemId)
                            itemCount = itemCount + 1

                        #print("you want download : " + str(itemCount - 1) + " episodes")
                    elif (start == end):
                        pageAnalyzer.appendId(start)
                    else:
                        print("Range start can't be bigger than range end")
                else:
                    print("Range must be integer-only")
            else:
                if(Utils.isStringInt(id)):
                    pageAnalyzer.appendId(int(id))
                else:
                    print("Not int")
        
        pageAnalyzer.prepare().download()

    def do_help(self, line):
        output = []
        output.append("Help message")
        output.append("")
        output.append("List of commands and usage:")
        output.append("*-*")
        output.append("SEARCHING")
        output.append("")
        output.append(
            "Search command: search \"something\" -limit 20 -stack 60 -cut 150")
        output.append(
            "\t-limit [number] is maximum of pages that will be fetch")
        output.append(
            "\t-stack [number] is the number of elements to print in a cell ")
        output.append(
            "\t-cut [number] will stop printing element if this number is passed ")
        output.append("")
        output.append("*-*")
        output.append("DOWNLOAD LIST")
        output.append("")
        output.append("Download command: downloadlist 1,3,4,100-300")
        output.append("\t1,3,4 allow you to put single item id")
        output.append("\t100-300 allow you to put ranged-value items ids")

        Utils.printFormat(output)

    def do_exit(self, line):
        exit()
