#!/usr/bin/env python
# coding=utf-8
import urllib,sys,MySQLdb,chardet,socket
from BeautifulSoup import BeautifulSoup
timeout=2
socket.setdefaulttimeout(timeout)
reload(sys)
sys.setdefaultencoding( "utf-8" )
db = MySQLdb.connect("localhost","root","","banner",charset='utf8')
cursor = db.cursor()
openfile = open("in.txt",'r')
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
for read in openfile.readlines():
    read = read.strip()
    try:
        req=urllib.urlopen(read)
        info = req.info()
        webServerType = (info.dict)['server']
        content = urllib.urlopen(read).read()
        encoding_content = chardet.detect(content)
        web_encoding = encoding_content['encoding']
        if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
            content_1 = content
        else :
            content_1 = content.decode('gbk','ignore').encode('utf-8')
        soup = BeautifulSoup(content_1)
        title= soup.find('title')
        banner=webServerType.strip()

        read_s=str(read)
        banner_s=str(banner)
        title_s=str(title)
        print str(read)+'  '+str(banner)+'  '+str(title)
        sql = "INSERT INTO info(domain,banner,title)  VALUES ('%s', '%s', '%s')" % (read_s,banner_s,title_s)
    except Exception, e:
        print str(e)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
db.close()