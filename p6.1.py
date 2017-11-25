
import urllib2

url=urllib2.urlopen('https://s.taobao.com/list?spm=a217f.8051907.312344.22.Qwa9lh&q=%E6%AF%9B%E9%92%88%E7%BB%87%E8%A1%AB&cat=16&style=grid&seller_type=taobao')
print url.geturl()