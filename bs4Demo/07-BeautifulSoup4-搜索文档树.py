from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')

#find_all(name, attrs, recursive, text, **kwargs)

#A.传字符串
print(soup.find('b'))#查找文档中所有的<b>标签:
print(soup.find_all('a'))

#B.传正则表达式
#找出所有以b开头的标签
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

#C.传列表
print(soup.find_all(["a", "b"]))#找出文档中的所有a标签和b标签

#2）keyword 参数
print(soup.find_all(id='link2'))#传入键值对参数，找到好友该key-value的标签

#3）text 参数
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))