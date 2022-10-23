import sys
sys.path.append(".")
import Api.ParseBDX.share
import Api.ParseBDX.unpackData
import Api.ParseBDX.indexList
import Api.ParseBDX.ContainerIndex
import nbtlib
# 载入依赖项



def addToBlockPalette():
    Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.getBDXauthor(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)
    Api.ParseBDX.share.blockPalette.append(Api.ParseBDX.share.lsSave[0])
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 添加方块到方块池

def xMoveOld():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.penPos[0] = Api.ParseBDX.share.penPos[0] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.penPos[1] = 0
    Api.ParseBDX.share.penPos[2] = 0
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版本 X 轴正方向移动

def yMoveOld():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.penPos[1] = Api.ParseBDX.share.penPos[1] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.penPos[2] = 0
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版本 Y 轴正方向移动

def zMoveOld():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.penPos[2] = Api.ParseBDX.share.penPos[2] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版本 Z 轴正方向移动

def placeBlock():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.share.blockPalette[Api.ParseBDX.share.lsSave[0]],
        "aux": Api.ParseBDX.share.lsSave[1]
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 放置方块(不含 NBT 数据)

def xMove():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.operation == b'\x0f':
        Api.ParseBDX.share.lsSave[0] = Api.ParseBDX.share.lsSave[0] * (-1)
    Api.ParseBDX.share.penPos[0] = Api.ParseBDX.share.penPos[0] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# X 轴移动

def yMove():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.operation == b'\x11':
        Api.ParseBDX.share.lsSave[0] = Api.ParseBDX.share.lsSave[0] * (-1)
    Api.ParseBDX.share.penPos[1] = Api.ParseBDX.share.penPos[1] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# Y 轴移动

def zMove():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.operation == b'\x13':
        Api.ParseBDX.share.lsSave[0] = Api.ParseBDX.share.lsSave[0] * (-1)
    Api.ParseBDX.share.penPos[2] = Api.ParseBDX.share.penPos[2] + Api.ParseBDX.share.lsSave[0]
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# Z 轴移动

def assignCommandBlockData():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.lsSave[0] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.share.lsSave[0] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": name,
        "aux": 0,
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.share.lsSave[3],
            "command": Api.ParseBDX.share.lsSave[1],
            "shouldTrackOutput": Api.ParseBDX.share.lsSave[6],
            "isConditional": Api.ParseBDX.share.lsSave[7],
            "executeOnFirstTick": Api.ParseBDX.share.lsSave[5],
            "tickDelay": Api.ParseBDX.share.lsSave[4],
            "name": Api.ParseBDX.share.lsSave[2],
            "isRedStoneMode": Api.ParseBDX.share.lsSave[8]
        }
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版 - assignCommandBlockData

def placeCommandBlockWithData():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.lsSave[2] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.share.lsSave[2] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.share.resultList.append({
    "x": Api.ParseBDX.share.penPos[0],
    "y": Api.ParseBDX.share.penPos[1],
    "z": Api.ParseBDX.share.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.share.lsSave[1],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.share.lsSave[5],
            "command": Api.ParseBDX.share.lsSave[3],
            "shouldTrackOutput": Api.ParseBDX.share.lsSave[8],
            "isConditional": Api.ParseBDX.share.lsSave[9],
            "executeOnFirstTick": Api.ParseBDX.share.lsSave[7],
            "tickDelay": Api.ParseBDX.share.lsSave[6],
            "name": Api.ParseBDX.share.lsSave[4],
            "isRedStoneMode": Api.ParseBDX.share.lsSave[10]
        }
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版 - placeCommandBlockWithData

def useRuntimeIdPalette():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    exec(f'Api.ParseBDX.share.runtimeIdsBlockPalette = Api.ParseBDX.RuntimeIdPalette.version{Api.ParseBDX.share.lsSave[0]}')
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版 - 设置 runtimeId 方块池

def placeBlockWithRuntimeId():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][0],
        "aux": Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][1]
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版 - 放置方块(不含 NBT 数据)

def placeCommandBlockWithRuntimeId():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.lsSave[1] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.share.lsSave[1] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][1],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.share.lsSave[4],
            "command": Api.ParseBDX.share.lsSave[2],
            "shouldTrackOutput": Api.ParseBDX.share.lsSave[7],
            "isConditional": Api.ParseBDX.share.lsSave[8],
            "executeOnFirstTick": Api.ParseBDX.share.lsSave[6],
            "tickDelay": Api.ParseBDX.share.lsSave[5],
            "name": Api.ParseBDX.share.lsSave[3],
            "isRedStoneMode": Api.ParseBDX.share.lsSave[9]
        }
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 旧版 - placeCommandBlockWithRuntimeId

def placeCommandBlockWithDataNew():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    if Api.ParseBDX.share.lsSave[1] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.share.lsSave[1] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.share.lsSave[0],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.share.lsSave[4],
            "command": Api.ParseBDX.share.lsSave[2],
            "shouldTrackOutput": Api.ParseBDX.share.lsSave[7],
            "isConditional": Api.ParseBDX.share.lsSave[8],
            "executeOnFirstTick": Api.ParseBDX.share.lsSave[6],
            "tickDelay": Api.ParseBDX.share.lsSave[5],
            "name": Api.ParseBDX.share.lsSave[3],
            "isRedStoneMode": Api.ParseBDX.share.lsSave[9]
        }
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
    # 放置命令方块 - placeCommandBlockWithDataNew

def placeBlockWithChestData():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    Api.ParseBDX.share.resultList.append({
        "x": Api.ParseBDX.share.penPos[0],
        "y": Api.ParseBDX.share.penPos[1],
        "z": Api.ParseBDX.share.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][0],
        "aux": Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][1],
        "entitynbt": nbtlib.serialize_tag(nbtlib.tag.Compound(
                {
                    Api.ParseBDX.ContainerIndex.blockList[Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][0]][
                        str(Api.ParseBDX.share.runtimeIdsBlockPalette[Api.ParseBDX.share.lsSave[0]][1])
                    ][0]: Api.ParseBDX.share.lsSave[1]
                }
            ))
    })
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 未使用的特性(但可调用) - 放置带有物品的容器

def operation39():
    exec(f'Api.ParseBDX.share.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.share.functionName}(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)')
    print(Api.ParseBDX.share.lsSave[0])
    Api.ParseBDX.share.pointer = Api.ParseBDX.share.lsSave[-1]
# 未被实现的特性/保留的特性
# 在 BDX 中支持一个可选的 Operation ，用于记录方块或实体的 NBT 数据
# https://github.com/LNSSPsd/PhoenixBuilder/issues/83