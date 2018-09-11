import re

def matchDemo():
    '''match方法只有一次匹配，可以设置开始位置，
        从开始位置匹配，不成功则放回None，
        匹配成功之后，返回match对象'''
    pattern = re.compile(r'\d+')
    match1 = pattern.match('asd123bdf')
    print("123asdb匹配之后match的结果(没有匹配到）：" )
    print(match1)
    print('------------------')
    match2 = pattern.match('123asdb')
    print("123asdb匹配之后match的结果：")
    print(match2)
    print('123asdb匹配数字的结果：' + match2.group())
def searchDemo():
    '''搜索，从目标字符串中匹配，只匹配一次'''
    pattern = re.compile(r'\d+')
    match1 = pattern.search('asd123bdf')
    print(match1)

    #设置了开始匹配位置
    match2 = pattern.search('asd123bdf123', 4)
    print(match2)

def findallDemo():
    '''搜索，从目标字符串中匹配，匹配多次
        返回的是一个list对象'''
    pattern = re.compile(r'\d+')
    match1 = pattern.findall('asd123bdf123123')
    print(match1)

    #设置了开始匹配位置
    pattern2 = re.compile(r'\d+\.\d*')
    match2 = pattern2.findall("123.141593, 'bigcat', 232312, 3.15")
    print(match2)

def finditerDemo():
    '''搜索，从目标字符串中匹配，只匹配一次
        它返回一个顺序访问每一个匹配结果（Match 对象）的迭代器。'''
    pattern = re.compile(r'\d+')
    match1 = pattern.finditer('asd123bdf123123')
    print(type(match1))
    for m1 in match1:
        print('matching string: %s, position: %s'%(m1.group(), m1.span()))
    print('----------')
    #设置了开始匹配位置
    pattern2 = re.compile(r'\d+\.\d*')
    match2 = pattern2.finditer("123.141593, 'bigcat', 232312, 3.15")
    for m2 in match2:
        print('matching string: %s, position: %s' % (m2.group(), m2.span()))

def subDemo():
    '''sub(repl, string[, count])
        sub函数用于替换，repl替换后面string匹配的内容
        参数repl可以是字符串也可以是函数,
        '''
    p = re.compile(r'(\w+) (\w+)')#\w==[A-Za-z0-9]
    s = 'hello 123,world 456'

    match1 = p.sub(r'hello world', s)
    print(match1)

    match2 = p.sub(r'\2 \1', s)
    print(match2)

    def func(m):
        #将hi与匹配正则表达式的第二部分结合，组成替换结果
        return 'hi' + ' ' + m.group(2)
    print(p.sub(func, s))

def ChineseDemo():
    '''返回的是一个list集合'''
    #中文的unicode编码范围为：\u4e00-\u9fa5
    title = u'你好，hello，世界'
    pattern = re.compile(u'[\u4e00-\u9fa5]+')
    result = pattern.findall(title)
    print(result)

def splitDemo():
    '''返回的是一个list集合'''
    pattern = re.compile(r'[\s\,\;]+')
    match = pattern.split('a,b;; c   d')
    print(match)
if __name__ == '__main__':
    # matchDemo()
    # searchDemo()
    # findallDemo()
    # finditerDemo()
    # subDemo()
    # ChineseDemo()
    splitDemo()