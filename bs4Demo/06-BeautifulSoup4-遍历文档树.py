from bs4 import BeautifulSoup

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

print(soup.head.contents)#将tag的子节点以列表的方式输出

print(soup.head.contents[0])#用列表索引来获取它的某一个元素

print(soup.head.children)#一个子节点list生成器对象

for child in soup.body.children:#遍历子节点list生成器对象
    print(child)

for child in soup.descendants:#对所有tag的子孙节点进行递归循环
    print(child)

#如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
print(soup.head.string)
print(soup.title.string)