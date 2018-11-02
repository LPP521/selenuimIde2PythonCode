
import os
import jsonReader
import jsonDict2pythonCode

jsonDirectory="IDE_Json脚本"
pythonDirectory="Python代码"

for root, dirs, files in os.walk(jsonDirectory, topdown=False):
    print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录（文件夹）
    print(files) #当前路径下所有非目录子文件（不是文件夹的东西）

    #遍历文件夹下面的多个脚本
    for jsonFile in files:


        # json字符串转化成 字典对象
        jsonFilePath=root+"\\"+jsonFile
        print(jsonFilePath)
        jsonDict = jsonReader.json2dict(jsonFilePath)


        # 字典转化为python的脚本代码
        #pyCode = "print('字典转化为python的脚本代码')"
        pyCode = jsonDict2pythonCode.json2code(jsonDict)

        #创建同名的py文件
        pythonFilePath=pythonDirectory+"\\"+os.path.splitext(jsonFile)[0]+".py"
        with open(pythonFilePath, 'w', encoding='UTF-8') as pythonFile:
            pythonFile.write(pyCode)







