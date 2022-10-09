import sys
sys.path.append(".")
import Api.share
import Api.unpackData
import Api.indexList
import Api.ContainerIndex
import nbtlib
# 载入依赖项



def addToBlockPalette():
    Api.share.lsSave = Api.unpackData.getBDXauthor(Api.share.BDXContext,Api.share.pointer)
    Api.share.blockPalette.append(Api.share.lsSave[0])
    Api.share.pointer = Api.share.lsSave[-1]
# 添加方块到方块池

def xMoveOld():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.penPos[0] = Api.share.penPos[0] + Api.share.lsSave[0]
    Api.share.penPos[1] = 0
    Api.share.penPos[2] = 0
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版本 X 轴正方向移动

def yMoveOld():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.penPos[1] = Api.share.penPos[1] + Api.share.lsSave[0]
    Api.share.penPos[2] = 0
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版本 Y 轴正方向移动

def zMoveOld():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.penPos[2] = Api.share.penPos[2] + Api.share.lsSave[0]
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版本 Z 轴正方向移动

def placeBlock():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": 'minecraft:' + Api.share.blockPalette[Api.share.lsSave[0]],
        "aux": Api.share.lsSave[1]
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 放置方块(不含 NBT 数据)

def xMove():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    if Api.share.operation == b'\x0f':
        Api.share.lsSave[0] = Api.share.lsSave[0] * (-1)
    Api.share.penPos[0] = Api.share.penPos[0] + Api.share.lsSave[0]
    Api.share.pointer = Api.share.lsSave[-1]
# X 轴移动

def yMove():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    if Api.share.operation == b'\x11':
        Api.share.lsSave[0] = Api.share.lsSave[0] * (-1)
    Api.share.penPos[1] = Api.share.penPos[1] + Api.share.lsSave[0]
    Api.share.pointer = Api.share.lsSave[-1]
# Y 轴移动

def zMove():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    if Api.share.operation == b'\x13':
        Api.share.lsSave[0] = Api.share.lsSave[0] * (-1)
    Api.share.penPos[2] = Api.share.penPos[2] + Api.share.lsSave[0]
    Api.share.pointer = Api.share.lsSave[-1]
# Z 轴移动

def assignCommandBlockData():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    if Api.share.lsSave[0] == 0:
        name = 'minecraft:command_block'
    elif Api.share.lsSave[0] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": name,
        "aux": 0,
        "cmddata":
        {
            "lastOutput": Api.share.lsSave[3],
            "command": Api.share.lsSave[1],
            "shouldTrackOutput": Api.share.lsSave[6],
            "isConditional": Api.share.lsSave[7],
            "executeOnFirstTick": Api.share.lsSave[5],
            "tickDelay": Api.share.lsSave[4],
            "name": Api.share.lsSave[2],
            "isRedStoneMode": Api.share.lsSave[8]
        }
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版 - assignCommandBlockData

def placeCommandBlockWithData():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.resultList.append({
    "x": Api.share.penPos[0],
    "y": Api.share.penPos[1],
    "z": Api.share.penPos[2],
        "name": 'minecraft:' + Api.share.blockPalette[Api.share.lsSave[0]],
        "aux": Api.share.lsSave[1],
        "cmddata":
        {
            "lastOutput": Api.share.lsSave[5],
            "command": Api.share.lsSave[3],
            "shouldTrackOutput": Api.share.lsSave[8],
            "isConditional": Api.share.lsSave[9],
            "executeOnFirstTick": Api.share.lsSave[7],
            "tickDelay": Api.share.lsSave[6],
            "name": Api.share.lsSave[4],
            "isRedStoneMode": Api.share.lsSave[10]
        }
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版 - placeCommandBlockWithData

def useRuntimeIdPalette():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    exec(f'Api.share.runtimeIdsBlockPalette = Api.RuntimeIdPalette.version{Api.share.lsSave[0]}')
    print(Api.share.lsSave)
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版 - 设置 runtimeId 方块池

def placeBlockWithRuntimeId():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": 'minecraft:' + Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][0],
        "aux": Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][1]
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版 - 放置方块(不含 NBT 数据)

def placeCommandBlockWithRuntimeId():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": 'minecraft:' + Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][0],
        "aux": Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][1],
        "cmddata":
        {
            "lastOutput": Api.share.lsSave[4],
            "command": Api.share.lsSave[2],
            "shouldTrackOutput": Api.share.lsSave[7],
            "isConditional": Api.share.lsSave[8],
            "executeOnFirstTick": Api.share.lsSave[6],
            "tickDelay": Api.share.lsSave[5],
            "name": Api.share.lsSave[3],
            "isRedStoneMode": Api.share.lsSave[9]
        }
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 旧版 - placeCommandBlockWithRuntimeId

def placeCommandBlockWithDataNew():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    if Api.share.lsSave[1] == 0:
        name = 'minecraft:command_block'
    elif Api.share.lsSave[1] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": name,
        "aux": Api.share.lsSave[0],
        "cmddata":
        {
            "lastOutput": Api.share.lsSave[4],
            "command": Api.share.lsSave[2],
            "shouldTrackOutput": Api.share.lsSave[7],
            "isConditional": Api.share.lsSave[8],
            "executeOnFirstTick": Api.share.lsSave[6],
            "tickDelay": Api.share.lsSave[5],
            "name": Api.share.lsSave[3],
            "isRedStoneMode": Api.share.lsSave[9]
        }
    })
    Api.share.pointer = Api.share.lsSave[-1]
    # 放置命令方块 - placeCommandBlockWithDataNew

def placeBlockWithChestData():
    exec(f'Api.share.lsSave = Api.unpackData.{Api.share.functionName}(Api.share.BDXContext,Api.share.pointer)')
    Api.share.resultList.append({
        "x": Api.share.penPos[0],
        "y": Api.share.penPos[1],
        "z": Api.share.penPos[2],
        "name": 'minecraft:' + Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][0],
        "aux": Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][1],
        "entitynbt": nbtlib.serialize_tag(nbtlib.tag.Compound(
                {
                    Api.ContainerIndex.blockList[Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][0]][
                        str(Api.share.runtimeIdsBlockPalette[Api.share.lsSave[0]][1])
                    ][0]: Api.share.lsSave[1]
                }
            ))
    })
    Api.share.pointer = Api.share.lsSave[-1]
# 未使用的特性(但可调用) - 放置带有物品的容器