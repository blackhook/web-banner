#coding:utf-8

import chardet,urllib2
#抓取网页html
line = "http://www.baidu.com"
html_1 = urllib2.urlopen(line,timeout=120).read()
#print html_1
encoding_dict = chardet.detect(html_1)
#print encoding
web_encoding = encoding_dict['encoding']
if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
  html = html_1
else :
   html = html_1.decode('gbk','ignore').encode('utf-8')

print html
