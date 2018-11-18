import os
import urllib
import urllib2
import json

url = "https://api.bzqll.com/music/tencent/search?key=579621905&s=123%E6%9C%A8%E5%A4%B4%E4%BA%BA&limit=100&offset=0&type=song"
req = urllib2.Request(url)
resdata = urllib2.urlopen(req)
res = resdata.read()
print res
obj = json.loads(res)
def Schedule(a, b, c):
    """''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

local = os.path.join('./', 'test.mp3')
print obj['data'][0]['url']
urllib.urlretrieve(obj['data'][0]['url'], local, Schedule)

