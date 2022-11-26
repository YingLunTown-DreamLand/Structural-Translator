import json, sys, nbtlib
sys.path.append(".")
import Others.Synthetic, Others.NBTtranslate, function
# 载入依赖项










class TranslateJSON:
    def __init__(
        self,
        inputPath:str
    )->None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `.mcstructure` 文件的路径
        """
        # 函数声明

        self.inputPath = inputPath    # 文件输入路径
        self.WhiteWallJson = {}    # WhiteWallJson: dict
        self.pool = []    # mcstructure 下的方块池
        self.json = {}    # 转义得到的结果
        # 实例化
    
    # 实例化函数







    def main(self)->None:
        """
        \n摘要
        本函数是 `class: TranslateJSON` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)，但转义得到的 `字典` 将会储存在 `self.json` 中
        """
        # 函数声明





        with open(self.inputPath,"r+",encoding='utf-8') as file:
            self.WhiteWallJson = json.load(file)
        # 将输入的 JSON 变为字典形式




        for i in range(len(self.WhiteWallJson)):
            if "blocknbt" in self.WhiteWallJson[i]:
                if type(self.WhiteWallJson[i]["blocknbt"]) == str:
                    try:
                        self.WhiteWallJson[i]["blocknbt"] = {
                            "states": function.outputJsonNBT_Compound(
                                nbtlib.parse_nbt(self.WhiteWallJson[i]["blocknbt"])
                            )["states"]
                        }
                    except:
                        None
        # 如果记录了 blocknbt 且其是 SNBT ，则将 blocknbt 处理为 {"states": ...}





        blockPool = {}
        blockCount = -1

        for i in self.WhiteWallJson:
            if "blocknbt" in i:
                try:
                    if not f'{i["name"]},{i["blocknbt"]["states"]}' in blockPool:
                        blockCount = blockCount + 1
                        blockPool[f'{i["name"]},{i["blocknbt"]["states"]}'] = blockCount
                except:
                    if not f'{i["name"]},{i["aux"]}' in blockPool:
                        blockCount = blockCount + 1
                        blockPool[f'{i["name"]},{i["aux"]}'] = blockCount
            elif not f'{i["name"]},{i["aux"]}' in blockPool:
                blockCount = blockCount + 1
                blockPool[f'{i["name"]},{i["aux"]}'] = blockCount
        # 取得方块池
        # 形式诸如 {"blockId:str,data:int": paletteId} or {"blockId:str,states:dict": paletteId}





        for i in blockPool:
            i = i.split(',',maxsplit=1)
            try:
                self.pool.append(
                    [
                        i[0],
                        int(i[1])
                    ]
                )
            except:
                self.pool.append(
                    [
                        i[0],
                        json.loads(i[1].replace("'",'"'))
                    ]
                )
        self.pool.append(['minecraft:air',{}])
        # 设置 mcstructure 下的方块池





        blockPos = {}
        blockDataInJson = {}


        for i in range(len(self.WhiteWallJson)):
            String = str(self.WhiteWallJson[i]['x']) + ',' + str(self.WhiteWallJson[i]['y']) + ',' + str(self.WhiteWallJson[i]['z'])
            
            if "blocknbt" in self.WhiteWallJson[i]:
                blockPos[String] = blockPool[
                    self.WhiteWallJson[i]['name'] + ',' + str(self.WhiteWallJson[i]["blocknbt"]["states"])
                ]
            else:
                blockPos[String] = blockPool[
                    self.WhiteWallJson[i]['name'] + ',' + str(self.WhiteWallJson[i]['aux'])
                ]
            
            blockDataInJson[String] = i

 
        del blockPool
        # 将 json 文件中记录的方块坐标制成索引表，便于查找对应位置的方块是否存在(形式诸如 {"x:int,y:int,z:int": location_in_the_block_pool:int})
        # 同时记录目标方块在 json 文件中的位置(形式诸如 {"x:int,y:int,z:int": location_in_the_json:int})





        xSize = 0
        ySize = 0
        zSize = 0
        for i in self.WhiteWallJson:
            if i['x'] > xSize:
                xSize = i['x']
            if i['y'] > ySize:
                ySize = i['y']
            if i['z'] > zSize:
                zSize = i['z']
        xSize = xSize + 1
        ySize = ySize + 1
        zSize = zSize + 1
        # 确定建筑物大小



        pos = [0,0,0]
        blockList = []
        blockEntityDataList = {}
        repeatingCount = -1
        xRepeat = xSize
        yRepeat = ySize
        zRepeat = zSize
        # 初始化


        while xRepeat > 0:
            xRepeat = xRepeat - 1
            # 改变数值

            while yRepeat > 0:
                yRepeat = yRepeat - 1
                # 改变数值
    
                while zRepeat > 0:
                    zRepeat = zRepeat - 1
                    # 改变数值

                    repeatingCount = repeatingCount + 1
                    # 得到当前被处理方块在密集矩阵下的角标

                    String = str(pos[0]) + ',' + str(pos[1]) + ',' + str(pos[2])
                    if String in blockPos:
                        blockList.append(blockPos[String]) 
                        # 向密集矩阵加入方块
                        blockEntityData = Others.Synthetic.main(
                            self.WhiteWallJson[
                                blockDataInJson[String]
                            ]
                        )
                        if blockEntityData != None:
                            blockEntityDataList[f'{repeatingCount}:10'] = blockEntityData
                        # 处理方块实体数据，如果有的话
                    else:
                        blockList.append(len(self.pool) - 1)
                    # 写入方块数据

                    if zRepeat > 0:
                        pos[2] = pos[2] + 1
                    # 移动指针
                # Z 轴

                if yRepeat > 0:
                    pos[1] = pos[1] + 1
                if zRepeat == 0:
                    zRepeat = zSize
                    pos[2] = 0
                # 移动指针
            # Y 轴及 X 轴

            if xRepeat > 0:
                pos[0] = pos[0] + 1
            if yRepeat == 0:
                yRepeat = ySize
                pos[1] = 0
            if zRepeat == 0:
                zRepeat = zSize
                pos[2] = 0
            # 移动指针
        


        self.json = {
            "Root:10":
            {
                "size:9":[xSize, ySize, zSize],
                "structure:10":
                {
                    "block_indices:9":
                    [
                        [],
                        []
                    ],
                    "palette:10":
                    {
                        "default:10":{}
                    }
                }
            }
        }
        # 初始化


        for i in blockList:
            self.json['Root:10']['structure:10']['block_indices:9'][0].append(i)
            self.json['Root:10']['structure:10']['block_indices:9'][1].append(-1)
        # 转换为支持的格式(半转换)


        if len(blockEntityDataList) > 0:
            self.json["Root:10"]["structure:10"]["palette:10"] = {
                "default:10":
                {
                   "block_position_data:10": blockEntityDataList
                }
            }
        # 处理方块实体数据，若存在的话