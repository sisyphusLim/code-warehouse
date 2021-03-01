from requests_html import HTMLSession
from requests_html import Element



session = HTMLSession()
r = session.get(r"https://cn.wowhead.com/search?q=浪息亚麻长裤#professions")
#print(r.html.xpath('//body/div[7]/div/div[1]/div[2]/div[4]/div[4]/div[4]/div[2]/div[2]/div/table/tbody/tr/td[3]/div/a').html)



#print(r.html.find("div#search-listview.listview").links)
#print(r.html.find("a.listview-cleartext.q2",first=True).text)
print(r.html.search('/spell={}"}')[0])
