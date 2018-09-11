import urllib.request
import urllib.parse
import http.cookiejar
def CookieSample():
    # 1. 构建一个已经登录过的用户的headers信息
    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",

        # 便于终端阅读，表示不支持压缩文件
        # Accept-Encoding: gzip, deflate, sdch,

        # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
        #这个cookie已经过期了
        "Cookie": "anonymid=ixrna3fysufnwv; depovince=GW; _r01_=1; JSESSIONID=abcmaDhEdqIlM7riy5iMv; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484060607173; jebecookies=26fb58d1-cbe7-4fc3-a4ad-592233d1b42e|||||; ick_login=1f2b895d-34c7-4a1d-afb7-d84666fad409; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=99e54330ba9f910b02e6b08058f780479; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=214ca9a28f70ca6aa0801404dda4f6789; societyguester=214ca9a28f70ca6aa0801404dda4f6789; id=327550029; xnsid=745033c5; ver=7.0; loginfrom=syshome"
    }

    # 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
    request= urllib.request.Request("http://www.renren.com/", headers=headers)

    # 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
    response = urllib.request.urlopen(request)

    # 4. 打印响应内容
    print(response.read())

def CookieJarDemo():
    # 构建一个CookieJar对象实例来保存cookie
    cookiejar = http.cookiejar.CookieJar()
    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    handler = urllib.request.HTTPCookieProcessor(cookiejar)
    # 通过 build_opener() 来构建opener
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)
    # 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中
    response = urllib.request.urlopen('http://www.baidu.com')
    ## 可以按标准格式将保存的Cookie打印出来
    # print(response.read())

    # 打印cookiejar中的cookie
    cookieStr = ''
    for item in  cookiejar:
        cookieStr = cookieStr + item.name + '=' + item.value + ';\n'
    print(cookieStr)
def SaveCookieToFileDemo():
    #创建保存cookie的文件名
    filename = 'cookie.txt'
    #创建MozillaCookirJar，这个类是可以将cookie写到文件的
    cookiejar = http.cookiejar.MozillaCookieJar()
    #创建handler
    handler = urllib.request.HTTPCookieProcessor(cookiejar)

    opener = urllib.request.build_opener(handler)

    response = opener.open('http://www.baidu.com')

    cookiejar.save(filename)

def LoadCookieFromFileDemo():
    filename = 'cookie.txt'
    cookiejar = http.cookiejar.MozillaCookieJar(filename)
    cookiejar.load(filename, ignore_discard=True,ignore_expires=True)

    handler = urllib.request.HTTPCookieProcessor(cookiejar)

    opener = urllib.request.build_opener(handler)

    response = opener.open('http://www.baidu.com')
    print(response.read())
    print(cookiejar)

def CookieAndPasswordLoginDemo():
    cookiejar = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(handler)
    #addheaders接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
    opener.addheaders = [
        ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
    ]

    data = {"email": "mr_mao_hacker@163.com", "password": "alaxxxxxime"}
    postdata = urllib.parse.urlencode(data)
    request = urllib.request.Request("http://www.renren.com/PLogin.do", data=postdata.encode('utf-8'))
    #先登录，然后获取cookie
    opener.open(request)
    #opener包含了cookie信息，然后再访问其他需要登录才能访问的页面
    response =opener.open("http://www.renren.com/410043129/profile")
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    # CookieSample()
    # CookieJarDemo()
    # SaveCookieToFileDemo()
    # LoadCookieFromFileDemo()
    CookieAndPasswordLoginDemo()