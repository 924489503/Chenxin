#-*-coding:utf-8-*-
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('C:/index.html'),"html.parser")
for link in soup.find_all("a"):
    print link.get('href')
    print link.get_text();