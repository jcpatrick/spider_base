import urllib.request
from lxml import etree
import json
page = 1
url = "https://www.qiushibaike.com/8hr/page/"+str(page) + '/'
headers = {
    'User-Agent': 'Mozilla/5.o (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}
try:
    request = urllib.request.Request(url, headers= headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    html = html.decode('utf-8')
    #

    resHtml = etree.HTML(html)
    #获得每一个帖子
    result = resHtml.xpath('//div[contains(@id,"qiushi_tag")]')

    list = []
    for block in result:
        item = {}
        #获取头像的url
        #/ div / a / img / @ src
        imgurl = block.xpath('./div/a/img/@src')#[0]
        item['imgUrl'] = imgurl
        #获取作者名称
        #/div/a/h2
        author = block.xpath('./div/a/h2')[0].text.strip()
        item['author'] = author
        #内容
        #//div[@class="content"]
        content = block.xpath('.//div[@class="content"]//span')[0].text.strip()
        print(content)
        item['content'] = content
        #点赞数
        #//span[@class="stats-vote"]//i
        vote = block.xpath('.//i')[0].text
        item['vote'] = vote
        #评论数
        #//span[@class="stats-comments"]//i
        comments = block.xpath('.//i')[1].text
        item['comments'] = comments
        list.append(item)
    qiushi = {'qiushi': list}
    print(qiushi)
    json.dump(qiushi, open('qiushi.json', 'w', encoding='utf-8'), ensure_ascii=False)


except Exception as e:
    print(e)