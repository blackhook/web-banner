import urllib,sys
from BeautifulSoup import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )
type = sys.getfilesystemencoding()

def check(url):
    try:
        req=urllib.urlopen(url)
        info = req.info()
        webServerType = (info.dict)['server']
        print url + " : " + '{'+webServerType.strip().encode(type)+'}',
    except Exception, e:
        pass

def title(url):
    try:
        content = urllib.urlopen(url).read()
        soup = BeautifulSoup(content,fromEncoding="gb18030")
        title_s= soup.find('title')
        print '   '+str(title_s).encode(type)
    except Exception, e:
        pass

openfile = open("in.txt",'r')
for read in openfile.readlines():
    read = read.strip()
    check(read)
    title(read)

