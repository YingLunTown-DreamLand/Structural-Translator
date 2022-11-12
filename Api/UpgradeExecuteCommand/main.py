import sys
sys.path.append(".")
import json
import Api.UpgradeExecuteCommand.translateCommand
# 载入依赖项







class UpgradeExecuteCommand:
    def __init__(self,inputPath:str) -> None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `WhiteWallJson` 文件的输入路径
        """
        # 函数声明

        self.inputPath = inputPath
        self.resultList = {}
        self.logList = []

    # 实例化





    def main(self) -> None:
        """
        \n摘要
        本函数是 `class: UpgradeExecuteCommand` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)，但转义得到的 `字典` 和有关日志会分别储存在 `self.resultList` 和 `self.logList` 中。
        """
        # 函数声明



        with open(self.inputPath,'r+',encoding='utf-8') as file:
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



        self.resultList = WhiteWallJson
        # 输出文件
        self.logList = successStatesList
        # 输出日志








inputPath = 'Api/UpgradeExecuteCommand/input.json'
outputPath = 'Api/UpgradeExecuteCommand/ans.json'
logPath = 'Api/UpgradeExecuteCommand/Upgrade.log'
# 确定输入文件、输出文件及日志文件的路径