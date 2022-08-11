from email.quoprimime import body_check
import json
import sys
from tkinter import Y
sys.path.append(".")
import share
# 载入依赖项

with open("input.json","r+b") as file:
    whiteWalljson = json.loads(bytearray(b'').join(file.readlines()).decode())
# 将输入的 JSON 变为字典形式

blockpool = [i.split(',') for i in (list(set((i["name"] + ',' + str(i["aux"])) for i in whiteWalljson)))]
blockpool = [[i[0],int(i[1])] for i in blockpool]
blockpool.append(['minecraft:air',0])
share.pool = blockpool
# 取得方块池
blockId = ['{']
pointer = -1
# 初始化
for i in blockpool:
    pointer = pointer + 1
    blockId.append(f'"{i}":{pointer}')
    blockId.append(',')
blockId[-1] = '}'
blockId = json.loads(''.join(blockId))
# 取得方块ID字典

xSize = 0
ySize = 0
zSize = 0
for i in whiteWalljson:
    if i['x'] > xSize:
        xSize = i['x']
    if i['y'] > ySize:
        ySize = i['y']
    if i['z'] > zSize:
        zSize = i['z']
xSize = xSize + 1
ySize = ySize + 1
zSize = zSize + 1
# 取得建筑物大小

blockMatrix = [str(i["x"])+','+str(i["y"])+','+str(i["z"]) for i in whiteWalljson]
blockMatrixNew = ['{']
pointer = -1
for i in blockMatrix:
    pointer = pointer + 1
    blockMatrixNew.append(f'"{i}":{pointer}')
    blockMatrixNew.append(',')
blockMatrixNew[-1] = '}'
blockMatrixNew = json.loads("".join(blockMatrixNew))
blockMatrix = blockMatrixNew
del blockMatrixNew
# 取得方块索引表的字典
pos = [0,0,0]
blockList = []
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
            try:
                ans = blockMatrix[str(pos[0])+','+str(pos[1])+','+str(pos[2])]
                blockList.append(blockId[str([whiteWalljson[ans]["name"],whiteWalljson[ans]["aux"]])])
            except:
                blockList.append((len(share.pool) - 1))
            # 向方块索引表加入方块
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
blockMatrix = blockList
del blockList
# 取得密集矩阵

mcs = ['{"Root:10":{"size:9":['+str(xSize)+','+str(ySize)+','+str(zSize)+'],"structure:10":{"block_indices:9":[[']
# 初始化
for i in blockMatrix:
    mcs.append(str(i))
    mcs.append(',')
mcs[-1] = '],['
for i in blockMatrix:
    mcs.append('-1')
    mcs.append(',')
mcs[-1] = ']]}}}'
mcs = json.loads("".join(mcs))
share.mcs = mcs
# 转换为支持的格式(半转换)