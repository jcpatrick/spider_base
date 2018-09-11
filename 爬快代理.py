import urllib.request
from lxml import etree
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

base_url = 'https://www.kuaidaili.com/free/inha/'
offset = 1

f = open('kuaidaili.txt','w')
for i in range(1, 6):
    print("start:" + base_url + str(i))
    request = urllib.request.Request(base_url + str(i), headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    html = etree.HTML(data)
    for each in html.xpath("//table/tbody/tr"):
        td = each.xpath('./td/text()')
        ip = td[0]
        port = td[1]
        f.write(ip + ":" +port + "\n")
    print("end")
    time.sleep(1)

f.close()