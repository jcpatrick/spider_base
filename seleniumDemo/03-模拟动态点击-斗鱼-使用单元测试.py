from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import unittest
from bs4 import BeautifulSoup

class DouyuSpider(unittest.TestCase):

    # 初始化方法,继承自TestCase
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome("H:\\chromedriver.exe", options=options)

    #具体测试的用例，一定要以test开头
    def testDouyu(self):
        self.driver.get("http://www.douyu.com/directory/all")
        i = 0
        while True:
            i += 1
            print(i)
            #page_source获取页面内容
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            title = soup.find_all("h3", {'class': 'ellipsis'})
            num = soup.find_all("span", {'class': 'dy-num fr'})
            # 使用zip()函数来可以把列表合并，并创建一个元组对的列表[(1,2), (3,4)]

            for title, num in zip(title, num):
                print("房间标题：%s\t观众人数：%s" % (title.get_text().strip(), num.get_text().strip()))

            #如果已经到最后一页了就退出循环
            if soup.find('a', {'class': 'shark-pager-disable-next'}):
                break
            #点击下一页
            self.driver.find_element_by_class_name('shark-pager-next').click()
    #退出时的清理方法，继承自TestCase
    def tearDown(self):
        print('清理结束')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

