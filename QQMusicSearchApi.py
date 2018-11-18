import urllib
import urllib2
import json


def keywordSearch(keyword):
    url = "https://api.bzqll.com/music/tencent/search?key=579621905&s={keyword}&limit=100&offset=0&type=song" \
        .format(keyword=keyword)
    req = urllib2.Request(url)
    resdata = urllib2.urlopen(req)
    res = resdata.read()
    print res
    obj = json.loads(res)
    return obj
