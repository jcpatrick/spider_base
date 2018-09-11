import urllib.parse
import urllib.request

def loadPage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1; Trident/5.0;'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    #return response.read()#如果以wb的形式写文件，就不用decode
    return response.read().decode(encoding='utf-8')


def writeToFile(html, filename):
    # with open(filename, 'wb') as f:#以二进制的格式保存文件
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(html)
    print("-" * 20)

def start_download(url, begin_page, end_page):
    header = {'User-Agent': 'Mozilla/5.0 '}
    print("123")
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50

        full_url = url + '&pn=' + str(pn)
        filename = '第%d页.html'%page

        print('正在下载%d页...'%pn)
        html = loadPage(url)
        writeToFile(html, filename)

def main():
    kw = input("请输入要爬取的贴吧：")
    begin_page = int(input("请输入起始页："))
    end_page = int(input("请输入结束页："))

    url = 'https://tieba.baidu.com/f'
    key_word = urllib.parse.urlencode({'kw': kw})
    url = url + '?' + key_word

    start_download(url, begin_page, end_page)
if __name__ == '__main__':
    main()

