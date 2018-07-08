import re
import unicodedata
import sys


class Utils:

    @staticmethod
    def slugify(string):
        sub = unicodedata.normalize('NFKD', string)
        return re.sub('[-\\s]+', '-', re.sub('[^\\w\\s-]', '', sub)
                      .strip()
                      .lower())

    @staticmethod
    def printFormat(object):
        print('+ ' + ("-" * 102) + ' +')

        if isinstance(object, list):
            for string in object:
                if string == '*-*':
                    print('+ ' + ("-" * 102) + ' +')
                else:
                    Utils.safePrint('| {:102} |'.format(
                        string.replace('\t', ' ' * 4)))
        else:
            Utils.safePrint('| {:102} |'.format(object.replace('\t', ' ' * 4)))

        print('+ ' + ("-" * 102) + ' +')

    @staticmethod
    def safePrint(object):
        print(object, file=sys.stderr)

    @staticmethod
    def is_empty(object):
        if object:
            return False
        else:
            return True

    @staticmethod
    def argument(name, default, min, line):
        if (name in line):
            match = re.search(
                r"^.*?[ \t]+[-]{0,2}" + name + "[ \t:=]+([\d]+)", line, re.MULTILINE)

            if (match != None and len(match.groups()) == 1):
                return max(1, int(match.group(1)))
        return default

    @staticmethod
    def isStringInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
