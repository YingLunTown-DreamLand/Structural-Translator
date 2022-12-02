from math import sin, cos, pi
import json, random
# 载入依赖项





class ModelRotation:
    def __init__(
        self,
        inputPath:str,
        randomSelect:bool = True,
        xBot:int|float = 0.0,
        yBot:int|float = 0.0,
        xSkewing:int|float = 0,
        ySkewing:int|float = 0,
        zSkewing:int|float = 0
    ) -> None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `WhiteWallJson` 文件所在路径
        `randomSelect:bool` 指的是在旋转后，若同一个位置出现了多个方块，则是否从中随机取一个作为最终方块(随机方法服从均匀分布)
           # 此参数默认为 `True`
        `xBot:int|float` 指的是竖直方向上的旋转角度(角度制)
           # 此参数默认为 `0.0`
        `yBot:int|float` 指的是水平方向上的旋转角度(角度制)
           # 此参数默认为 `0.0`
        `xSkewing:int|float` 指的是原始建筑在相对坐标系下的 `x轴` 偏移量
           # 此参数默认为 `0`
        `ySkewing:int|float` 指的是原始建筑在相对坐标系下的 `y轴` 偏移量
           # 此参数默认为 `0`
        `zSkewing:int|float` 指的是原始建筑在相对坐标系下的 `z轴` 偏移量
           # 此参数默认为 `0`
        \n使用说明
        本功能的原理是将原本文件中各个方块的坐标按照 `(^x,^y,^z)` 的法则映射到新的相对坐标，因此 `xBot:int|float` 和 `yBot:int|float` 分别指代的是局部坐标系原点处一“虚拟”实体的俯仰角和偏航角。
        """
        # 函数声明

        self.inputPath = inputPath    # WhiteWallJson 文件所在路径
        self.randomSelect = randomSelect    # 旋转后，若同一个位置出现了多个方块，则是否从中随机取一个作为最终方块(随机方法服从均匀分布)
        self.xBot = pi*xBot/180    # 竖直方向上的旋转角度
        self.yBot = pi*yBot/180    # 水平方向上的旋转角度
        self.xSkewing = xSkewing    # 原始建筑在相对坐标系下的 x轴 偏移量
        self.ySkewing = ySkewing    # 原始建筑在相对坐标系下的 y轴 偏移量
        self.zSkewing = zSkewing    # 原始建筑在相对坐标系下的 z轴 偏移量
        self.input = []    # WhiteWallJson 文件被解析完成后输出的列表
        self.result = []    # 旋转结果
        # 实例化

    # 实例化函数

    
    
    def posChange(x:int|float, y:int|float, z:int|float, xBot:int|float, yBot:int|float) -> list:
        return [
            x*cos(yBot)-y*sin(xBot)*sin(yBot)-z*cos(xBot)*sin(yBot),
            y*cos(xBot)-z*sin(xBot),
            x*sin(yBot)+y*sin(xBot)*cos(yBot)+z*cos(xBot)*cos(yBot)
        ]
    # 更新坐标
    # 公式来源: https://github.com/Happy2018new/DreamLand-YingLunTown/blob/main/Command/%E9%87%8D%E8%A6%81%E7%A0%94%E7%A9%B6%E6%88%90%E6%9E%9C/%E5%9D%90%E6%A0%87%E6%81%92%E7%AD%89%E5%8F%98%E6%8D%A2/%E5%9D%90%E6%A0%87%E6%81%92%E7%AD%89%E5%8F%98%E6%8D%A2.pdf



    def main(self) -> bool:
        """
        \n摘要
        本函数是 `class: ModelRotation` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        当成功时，返回 `True `；当提供的文件被解析为非 `list` 类型时，返回 `False` 。除此之外，旋转后的结果会被储存在 `self.result: list` 中
        """
        # 函数声明


        with open(self.inputPath,"r+",encoding='utf-8') as file:
            self.input = json.load(file)
        if type(self.input) != list:
            return False
        # 读取 WhiteWallJson 文件为 list 格式


        for i in range(len(self.input)):
            if self.xSkewing == 0 and self.ySkewing == 0 and self.zSkewing == 0:
                break
            self.input[i]["x"] = self.input[i]["x"] + self.xSkewing
            self.input[i]["y"] = self.input[i]["y"] + self.ySkewing
            self.input[i]["z"] = self.input[i]["z"] + self.zSkewing
        # 执行偏移设置


        blockRecord_before = {}
        for i in range(len(self.input)):
            String = str(self.input[i]["x"]) + ',' + str(self.input[i]["y"]) + ',' + str(self.input[i]["z"])
            if not String in blockRecord_before:
                blockRecord_before[String] = [i]
            else:
                blockRecord_before[String].append(i)
        # 获取方块索引表，用于判断旋转前同一个位置是否存在多个方块
        # example: blockRecord_before = {"0,0,0": [0,1,2]}


        for i in range(len(self.input)):
            if self.xBot == 0.0 and self.yBot == 0.0:
                break
            ans = ModelRotation.posChange(
                self.input[i]["x"],
                self.input[i]["y"],
                self.input[i]["z"],
                self.xBot,
                self.yBot
            )
            self.input[i]["new_x"] = int(ans[0])
            self.input[i]["new_y"] = int(ans[1])
            self.input[i]["new_z"] = int(ans[2])
        # 更新坐标


        blockRecord = {}
        for i in range(len(self.input)):
            String = str(self.input[i]["new_x"]) + ',' + str(self.input[i]["new_y"]) + ',' + str(self.input[i]["new_z"])
            if not String in blockRecord:
                blockRecord[String] = [i]
            else:
                blockRecord[String].append(i)
        # 获取方块索引表，用于判断旋转后同一个位置是否存在多个方块
        # example: blockRecord = {"0,0,0": [0,1,2]}


        for i in blockRecord:
            block_location_in_json = blockRecord[i][random.randint(0,len(blockRecord[i]) - 1)] if self.randomSelect == True else blockRecord[i][0]
            String = str(self.input[block_location_in_json]["x"]) + ',' + str(self.input[block_location_in_json]["y"]) + ',' + str(self.input[block_location_in_json]["z"])
            for i1 in blockRecord_before[String]:
                self.result.append(self.input[i1])
                self.result[-1]["x"] = self.result[-1]["new_x"]
                self.result[-1]["y"] = self.result[-1]["new_y"]
                self.result[-1]["z"] = self.result[-1]["new_z"]
                del self.result[-1]["new_x"]
                del self.result[-1]["new_y"]
                del self.result[-1]["new_z"]
        # 筛除同一位置上重复的方块，只保留一个结果


        xMin = min([i["x"] for i in self.result])
        yMin = min([i["y"] for i in self.result])
        zMin = min([i["z"] for i in self.result])
        if xMin == 0 and yMin == 0 and zMin == 0:
            pass
        else:
            for i in range(len(self.result)):
                self.result[i]["x"] = self.result[i]["x"] - xMin
                self.result[i]["y"] = self.result[i]["y"] - yMin
                self.result[i]["z"] = self.result[i]["z"] - zMin
        # 将建筑物修正到第一象限


        del self.input
        # 删除不必要内容


        return True
        # 返回值