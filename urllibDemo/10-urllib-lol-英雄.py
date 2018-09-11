import urllib.request
import urllib.parse
import urllib.error
import re

class LOL(object):
    def __init__(self):
        # self.baseURL = 'http://lol.qq.com/web201310/info-defail.shtml?'
        #英雄信息的js
        self.allHeroURL = 'http://lol.qq.com/biz/hero/champion.js'
        self.heroBaseURL = 'http://lol.qq.com/biz/hero/'
        self.heroIdList = {}

    def requestHelper(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 68.0.3440.84 Safari / 537.36'
            }
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read()
        except urllib.error.HTTPError:
            content = ''

        return content
    def loadAllHeroURL(self):
        '''获取英雄的名称列表'''


        #切换js，把它切成json字符串去掉第二个=号前面的和最后一个;号
        content = self.requestHelper(self.allHeroURL)
        # 获取数据的字符集，然后解码
        from pip._vendor import chardet
        encoding = chardet.detect(content)['encoding']
        print(encoding)
        content = content.decode(encoding=encoding)
        chapionListData = content.split('=')[2][:-1]
        data = eval(chapionListData)
        heroNameList = data['keys']
        heroDescri = str(data['data'])#英雄的详细名称和图片
        self.version = data['version']
        self.updated = data['updated']
        #将英雄名称加入url中
        ifFirst = True
        for key,value in heroNameList.items():
            # print('%s----%s'%(key, value))
            #通过正则表达式取出中文名和称谓
            pattern = re.compile(key+r'[\s\S]*?\'name\': \'(.*?)\'[\s\S]*?\'title\': \'(.*?)\'', re.S)
            match = pattern.findall(heroDescri)
            name = match[0][0] + "-" + match[0][1]
            self.heroIdList[value] = name

    def loadHeroDetail(self):
        isFirst = True
        for heroid, heroName in self.heroIdList.items():

            url = self.heroBaseURL + heroid + '.js'
            print(heroName+url)
            content = self.requestHelper(url)
            content = content.decode('unicode_escape')#直接将ascill的字节字符串解码，这样中文就能显示了
            print(content)
            #注意content是个js的对象，而不是JSON数组
            # hero = content.split(";")[1]
            # heroData = eval(hero)
            # 使用正则表达式解析
            # pattern = re.compile(r'"(lore|blurb|allytips|enemytips)":(.*?),', re.S)
            #获得背景故事
            pattern = re.compile(r'"(lore)":(.*?),', re.S)
            match = pattern.findall(content)
            #获取背景故事
            lore = match[0][1]
            lore = lore.replace('<br>', "\n")
            # print(lore)

            #写文件的时候，指定编码
            f = open('hero/' + heroName + '.txt', 'w', encoding='utf-8')
            f.write(heroName +"\n")
            f.writelines(lore + "\n")
            #获得技能描述
            pattern2 = re.compile(r'(Q|W|E|R)","name":"(.*?)","description":"(.*?)"[\s\S]*?"tooltip":"(.*?)"', re.S)
            match2 = pattern2.findall(content)
            for sName,sNameCn,sDesc,sDemage in match2:
                content = "%s(%s)\n%s\n%s\n"%(sName,sNameCn,sDesc,sDemage.replace('\\',''))
                f.write(content)
            f.close()

if __name__ == '__main__':
    lol = LOL()
    lol.loadAllHeroURL()
    lol.loadHeroDetail()
    # lol.loadChampionDetails()