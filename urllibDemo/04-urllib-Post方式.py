import urllib.request
import urllib.parse
import time
import random
import hashlib
def get_salt():
    salt = int(time.time() * 1000) + random.randint(0,10)
    return str(salt)
def get_sign(data, salt):
    md5 = hashlib.md5()
    md5.update(("fanyideskweb" + data + salt + "ebSeFb%=XZ%T[KZ)c(sy!").encode('utf-8'))
    return md5.hexdigest()
def main():

    #无反爬虫的编码，少了个translate后面少了个_o
    # url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID = -1817391905@10.169.0.84;',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0',
        # 'Accept-Encoding': 'gzip, deflate',#爬虫不要写，不然就需要对结果进行gzip解压
    }
    data = '你在干什么啊'
    salt = get_salt()
    sign = get_sign(data, salt)
    print(sign)
    formData = {
        'i': data,
        'salt': salt,
        'sign': sign,
        'smartresult': 'dict',
        'form': 'AUTO',
        'to': 'AUTO',
        'doctype': 'json',
        'version': '2.1',
        "keyfrom": "fanyi.web",
        'action': 'FY_BY_CLICKBUTTION',
        'client': 'fanyideskweb',
        'typoResult': 'true'
    }

    #Post的数据，转成url编码之后，还需要转成byte类型
    data = urllib.parse.urlencode(formData).encode(encoding='utf-8')
    request = urllib.request.Request(url=url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    # 获取结果的编码格式
    # from pip._vendor import chardet
    # codeing = chardet.detect(result)
    # print(codeing)
    print(result)
    
if __name__ == '__main__':
    main()
