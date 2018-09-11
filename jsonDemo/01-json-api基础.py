import json

def loadFunc():
    strList = '[1, 2, 3, 4]'

    strDict = '{"city": "北京", "name": "大猫"}'

    print(json.loads(strList))
    # [1, 2, 3, 4]

    print(json.loads(strDict)) # json数据自动按Unicode存储

def dumpsFunc():
    listStr = [1, 2, 3, 4]
    tupleStr = (1, 2, 3, 4)
    dictStr = {"city": "北京", "name": "大猫"}

    print(json.dumps(listStr))
    print(json.dumps(tupleStr))

    # 注意：json.dumps() 序列化时默认使用的ascii编码
    # 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
    # chardet.detect()返回字典, 其中confidence是检测精确度
    print(json.dumps(dictStr))
    print(json.dumps(dictStr, ensure_ascii=False))

def dumpFunc():
    '''将json写到文件中'''
    listStr = [{"city": "北京"}, {"name": "大刘"}]
    json.dump(listStr, open("listStr.json", "w"), ensure_ascii=False)

    dictStr = {"city": "北京", "name": "大刘"}
    json.dump(dictStr, open("dictStr.json", "w"), ensure_ascii=False)
if __name__ == '__main__':
    # loadFunc()
    dumpsFunc()
    dumpFunc()