from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.wait import WebDriverWait


def doubanLogin():
    options = webdriver.ChromeOptions()
    options.headless = True
    chrome = webdriver.Chrome('H:\\chromedriver.exe', options=options)

    chrome.get("https://www.douban.com/")
    username = input("请输入账号：")
    password = input("请输入密码：")

    chrome.find_element_by_id("form_email").send_keys(username)
    chrome.find_element_by_id("form_password").send_keys(password)
    ac = chrome.find_element_by_id("captcha_image")
    # 将鼠标移动到验证码的位置
    ActionChains(chrome).move_to_element(ac).perform()
    chrome.save_screenshot('captcha.png')
    captcha = input("请输入验证码:")
    chrome.find_element_by_id('captcha_field').send_keys(captcha)

    chrome.find_element_by_xpath('//input[@value="登录豆瓣"]').click()
    chrome.save_screenshot('login_success.png')

    chrome.quit()

def neteaseMailLogin():
    options = webdriver.ChromeOptions()
    # options.headless = True
    chrome = webdriver.Chrome('H:\\chromedriver.exe', options=options)
    chrome.get("https://mail.163.com/")

    ac = chrome.find_element_by_id('lbNormal')
    ActionChains(chrome).move_to_element(ac).perform()
    chrome.save_screenshot('account_login.png')#选择到登陆

    #切换到frame
    iframe = chrome.find_element_by_xpath('//iframe[@id="x-URS-iframe"]')
    chrome.switch_to.frame(iframe)

    chrome.save_screenshot('iframe.png')
    username = input("请输入账号：")
    password = input("请输入密码：")

    chrome.find_element_by_name('email').send_keys(username)
    chrome.find_element_by_name('password').send_keys(password)

    chrome.find_element_by_id('dologin').click()

    time.sleep(2)
    #要等待页面加载完成再关闭，不然无法加载到页面
    chrome.save_screenshot('confirm_login.png')
    #切换回主界面
    # chrome.switch_to.default_content()
    # chrome.save_screenshot('confirm_login.png')
    # chrome.quit()

if __name__ == '__main__':
    # doubanLogin()
    neteaseMailLogin()