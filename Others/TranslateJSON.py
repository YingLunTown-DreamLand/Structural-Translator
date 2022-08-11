import json
import sys
sys.path.append(".")
import share
# 载入依赖项

with open("input.json","r+b") as file:
    whiteWalljson = json.loads(bytearray(b'').join(file.readlines()).decode())
# 将输入的 JSON 变为字典形式

blockpool = [i.split(',') for i in (list(set((i["name"] + ',' + str(i["aux"])) for i in whiteWalljson)))]
blockpool = [[i[0],int(i[1])] for i in blockpool]
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

blockMatrix = [blockId[str([i["name"],i["aux"]])] for i in whiteWalljson]
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