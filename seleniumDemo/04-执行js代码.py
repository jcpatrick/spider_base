from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome("H:\\chromedriver.exe", options=options)

driver.get('http://www.baidu.com')
# 调用给搜索输入框标红js脚本
js = 'var kw = document.getElementById("kw"); kw.style.border="2px solid red";'
driver.execute_script(js)
driver.save_screenshot('redbox.png')

#js隐藏元素，将获取的图片元素隐藏

img = driver.find_element_by_xpath("//*[@id='lg']/img")
driver.execute_script('$(arguments[0]).fadeOut()',img)

# 向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

#查看页面快照
driver.save_screenshot("nullbaidu.png")

driver.quit()