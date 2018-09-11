from lxml import etree

if __name__ == '__main__':
    html = etree.parse('hello.html')
    print(html)
    #获取li标签下面的内容
    result = html.xpath('//li')

    print(len(result))
    print(type(result))

    print("----------------------")
    #获取li标签class属性的值
    result = html.xpath('//li/@class')
    print(result)

    print("----------------------")
    #获取li下面属性href为link1.html的a标签
    result = html.xpath('//li/a[@href="link1.html"]')
    print(result)

    print("----------------------")
    #获取li标签下面的所有span
    result = html.xpath("//li//span")
    print(result)

    print("----------------------")
    #获取 <li> 标签下的<a>标签里的所有 class
    result = html.xpath('//li/a//@class')
    print(result)

    print("----------------------")
    # 获取最后一个 < li > 的 < a > 的href
    result = html.xpath('//li[last()]/a//@href')
    print(result)

    print("----------------------")
    # 获取倒数第二个元素的内容
    result = html.xpath('//li[last()-1]/a')
    print(result[0].text)

    print("----------------------")
    # 获取 class 值为 bold 的标签名
    result = html.xpath('//*[@class="bold"]')
    print(result[0].tag)
