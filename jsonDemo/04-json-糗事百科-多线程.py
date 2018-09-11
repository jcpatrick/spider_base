from threading import Thread,Lock
from queue import Queue
import time
import json
from lxml import etree
import requests
import chardet

class CatchThread(Thread):
    def __init__(self, thread_id, queue):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        print('Starting:' + self.thread_id)
        self.spider()
        print('Finishing:' + self.thread_id)
    def spider(self):

        while True:
            if self.queue.empty():
                break
            else:
                page = self.queue.get()
                url = 'https://www.qiushibaike.com/8hr/page/' + str(page) + "/"

                headers = {
                    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
                    'Host': 'www.qiushibaike.com',
                    'Upgrade-Insecure-Requests': '1'
                }
                if page > 1:
                    headers['Referer'] = 'https://www.qiushibaike.com/8hr/page/' + str(page - 1) + "/"
                #设置重连机制
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        proxys={
                            'http':'61.135.217.7:80',
                            'http':'174.120.70.232:80',
                            'http':'177.137.20.55:80',
                        }
                        response = requests.get(url, headers=headers, proxies=proxys)
                        if response.status_code == 200:
                            response.encoding = 'utf-8'
                            data = response.text

                            DATA_QUEUE.put(data)
                            time.sleep(0.2)
                            break
                    except Exception as e:
                        print("-----"+e)
                if timeout < 0:
                    print('timeout:' + url)

class ParserThread(Thread):
    def __init__(self, thread_id, queue, l, f):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.lock = l
        self.f = f

    def run(self):
        print('starting parse:' + self.thread_id)
        global EXIT_PARSER_TAG
        while not EXIT_PARSER_TAG:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                data = self.queue.get(False)
                if not data:
                    pass
                self.parse_data(data)
                self.queue.task_done()
            except:
                pass
        print('exiting:' + self.thread_id)

    def parse_data(self, data):
        global TOTAL, COUNT
        try:
            html = etree.HTML(data)
            articles = html.xpath('//div[contains(@id,"qiushi_tag")]')
            for article in articles:
                try:
                    image = article.xpath('.//img/@src')[0]
                    author = article.xpath('.//h2')[0].text.strip()
                    content = article.xpath('.//div[@class="content"]/span')[0].text.strip()
                    vote = None
                    comments = None
                    try:
                        vote = article.xpath('.//i')[0].text
                        comments = article.xpath('.//i')[1].text
                    except:
                        pass
                    item = {
                        'images': image,
                        'author': author,
                        'content': content,
                        'vote': vote,
                        'comments': comments
                    }
                    with self.lock:
                        self.f.write(json.dumps(item, ensure_ascii=False) + '\n')
                except:
                    pass
            # for site in articles:
            #     try:
            #         imgUrl = site.xpath('.//img/@src')[0]
            #         title = site.xpath('.//h2')[0].text
            #         content = site.xpath('.//div[@class="content"]/span')[0].text.strip()
            #         vote = None
            #         comments = None
            #         try:
            #             vote = site.xpath('.//i')[0].text
            #             comments = site.xpath('.//i')[1].text
            #         except:
            #             pass
            #         result = {
            #             'imgUrl': imgUrl,
            #             'title': title,
            #             'content': content,
            #             'vote': vote,
            #             'comments': comments,
            #         }
            #
            #         with self.lock:
            #             # print 'write %s' % json.dumps(result)
            #             self.f.write(json.dumps(result, ensure_ascii=False) + "\n")
            #
            #     except Exception as e:
            #         print('site in result', e)
        except Exception as e:
            print("parse_data---"+e)
        with self.lock:
            TOTAL += 1


DATA_QUEUE = Queue()
EXIT_PARSER_TAG = False
TOTAL = 0
LOCK = Lock()
COUNT = 0
def main():
    output = open('qiushi-thread.json', 'w', encoding='utf-8')

    page_queue = Queue(50)

    for page in range(1, 11):
        page_queue.put(page)

    catchThreads = []
    catchIDList = ['catch-1', 'catch-2', 'catch-3']
    for thread_id in catchIDList:
        thread = CatchThread(thread_id, page_queue)
        thread.start()
        catchThreads.append(thread)

    parseThreads = []
    parseIDList = ['parse-1', 'parse-2', 'parse-3']
    for thread_id in parseIDList:
        thread = ParserThread(thread_id, DATA_QUEUE, LOCK, output)
        thread.start()
        parseThreads.append(thread)

    #等待抓取页面的任务全部被消费
    while not page_queue.empty():
        pass

    #等待抓取线程完成
    for t in catchThreads:
        t.join()

    #等待解析任务全部被消费
    while not DATA_QUEUE.empty():
        pass

    #设置结束解析线程循环标记
    global EXIT_PARSER_TAG
    EXIT_PARSER_TAG = True

    #等下解析线程结束
    for t in parseThreads:
        t.join()

    #关闭文件输出流
    with LOCK:
        output.close()
    print(str(COUNT))

if __name__ == '__main__':
    main()