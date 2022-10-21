import json,sys # 载入第三方库
sys.path.append(".") # 载入本地库
import share,Others.Synthetic # 载入本地库
# 载入依赖项





with open("input.json","r+",encoding='utf-8') as file:
    WhiteWallJson = json.load(file)
# 将输入的 JSON 变为字典形式





blockPool = {}
blockCount = -1
for i in WhiteWallJson:
    if not f'{i["name"]},{i["aux"]}' in blockPool:
        blockCount = blockCount + 1
        blockPool[f'{i["name"]},{i["aux"]}'] = blockCount
# 取得方块池
# 形式诸如 {"blockId:str,data:int": paletteId}



for i in blockPool:
    i = i.split(',')
    share.pool.append(
        [
            i[0],
            int(i[1])
        ]
    )
share.pool.append(['minecraft:air',0])
# 设置 mcstructure 下的方块池





blockPos = {}
blockDataInJson = {}
for i in range(len(WhiteWallJson)):
    blockPos[str(WhiteWallJson[i]['x']) + ',' + str(WhiteWallJson[i]['y']) + ',' + str(WhiteWallJson[i]['z'])] = blockPool[
        WhiteWallJson[i]['name'] + ',' + str(WhiteWallJson[i]['aux'])
    ]
    blockDataInJson[str(WhiteWallJson[i]['x']) + ',' + str(WhiteWallJson[i]['y']) + ',' + str(WhiteWallJson[i]['z'])] = i
del blockPool
# 将 json 文件中记录的方块坐标制成索引表，便于查找对应位置的方块是否存在(形式诸如 {"x:int,y:int,z:int": location_in_the_block_pool:int})
# 同时记录目标方块在 json 文件中的位置(形式诸如 {"x:int,y:int,z:int": location_in_the_json:int})





xSize = 0
ySize = 0
zSize = 0
for i in WhiteWallJson:
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
                    WhiteWallJson[
                        blockDataInJson[String]
                    ]
                )
                if blockEntityData != None:
                    blockEntityDataList[f'{repeatingCount}:10'] = blockEntityData
                # 处理方块实体数据，如果有的话
            else:
                blockList.append(len(share.pool) - 1)
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





mcs = {
    "Root:10":
    {
        "size:9":[xSize, ySize, zSize],
        "structure:10":
        {
            "block_indices:9":
            [
                [],
                []
            ]
        }
    }
}
# 初始化


for i in blockList:
    mcs['Root:10']['structure:10']['block_indices:9'][0].append(i)
    mcs['Root:10']['structure:10']['block_indices:9'][1].append(-1)
# 转换为支持的格式(半转换)


if len(blockEntityDataList) > 0:
    mcs["Root:10"]["structure:10"]["palette:10"] = {
        "default:10":
        {
           "block_position_data:10": blockEntityDataList
        }
    }
# 处理方块实体数据，若存在的话


share.mcs = mcs
del mcs
# 善后