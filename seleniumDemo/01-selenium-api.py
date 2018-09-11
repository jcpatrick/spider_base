# 导入 webdriver
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
def PhantomJS_Demo():
    '''这个对象已经过时了'''
    driver = webdriver.PhantomJS('C:\\Users\\cong\\Desktop\\python笔记\\爬虫\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs')

    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("http://www.baidu.com/")

    # 获取页面名为 wrapper的id标签的文本内容
    data = driver.find_element_by_id("wrapper").text
    print(data)

def Chrome_Demo():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')#开启无界面模式
    # chrome_options.add_argument('--disable-gpu')
    chrome = webdriver.Chrome("H:\\chromedriver.exe", options=chrome_options)
    chrome.get('http://www.baidu.com')

    data = chrome.find_element_by_id("wrapper").text
    print(data)

    print(chrome.title)#答应html中的title

    #截图
    chrome.save_screenshot("baidu.png")

    # 向搜索框中输入内容
    chrome.find_element_by_id("kw").send_keys("长城")

    # 点击查找按钮
    chrome.find_element_by_id('su').click()

    chrome.save_screenshot("长城.png")

    # 打印网页渲染后的源代码
    print(chrome.page_source)

    # 获取当前页面Cookie
    print(chrome.get_cookies())

    #ctrl+a全选输入框中的内容
    chrome.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

    # ctrl+x 剪切输入框内容
    chrome.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

    # 输入框重新输入内容
    chrome.find_element_by_id("kw").send_keys("itcast")

    # 模拟Enter回车键
    chrome.find_element_by_id("su").send_keys(Keys.RETURN)

    # 清除输入框内容
    chrome.find_element_by_id("kw").clear()

    # 生成新的页面快照
    chrome.save_screenshot("itcast.png")

    #获取当前的url
    print(chrome.current_url)

    # 关闭当前页面，如果只有一个页面，会关闭浏览器
    # chrome.close()

    # 关闭浏览器
    # chrome.quit()

def locatedWebElements():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome('H:\\chromedriver.exe', options=options)
    driver.get('http://www.baidu.com')
    # 获取id标签值
    try:
        element = driver.find_element_by_id("passwd-id")
    except:
        pass
    # 获取name标签值
    try:
        element = driver.find_element_by_name("user-name")
    except:
        pass
    # 获取标签名值
    element = driver.find_elements_by_tag_name("input")
    # 也可以通过XPath来匹配
    element = driver.find_element_by_xpath("//input[@id='passwd-id']")
if __name__ == '__main__':
    # PhantomJS_Demo()
    # Chrome_Demo()
    locatedWebElements()