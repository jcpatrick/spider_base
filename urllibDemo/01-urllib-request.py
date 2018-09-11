import urllib.request
import random

#通过urllib直接访问目标网站
def main():
    response = urllib.request.urlopen('http://www.baidu.com')
    result = response.read()
    print(result)

def main2():
    url = 'http://www.baidu.com'
    #设置了请求头的访问
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    req = urllib.request.Request(url, headers=header)
    req.add_header('Connection', 'keep-alive')
    hd = req.get_header('Connection', 'None')
    print(hd)
    print('------------------')
    #获取请求头信息
    resp = urllib.request.urlopen(req)
    res = resp.read()
    #获取响应吗和
    code = resp.code
    print('response code:%d' %code)
    print(res)

def main3():
    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
    ]
    url = "http://www.itcast.cn"
    user_agent = random.choice(ua_list)

    request = urllib.request.Request(url)

    request.add_header('User-Agent', user_agent)
    resp = urllib.request.urlopen(request)
    result = resp.read()
    print(result.decode(encoding='utf8'))
    

if __name__ == '__main__':
    # main()
    # main2()
    main3()