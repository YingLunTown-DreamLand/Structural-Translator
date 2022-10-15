import sys
sys.path.append(".")
import json
import Api.UpgradeExecuteCommand.translateCommand
# 载入依赖项



inputPath = 'Api/UpgradeExecuteCommand/input.json'
outputPath = 'Api/UpgradeExecuteCommand/ans.json'
logPath = 'Api/UpgradeExecuteCommand/Upgrade.log'
# 确定输入文件、输出文件及日志文件的路径



with open(inputPath,'r+',encoding='utf-8') as file:
    WhiteWallJson = json.load(file)
# 读入 WhiteWallJson 文件



successStatesList = []
# 初始化成功及失败列表



for i in range(len(WhiteWallJson)):
    if 'cmddata' in WhiteWallJson[i]:
        if 'command' in WhiteWallJson[i]['cmddata']:
            try:
                ans = Api.UpgradeExecuteCommand.translateCommand.run(
                    WhiteWallJson[i]['cmddata']['command']
                    )
                if ans != WhiteWallJson[i]['cmddata']['command']:
                    successStatesList.append(
                        [
                            'SUCCESS',
                            WhiteWallJson[i]['cmddata']['command'],
                            ans
                        ]
                    )
                WhiteWallJson[i]['cmddata']['command'] = ans
            except:
                successStatesList.append(
                    [
                        'UNSUCCESS',
                        WhiteWallJson[i]['cmddata']['command']
                    ]
                )
# 升级 execute 语法



with open(outputPath,'w+',encoding='utf-8') as file:
    file.write(json.dumps(WhiteWallJson,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
# 输出文件



with open(logPath,'w+',encoding='utf-8') as file:
    for i in successStatesList:
        file.write(str(i)+'\n')
# 输出日志



print(f'LogFile - 日志文件已成功生成，保存在 {logPath} 下.')
print(f'UpgradeDown - 已成功升级目标文件中的 Execute 命令，存在在 {outputPath} 下.')
# 打印提示