import json
def json2dict(jsonFilePath):
    with open(jsonFilePath, 'r', encoding='UTF-8') as jsonFile:
        jsonDict = json.load(jsonFile, strict=False)  # strict=False 不标准的json也能识别
    return jsonDict
