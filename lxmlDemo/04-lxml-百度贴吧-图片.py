import urllib.request
import urllib.parse
from lxml import etree
class Spider(object):
    def __init__(self):
        self.title = input("请输入要访问的贴吧：")
        self.startPage = int(input("请输入要起始页码："))
        self.endPage = int(input("请输入要结束页码："))

        self.baseURL = 'https://tieba.baidu.com'

        self.headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}'}

        self.pageCode = 1#页面编号，从1开始

    def tiebaSpider(self):
        for page in range(self.startPage, self.endPage + 1):
            pn = (page - 1) * 50
            queryStr = {
                'kw': self.title,
                'pn': pn
            }
            queryStr = urllib.parse.urlencode(queryStr)
            url = self.baseURL + '/f?' + queryStr
            print("tielbar-----"+url)
            self.loadPage(url)

    def loadPage(self, url):
        '''加载页面'''
        #注意这里传的是header=
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        selector  =etree.HTML(html)
        #//div[@class="threadlist_lz clearfix"]/div/a[@rel="noreferrer"]/@href
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a[@rel="noreferrer"]/@href')
        print(links)
        for link in links:
            imgPageURL = self.baseURL + link#贴吧详细页url
            # print(imgPageURL)
            self.loadImages(imgPageURL)


    def loadImages(self, link):
        request = urllib.request.Request(link, headers=self.headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        selector = etree.HTML(html)

        #//*/img[@class="BDE_Image"]/@src
        imgURLs = selector.xpath('//*/img[@class="BDE_Image"]/@src')

        for imgUrl in imgURLs:
            fileType = imgUrl.split('.')[-1]
            self.downloadImage(imgUrl, fileType)
    def downloadImage(self, url, filetype):
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(request)
        img = response.read()
        #文件名字可以截取url最后一个/后面的那部分url.split('/')[-1]
        f = open("./images/" + str(self.pageCode) + "." + filetype, 'wb')
        f.write(img)
        f.close()
        self.pageCode += 1

if __name__ == '__main__':
    spider = Spider()
    spider.tiebaSpider()