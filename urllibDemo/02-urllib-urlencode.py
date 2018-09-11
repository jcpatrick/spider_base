import urllib.request
import urllib.parse

def main():
    '''使用urlencode将dict（字典）转成url编码格式'''
    url = 'http://www.baidu.com/s'
    request_params = {'wd':'胡歌 刘亦菲'}
    #将请求参数转成url编码格式
    request_params = urllib.parse.urlencode(request_params)
    print(request_params)#url中的+号或者是%20表示空格

    #将url编码格式字符串转回会utf-8格式字符串
    # utfcode = urllib.parse.unquote(request_params)
    # print(utfcode)

    url = url + '?' +request_params
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request = urllib.request.Request(url, headers= headers)

    # request.add_header(header)

    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    print(result)

if __name__ == '__main__':
    main()