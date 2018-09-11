import urllib.request

def HttpHandlerDemo():
    http_handler = urllib.request.HTTPHandler()
    # 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
    # http_handler = urllib.request.HTTPSHandler()

    # 构建一个HTTPHandler 处理器对象，支持处理HTTP请求，同时开启Debug Log，debuglevel 值默认 0
    # http_handler = urllib.request.HTTPHandler(debuglevel=1)

    # 构建一个HTTPHSandler 处理器对象，支持处理HTTPS请求，同时开启Debug Log，debuglevel 值默认 0
    # https_handler = urllib.request.HTTPSHandler(debuglevel=1)

    opener = urllib.request.build_opener(http_handler)

    request = urllib.request.Request('http://www.baidu.com')

    resposne = opener.open(request)

    print(resposne.read())

def ProxyHandlerDemo():
    #可以使用列表，从中随机选一个
    # proxy_list = [
    #     {"http": "124.88.67.81:80"},
    #     {"http": "124.88.67.81:80"},
    #     {"http": "124.88.67.81:80"},
    #     {"http": "124.88.67.81:80"},
    #     {"http": "124.88.67.81:80"}
    # ]

    proxy_handler = urllib.request.ProxyHandler({"http" : "61.135.217.7:80"})

    null_proxy_handelr = urllib.request.ProxyHandler({})

    proxySwitch = True

    if proxySwitch:
        opener = urllib.request.build_opener(proxy_handler)
    else:
        opener = urllib.request.build_opener(null_proxy_handelr)

    request = urllib.request.Request('http://www.baidu.com')

    # 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，
    # 而urlopen()则不使用自定义代理。
    response = opener.open(request)

    # 2. 如果这么写，就是将opener应用到全局，之后所有的，
    # 不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # urllib.request.install_opener(opener)
    # response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))

def PasswordRealmProxyAuthHandler():
    '''密码管理器'''
    # 验证代理授权的用户名和密码(ProxyBasicAuthHandler())
    # 验证Web客户端的的用户名和密码(HTTPBasicAuthHandler())

    # 私密代理授权的账户
    user = "mr_mao_hacker"
    # 私密代理授权的密码
    passwd = "sffqry9r"
    # 私密代理 IP
    proxyserver = "61.158.163.130:16816"

    # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
    passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
    passwdmgr.add_password(None, proxyserver, user, passwd)

    # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
    #   注意，这里不再使用普通ProxyHandler类了
    proxyauth_handler = urllib.request.ProxyBasicAuthHandler(passwdmgr)
    #方法二
    # proxyauth_handler = urllib.request.ProxyBasicAuthHandler({'http': '用户名:密码@ip地址'})

    # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler

    opener = urllib.request.build_opener(proxyauth_handler)

    # 5. 构造Request 请求
    request = urllib.request.Request("http://www.baidu.com/")

    # 6. 使用自定义opener发送请求
    response = opener.open(request)

    # 7. 打印响应内容
    print(response.read().decode('utf-8'))

def PasswordRealmWebAuthHandler():
    # 用户名
    user = "test"
    # 密码
    passwd = "123456"
    # Web服务器 IP
    webserver = "http://192.168.1.13"

    passwdmgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    passwdmgr.add_password(None, webserver, user, passwd)
    handler = urllib.request.HTTPBasicAuthHandler(passwdmgr)
    opener = urllib.request.build_opener((handler))
    # 5. 可以选择通过install_opener()方法定义opener为全局opener
    urllib.request.install_opener(opener)
    request = urllib.request.Request('http://192.168.1.13:8000')

    # resposne = opener.open(request)
    resposne = urllib.request.urlopen(request)
    print(resposne.read().decode('utf-8'))


if __name__ == '__main__':
    # HttpHandlerDemo()
    # ProxyHandlerDemo()
    # PasswordRealmProxyAuthHandler()
    PasswordRealmWebAuthHandler()