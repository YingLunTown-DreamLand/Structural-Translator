import sys
sys.path.append(".")
from Api.ParseBDX.main import ParseBDX
import os, json
# 载入依赖项





searchPath = "Api/ParseBDX"    # 从哪个路径搜索 BDX 文件
outputPath = 'Api/ParseBDX/Output'    # 在哪里输出 JSON 文件




searchPath = os.path.normpath(searchPath).replace('\\','/')
outputPath = os.path.normpath(outputPath).replace('\\','/')
# 格式化处理





filePath = []
for root,dirs,files in os.walk(searchPath):
    for fileName in files:
        String = os.path.normpath(os.path.join(root,fileName)).replace('\\','/').split('/')
        String[-1] = String[-1].split('.')
        if len(String[-1]) > 0:
            String[-1][-1] = String[-1][-1].replace('B','b').replace('D','d').replace('X','x')
        String[-1] = ".".join(String[-1])
        if os.path.splitext(String[-1])[-1] == '.bdx':
            filePath.append("/".join(String))
print(f'A total of {len(filePath)} files were found.')
# 找到 searchPath 下的所有 BDX 文件





logList = {}
for i in filePath:
    Parse = ParseBDX(i)
    try:
        Parse.main()
    except:
        logList[i] = {
            "inputPath": i,    # 文件输入路径
            "blockNBT_find_out": None,    # 找到的可以被解析为 str 的 operation 39
            "blockNBT_error": None,    # 找到的无法被解析为 str 的 operation 39
            "authorName": None,    # 作者名称
            "file_is_integrity": False    # 文件是否完整
        }
        print(f'Failed to parse "{i}", and it maybe not a correct BDX file.')
        continue
    # 解析文件

    mkdirPath = os.path.normpath(os.path.join(outputPath,i.replace(searchPath + '/','',1))).replace('\\','/').split('/')
    del mkdirPath[-1]
    mkdirPath = "/".join(mkdirPath)
    # 确定文件夹创建路径

    if not os.path.exists(mkdirPath):
        os.makedirs(mkdirPath)
    # 创建文件夹，若对应的文件夹不存在的话

    outputLocation = os.path.normpath(os.path.join(outputPath,i.replace(searchPath + '/','',1) + '.json')).replace('\\','/')
    with open(outputLocation,"w+",encoding='utf-8') as file:
        file.write(json.dumps(Parse.resultList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
    # 写入到文件

    logList[i] = Parse.logList
    # 写入日志

    print(f'"{i}" have been finished, saved in "{outputLocation}" .')
# 解析对应的文件





if not os.path.exists(outputPath):
    os.makedirs(outputPath)
# 创建文件夹，若对应的文件夹不存在的话

logOutputLocation = os.path.normpath(os.path.join(outputPath,'ParseBDX_log.json')).replace('\\','/')

with open(logOutputLocation,"w+",encoding='utf-8') as file:
    file.write(json.dumps(logList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
    print(f'Log files has beed wrote, saved in "{logOutputLocation}" .')
# 生成日志