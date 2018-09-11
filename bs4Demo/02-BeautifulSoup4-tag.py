from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 查找的是在所有内容中的第一个符合要求的标签。都是取标签内的属性
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


    #tag
    soup = BeautifulSoup(html, 'lxml')

    print(soup.title)

    print(soup.head)

    print(soup.a)

    print(soup.p)

    print(type(soup.p))

    #name
    print(soup.name)

    print(soup.head.name)

    print(soup.title.name)

    print(soup.p.attrs)#获取p标签的属性key-value

    print(soup.p['class'])#还可以利用get方法，传入属性的名称，二者是等价的
    print(soup.p.get('class'))

    soup.p['class']="newClass"
    print(soup.p)

    del soup.p['class']
    print(soup.p)