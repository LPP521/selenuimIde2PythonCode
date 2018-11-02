def json2code(jsonDict):

    print("json字符串转化成 字典对象--:  ", jsonDict)
    print("项目名称--:  @", jsonDict['name'])
    print("tests的名称--:  @", jsonDict['tests'][0]['name'])
    print("tests的全部操作，需要遍历，根据command命令类型转化为不同的操作--:  ", jsonDict['tests'][0]['commands'])
    print("其中一个操作--:  ", jsonDict['tests'][0]['commands'][2])




    return str(jsonDict['tests'][0]['commands'][2])