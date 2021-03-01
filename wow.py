#coding=utf-8


from requests_html import HTMLSession


session = HTMLSession()
r = session.get("https://cn.wowhead.com/spell=265106")
#print(r.html.html)

print(r.html.search('"moneygold">{}<')[0])
#售价
print(r.html.find("div.whtt-sellprice",first = True).html)
#材料
print(r.html.find("div.indent.q1",first = True).text)
#print(r.html.xpath("/html/body/div[5]/div/div[1]/div[2]/div[4]/div[2]/div[5]/table/tbody/tr[1]/td/table[2]/tbody/tr/td/div[2]",first=True).text)