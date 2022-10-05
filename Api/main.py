import sys
sys.path.append(".")
import Api.indexList
import Api.unpackData
# 载入依赖项





BDXContext = Api.unpackData.getBDXdata('Api/input.bdx')
# 取得解压后的 BDX 数据
# 舍弃内部文件头 BDX



authorName = Api.unpackData.getBDXauthor(BDXContext)
BDXContext = authorName[-1]
authorName = authorName[0]
# 取得作者之名



penPos = [0,0,0]
blockPalette = []
resultList = []
# 初始化


while True:
    functionName = Api.unpackData.getType(BDXContext)
    if functionName == False:
        resultList.append('Error End')
        break
    BDXContext = functionName[-1]
    operation = functionName[1]
    functionName = functionName[0]
    # 取得函数名及操作编号
    # 若 Api.unpackData.getType 返回 False ，则表明文件可能已损坏

    if operation == bytearray(b'\x58'):
        resultList.append('XE')
        break
    # 判断是否需要结束

    if Api.indexList.indexListforMain[operation] == 'addToBlockPalette':
        lsSave = Api.unpackData.getBDXauthor(BDXContext)
        blockPalette.append(lsSave[0])
        BDXContext = lsSave[-1]
        continue
    # 添加方块到方块池
    if Api.indexList.indexListforMain[operation] == 'x+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext)')
        penPos[0] = penPos[0] + lsSave[0]
        penPos[1] = 0
        penPos[2] = 0
        BDXContext = lsSave[-1]
        continue
    # 旧版本 X 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'y+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext)')
        penPos[1] = penPos[1] + lsSave[0]
        penPos[2] = 0
        BDXContext = lsSave[-1]
        continue
    # 旧版本 Y 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'z+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext)')
        penPos[3] = penPos[3] + lsSave[0]
        BDXContext = lsSave[-1]
        continue
    # 旧版本 Z 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'placeBlock':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext)')
        blockPalette.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + lsSave[0],
            "aux": lsSave[1]
        })
        BDXContext = lsSave[-1]
        continue
    # 放置方块(不含 NBT 数据)