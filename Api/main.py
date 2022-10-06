import sys
sys.path.append(".")
import nbtlib
import Api.indexList
import Api.unpackData
import Api.RuntimeIdPalette
import Api.ContainerIndex
# 载入依赖项





BDXContext = Api.unpackData.getBDXdata('Api/input.bdx')
# 取得解压后的 BDX 数据
# 舍弃内部文件头 BDX



authorName = Api.unpackData.getBDXauthor(BDXContext,0)
BDXContext = BDXContext[authorName[-1]:]
authorName = authorName[0]
# 取得作者之名



pointer = 0
penPos = [0,0,0]
blockPalette = []
resultList = []
runtimeIdsBlockPalette = []
successStates = False
# 初始化


while True:
    if BDXContext[pointer:pointer+1] == b'\x58':
        successStates = True
        break
    # 判断是否需要结束

    functionName = Api.unpackData.getType(BDXContext,pointer)
    if functionName == False:
        break
    pointer = functionName[-1]
    operation = functionName[1]
    functionName = functionName[0]
    # 取得函数名及操作编号
    # 若 Api.unpackData.getType 返回 False ，则表明文件可能已损坏

    if Api.indexList.indexListforMain[operation] == 'addToBlockPalette':
        lsSave = Api.unpackData.getBDXauthor(BDXContext,pointer)
        blockPalette.append(lsSave[0])
        pointer = lsSave[-1]
        continue
    # 添加方块到方块池
    if Api.indexList.indexListforMain[operation] == 'x+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        penPos[0] = penPos[0] + lsSave[0]
        penPos[1] = 0
        penPos[2] = 0
        pointer = lsSave[-1]
        continue
    # 旧版本 X 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'y+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        penPos[1] = penPos[1] + lsSave[0]
        penPos[2] = 0
        pointer = lsSave[-1]
        continue
    # 旧版本 Y 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'z+Move-old':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        penPos[2] = penPos[2] + lsSave[0]
        pointer = lsSave[-1]
        continue
    # 旧版本 Z 轴正方向移动
    if Api.indexList.indexListforMain[operation] == 'placeBlock':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + blockPalette[lsSave[0]],
            "aux": lsSave[1]
        })
        pointer = lsSave[-1]
        continue
    # 放置方块(不含 NBT 数据)
    if Api.indexList.indexListforMain[operation] == 'NOP':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        pointer = lsSave[-1]
        continue
    # “摆烂”操作
    if Api.indexList.indexListforMain[operation] == 'xMove':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        if operation == b'\x0f':
            lsSave[0] = lsSave[0] * (-1)
        penPos[0] = penPos[0] + lsSave[0]
        pointer = lsSave[-1]
        continue
    # X 轴移动
    if Api.indexList.indexListforMain[operation] == 'yMove':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        if operation == b'\x11':
            lsSave[0] = lsSave[0] * (-1)
        penPos[1] = penPos[1] + lsSave[0]
        pointer = lsSave[-1]
        continue
    # Y 轴移动
    if Api.indexList.indexListforMain[operation] == 'zMove':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        if operation == b'\x13':
            lsSave[0] = lsSave[0] * (-1)
        penPos[2] = penPos[2] + lsSave[0]
        pointer = lsSave[-1]
        continue
    # Z 轴移动
    if Api.indexList.indexListforMain[operation] == 'assignCommandBlockData':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        if lsSave[0] == 0:
            name = 'minecraft:command_block'
        elif lsSave[0] == 1:
            name = 'minecraft:repeating_command_block'
        else:
            name = 'minecraft:chain_command_block'
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": name,
            "aux": 0,
            "cmddata":
            {
                "lastOutput": lsSave[3],
                "command": lsSave[1],
                "shouldTrackOutput": lsSave[6],
                "isConditional": lsSave[7],
                "executeOnFirstTick": lsSave[5],
                "tickDelay": lsSave[4],
                "name": lsSave[2],
                "isRedStoneMode": lsSave[8]
            }
        })
        pointer = lsSave[-1]
        continue
    # 旧版 - assignCommandBlockData
    if Api.indexList.indexListforMain[operation] == 'placeCommandBlockWithData':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + blockPalette[lsSave[0]],
            "aux": lsSave[1],
            "cmddata":
            {
                "lastOutput": lsSave[5],
                "command": lsSave[3],
                "shouldTrackOutput": lsSave[8],
                "isConditional": lsSave[9],
                "executeOnFirstTick": lsSave[7],
                "tickDelay": lsSave[6],
                "name": lsSave[4],
                "isRedStoneMode": lsSave[10]
            }
        })
        pointer = lsSave[-1]
        continue
    # 旧版 - placeCommandBlockWithData
    if Api.indexList.indexListforMain[operation] == 'useRuntimeIdPalette':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        exec(f'runtimeIdsBlockPalette = Api.RuntimeIdPalette.version{lsSave[0]}')
        pointer = lsSave[-1]
        continue
    # 旧版 - 设置 runtimeId 方块池
    if Api.indexList.indexListforMain[operation] == 'placeBlockWithRuntimeId':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + runtimeIdsBlockPalette[lsSave[0]][0],
            "aux": runtimeIdsBlockPalette[lsSave[0]][1]
        })
        pointer = lsSave[-1]
        continue
    # 旧版 - 放置方块(不含 NBT 数据)
    if Api.indexList.indexListforMain[operation] == 'placeCommandBlockWithRuntimeId':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + runtimeIdsBlockPalette[lsSave[0]][0],
            "aux": runtimeIdsBlockPalette[lsSave[0]][1],
            "cmddata":
            {
                "lastOutput": lsSave[4],
                "command": lsSave[2],
                "shouldTrackOutput": lsSave[7],
                "isConditional": lsSave[8],
                "executeOnFirstTick": lsSave[6],
                "tickDelay": lsSave[5],
                "name": lsSave[3],
                "isRedStoneMode": lsSave[9]
            }
        })
        pointer = lsSave[-1]
        continue
    # 旧版 - placeCommandBlockWithRuntimeId
    if Api.indexList.indexListforMain[operation] == 'placeCommandBlockWithDataNew':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        if lsSave[1] == 0:
            name = 'minecraft:command_block'
        elif lsSave[1] == 1:
            name = 'minecraft:repeating_command_block'
        else:
            name = 'minecraft:chain_command_block'
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": name,
            "aux": lsSave[0],
            "cmddata":
            {
                "lastOutput": lsSave[4],
                "command": lsSave[2],
                "shouldTrackOutput": lsSave[7],
                "isConditional": lsSave[8],
                "executeOnFirstTick": lsSave[6],
                "tickDelay": lsSave[5],
                "name": lsSave[3],
                "isRedStoneMode": lsSave[9]
            }
        })
        pointer = lsSave[-1]
        continue
    # 放置命令方块 - placeCommandBlockWithDataNew
    if Api.indexList.indexListforMain[operation] == 'placeBlockWithChestData':
        exec(f'lsSave = Api.unpackData.{functionName}(BDXContext,pointer)')
        resultList.append({
            "x": penPos[0],
            "y": penPos[1],
            "z": penPos[2],
            "name": 'minecraft:' + runtimeIdsBlockPalette[lsSave[0]][0],
            "aux": runtimeIdsBlockPalette[lsSave[0]][1],
            "entitynbt": nbtlib.serialize_tag(nbtlib.tag.Compound(
                    {
                        Api.ContainerIndex.blockList[runtimeIdsBlockPalette[lsSave[0]][0]][
                            str(runtimeIdsBlockPalette[lsSave[0]][1])
                        ][0]: lsSave[1]
                    }
                ))
        })
        pointer = lsSave[-1]
        continue
    # 未使用的特性(但可调用) - 放置带有物品的容器


if authorName == '':
    print('作者未定义.')
else:
    print('作者之名: ' + authorName)
if successStates == False:
    print('文件不完整或已损坏')
if successStates == True:
    print('文件完整')
# 打印作者名称及文件完整结论
with open("Api/ans.json","w+",encoding='utf-8') as file:
    import json
    file.write(json.dumps(resultList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
# 输出结果
print('SUCCESS: 已成功解析目标文件，已保存在 Api 目录下，文件名是 ans.json .')
# 打印解析结果