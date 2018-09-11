import urllib.request
import urllib.parse

def demo1():
    '''Ajax传url参数+form参数'''
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
    headers = {'User-Agent': 'Mozilla/5.0 ....'}
    data = {
        'start': '0',
        'limit': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')#注意要进行编码
    request = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    print(result)

def demo2():
    url = "https://movie.douban.com/j/chart/top_list?"
    headers = {"User-Agent": "Mozilla...."}
    formdata = {
        'type': '11',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '10'
    }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    request = urllib.request.Request(url, data= data, headers=headers)
    response  =urllib.request.urlopen(request)
    result = response.read().decode(encoding='utf-8')
    print(result)

if __name__ == '__main__':
    # demo1()
    demo2()