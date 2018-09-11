import urllib.request
import urllib.parse
import ssl
def httpsErrorDemo():
    '''直接报错'''
    url = "https://www.12306.cn/mormhweb/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    print(response.read())

def httpsSSLDemo():
    '''直接报错'''
    url = "https://www.12306.cn/mormhweb/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    context = ssl._create_unverified_context()
    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request, context=context)

    print(response.read().decode('utf-8'))

if __name__ == '__main__':
    # httpsErrorDemo()
    httpsSSLDemo()