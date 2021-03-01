#coding=utf-8

from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
r = session.get("https://cn.wowhead.com/tailoring")

#print(r.html.html)
#print(r.html.find('script.type'))
#print(r.html.xpath("/body/div[6]/div/div[1]/div[2]/div[4]/script[6]"))

soup = BeautifulSoup(r.text,'lxml')
for a in soup.find_all(class_='listview-cleartext.q4'):
    link = a
    print(link)