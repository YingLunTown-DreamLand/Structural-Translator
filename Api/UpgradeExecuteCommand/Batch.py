import sys
sys.path.append(".")
from Api.UpgradeExecuteCommand.main import UpgradeExecuteCommand
import os, json
# 载入依赖项





searchPath = "Api/UpgradeExecuteCommand"    # 从哪个路径搜索 JSON 文件
outputPath = 'Api/UpgradeExecuteCommand/Output'    # 在哪里输出 JSON 文件




searchPath = os.path.normpath(searchPath)
outputPath = os.path.normpath(outputPath)
# 格式化处理





filePath = []
for root,dirs,files in os.walk(searchPath):
    for fileName in files:
        String = os.path.normpath(os.path.join(root,fileName)).split('\\')
        String[-1] = String[-1].split('.')
        if len(String[-1]) > 0:
            String[-1][-1].replace('J','j').replace('S','s').replace('O','o').replace('N','n')
        String[-1] = ".".join(String[-1])
        if os.path.splitext(String[-1])[-1] == '.json' and String[-1] != 'UpgradeExecuteCommand_log.json':
            filePath.append("\\".join(String))
print(f'A total of {len(filePath)} files were found.')
# 找到 searchPath 下的所有 BDX 文件





logList = {}
for i in filePath:
    Upgrade = UpgradeExecuteCommand(i)
    try:
        Upgrade.main()
    except:
        print(f'Failed to parse "{i}" ,and it maybe not a correct JSON file.')
        continue
    # 解析文件

    mkdirPath = os.path.normpath(os.path.join(outputPath,i.replace(searchPath + '\\','',1))).split('\\')
    del mkdirPath[-1]
    mkdirPath = "\\".join(mkdirPath)
    # 确定文件夹创建路径

    if not os.path.exists(mkdirPath):
        os.makedirs(mkdirPath)
    # 创建文件夹，若对应的文件夹不存在的话

    outputLocation = os.path.normpath(os.path.join(outputPath,i.replace(searchPath + '\\','',1)))
    with open(outputLocation,"w+",encoding='utf-8') as file:
        file.write(json.dumps(Upgrade.resultList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
    # 写入到文件

    logList[i] = (Upgrade.logList)
    # 写入日志

    print(f'"{i}" have been finished, saved in "{outputLocation}" .')
# 解析对应的文件





if not os.path.exists(outputPath):
    os.makedirs(outputPath)
# 创建文件夹，若对应的文件夹不存在的话

logOutputLocation = os.path.normpath(os.path.join(outputPath,'UpgradeExecuteCommand_log.json'))

with open(logOutputLocation,"w+",encoding='utf-8') as file:
    file.write(json.dumps(logList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
    print(f'Log files has beed wrote, saved in "{logOutputLocation}" .')
# 生成日志