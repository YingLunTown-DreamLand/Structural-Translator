import share
import copy
# 载入依赖项










class replaceBlockID:
    def __init__(
        self,
        input:list
    )->None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `input:list` 提供的替换列表
        """
        # 函数声明

        self.input = input    # 提供的替换列表
        self.errorLog = []    # 错误日志
        self.result = []    # 处理结果
        # 实例化
    
    # 实例化函数







    def main(self)->None:
        """
        \n摘要
        本函数是 `class: replaceBlockID` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)。当该组件运行时发生了错误，则会在 `self.errorLog: list` 显示 `self.input` 的错误位置。
        除此之外，替换结果会保存在 `self.result: list` 下，格式为 `[share.pool, share.ContainerReplaceBlockIDList]` 。\n
        应当特别说明的是，本函数会自动更新 `share.pool` 中的内容，因此 `self.result: list` 只是为了记录结果而构造的一个列表。
        """
        # 函数声明





        for i in range(len(self.input)):    # example: i = 'B;minecraft:grass,2,minecraft:glass,0'
            location = i
            # 记录当前正在处理的项

            i = self.input[i].split(';',maxsplit=1)    # ['B', 'minecraft:grass,2,minecraft:glass,0']
            try:
                Type = i[0]    # 'B'
                String = i[1]    # 'minecraft:grass,2,minecraft:glass,0'
            except:
                self.errorLog.append(location)    # 写入错误日志
                continue
            # 提取类型及替换字符串



            String = String.split(',',maxsplit=3)    # ['minecraft:grass', '2', 'minecraft:glass', '0']
            # 将替换字符串拆分为列表



            try:
                FromName = String[0]    # 'minecraft:grass'
                FromData = int(String[1])    # 2
                ToName = String[2]    # 'minecraft:glass'
                ToData = int(String[3])    # 0
            except:
                self.errorLog.append(location)    # 写入错误日志
                continue
            # 提取替换方块的名称、数据值和被替换方块的名称、数据值



            del String

            if FromName.find('minecraft:') == -1 or ToName.find('minecraft:') == -1:
                self.errorLog.append(location)    # 写入错误日志
                continue
                # 检查提供的名称是否存在“minecraft”命名空间

            if (FromData != -1 and FromData < 0) or (ToData != -1 and ToData < 0):
                self.errorLog.append(location)    # 写入错误日志
                continue
                # 检查提供的数据值是否是自然数或 -1

            # 删除无关内容并进行检查



            if Type == 'B':
                for i in range(len(share.pool)):

                    save = share.pool[i]    # example: save = ['minecraft:grass', 2]

                    if FromName == save[0] and (FromData == save[1] or FromData == -1):
                        share.pool[i][0] = ToName
                        # 修改名称

                        if save[-1] == '摆烂':    # 这里考虑 save = ['minecraft:double_plant', 0, '摆烂']
                            del share.pool[i][-1]
                        # 考虑“摆烂”情况

                        if ToData != -1:
                            share.pool[i][1] = ToData
                        # 修改数据值

            # 处理方块池(share.pool)


            elif Type == 'C':
                share.ContainerReplaceBlockIDList.append(
                    [
                        FromName,
                        FromData,
                        ToName,
                        ToData
                    ]
                )
            # 处理容器内的物品
    # 主体部分





        self.result = [
            copy.deepcopy(share.pool),
            copy.deepcopy(share.ContainerReplaceBlockIDList)
        ]
        # 写入处理结果
    # 主函数