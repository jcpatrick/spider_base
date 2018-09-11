from lxml import etree

if __name__ == '__main__':
    html = etree.parse('hello.html')
    result = etree.tostring(html, pretty_print=True)
    print(result.decode('utf-8'))