import urllib.request
import json
import chardet
import jsonpath

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = urllib.request.urlopen(url)
html = response.read()
encoding = chardet.detect(html)['encoding']
html = html.decode(encoding=encoding)

jsonobj = json.loads(html)

citylist = jsonpath.jsonpath(jsonobj,'$..name')
print(citylist)
print(type(citylist))

content = json.dumps(citylist, ensure_ascii=False)
print(content)
f = open('citi.json','w',encoding='utf-8')
f.write(content)
f.close()

