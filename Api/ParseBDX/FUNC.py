import sys
sys.path.append(".")
import Api.ParseBDX.shareFUNC
import Api.ParseBDX.unpackData
import Api.ParseBDX.indexList
import Api.ParseBDX.ContainerIndex
import function, share
import nbtlib
# 载入依赖项



def addToBlockPalette():
    Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.getBDXauthor(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)
    Api.ParseBDX.shareFUNC.blockPalette.append(Api.ParseBDX.shareFUNC.lsSave[0])
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 添加方块到方块池

def xMoveOld():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.penPos[0] = Api.ParseBDX.shareFUNC.penPos[0] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.penPos[1] = 0
    Api.ParseBDX.shareFUNC.penPos[2] = 0
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版本 X 轴正方向移动

def yMoveOld():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.penPos[1] = Api.ParseBDX.shareFUNC.penPos[1] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.penPos[2] = 0
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版本 Y 轴正方向移动

def zMoveOld():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.penPos[2] = Api.ParseBDX.shareFUNC.penPos[2] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版本 Z 轴正方向移动

def placeBlock():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.shareFUNC.blockPalette[Api.ParseBDX.shareFUNC.lsSave[0]],
        "aux": Api.ParseBDX.shareFUNC.lsSave[1]
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 以数据值(附加值)放置方块(不含 NBT 数据)

def NOP():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 摆烂(不执行任何操作)

def PlaceBlockWithBlockStates():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    share.reset()
    blockName = 'minecraft:' + Api.ParseBDX.shareFUNC.blockPalette[Api.ParseBDX.shareFUNC.lsSave[0]]
    i1 = function.searchingFor(blockName)
    try:
        i1 = [
            i1[0],
            i1[1].replace('blockData','blockData_NoType'),
            i1[2].replace('blockData','blockData_NoType')
        ]
        share.ans = Api.ParseBDX.shareFUNC.lsSave[1]
        share.name = blockName
        exec(i1[1])
        exec(f'share.pool.append([blockName,{i1[2]}])')
        if share.pool[-1][-1] == None:
            0/0
        if type(share.pool[-1][-1]) == list:
            if share.pool[-1][-1][-1] == '摆烂':
                share.pool[-1] = [share.pool[-1][0],share.pool[-1][1][0],'摆烂']
    except ZeroDivisionError:
        share.pool[-1][-1] = 0
        Api.ParseBDX.shareFUNC.blockStatesError.append(
            {
                "x": Api.ParseBDX.shareFUNC.penPos[0],
                "y": Api.ParseBDX.shareFUNC.penPos[1],
                "z": Api.ParseBDX.shareFUNC.penPos[2],
                "name": blockName,
                "blocknbt": 
                {
                    "states": Api.ParseBDX.shareFUNC.lsSave[1],
                    "name": blockName
                },
                "warningInfo": 'function.return.none'
            }
        )
    except TypeError:
        share.pool.append([blockName,0])
        if not Api.ParseBDX.shareFUNC.lsSave[1] == {}:
            Api.ParseBDX.shareFUNC.blockStatesError.append(
                {
                    "x": Api.ParseBDX.shareFUNC.penPos[0],
                    "y": Api.ParseBDX.shareFUNC.penPos[1],
                    "z": Api.ParseBDX.shareFUNC.penPos[2],
                    "name": blockName,
                    "blocknbt": 
                    {
                        "states": Api.ParseBDX.shareFUNC.lsSave[1],
                        "name": blockName
                    },
                "warningInfo": 'block.not.found'
                }
            )
    except:
        share.pool.append([blockName,0])
        Api.ParseBDX.shareFUNC.blockStatesError.append(
            {
                "x": Api.ParseBDX.shareFUNC.penPos[0],
                "y": Api.ParseBDX.shareFUNC.penPos[1],
                "z": Api.ParseBDX.shareFUNC.penPos[2],
                "name": blockName,
                "blocknbt": 
                {
                    "states": Api.ParseBDX.shareFUNC.lsSave[1],
                    "name": blockName
                },
                "warningInfo": 'translate.error'
            }
        )
    # get block data
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": blockName,
        "aux": int(share.pool[-1][-1]),
        "blocknbt": 
        {
            "states": Api.ParseBDX.shareFUNC.lsSave[1],
            "name": blockName
        }
    })
    # append result
    share.reset()
    # clean glabol values
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
    # set pointer to a new one
# 以方块状态放置方块(不含 NBT 数据)

def xMove():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.operation == b'\x0f':
        Api.ParseBDX.shareFUNC.lsSave[0] = Api.ParseBDX.shareFUNC.lsSave[0] * (-1)
    Api.ParseBDX.shareFUNC.penPos[0] = Api.ParseBDX.shareFUNC.penPos[0] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# X 轴移动

def yMove():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.operation == b'\x11':
        Api.ParseBDX.shareFUNC.lsSave[0] = Api.ParseBDX.shareFUNC.lsSave[0] * (-1)
    Api.ParseBDX.shareFUNC.penPos[1] = Api.ParseBDX.shareFUNC.penPos[1] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# Y 轴移动

def zMove():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.operation == b'\x13':
        Api.ParseBDX.shareFUNC.lsSave[0] = Api.ParseBDX.shareFUNC.lsSave[0] * (-1)
    Api.ParseBDX.shareFUNC.penPos[2] = Api.ParseBDX.shareFUNC.penPos[2] + Api.ParseBDX.shareFUNC.lsSave[0]
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# Z 轴移动

def assignCommandBlockData():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.lsSave[0] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.shareFUNC.lsSave[0] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": name,
        "aux": 0,
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.shareFUNC.lsSave[3],
            "command": Api.ParseBDX.shareFUNC.lsSave[1],
            "shouldTrackOutput": Api.ParseBDX.shareFUNC.lsSave[6],
            "isConditional": Api.ParseBDX.shareFUNC.lsSave[7],
            "executeOnFirstTick": Api.ParseBDX.shareFUNC.lsSave[5],
            "tickDelay": Api.ParseBDX.shareFUNC.lsSave[4],
            "name": Api.ParseBDX.shareFUNC.lsSave[2],
            "isRedStoneMode": Api.ParseBDX.shareFUNC.lsSave[8]
        }
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版 - assignCommandBlockData

def placeCommandBlockWithData():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.lsSave[2] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.shareFUNC.lsSave[2] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.shareFUNC.resultList.append({
    "x": Api.ParseBDX.shareFUNC.penPos[0],
    "y": Api.ParseBDX.shareFUNC.penPos[1],
    "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.shareFUNC.lsSave[1],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.shareFUNC.lsSave[5],
            "command": Api.ParseBDX.shareFUNC.lsSave[3],
            "shouldTrackOutput": Api.ParseBDX.shareFUNC.lsSave[8],
            "isConditional": Api.ParseBDX.shareFUNC.lsSave[9],
            "executeOnFirstTick": Api.ParseBDX.shareFUNC.lsSave[7],
            "tickDelay": Api.ParseBDX.shareFUNC.lsSave[6],
            "name": Api.ParseBDX.shareFUNC.lsSave[4],
            "isRedStoneMode": Api.ParseBDX.shareFUNC.lsSave[10]
        }
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版 - placeCommandBlockWithData

def useRuntimeIdPalette():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    exec(f'Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette = Api.ParseBDX.RuntimeIdPalette.version{Api.ParseBDX.shareFUNC.lsSave[0]}')
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版 - 设置 runtimeId 方块池

def placeBlockWithRuntimeId():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][0],
        "aux": Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][1]
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版 - 放置方块(不含 NBT 数据)

def placeCommandBlockWithRuntimeId():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.lsSave[1] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.shareFUNC.lsSave[1] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][1],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.shareFUNC.lsSave[4],
            "command": Api.ParseBDX.shareFUNC.lsSave[2],
            "shouldTrackOutput": Api.ParseBDX.shareFUNC.lsSave[7],
            "isConditional": Api.ParseBDX.shareFUNC.lsSave[8],
            "executeOnFirstTick": Api.ParseBDX.shareFUNC.lsSave[6],
            "tickDelay": Api.ParseBDX.shareFUNC.lsSave[5],
            "name": Api.ParseBDX.shareFUNC.lsSave[3],
            "isRedStoneMode": Api.ParseBDX.shareFUNC.lsSave[9]
        }
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 旧版 - placeCommandBlockWithRuntimeId

def placeCommandBlockWithDataNew():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    if Api.ParseBDX.shareFUNC.lsSave[1] == 0:
        name = 'minecraft:command_block'
    elif Api.ParseBDX.shareFUNC.lsSave[1] == 1:
        name = 'minecraft:repeating_command_block'
    else:
        name = 'minecraft:chain_command_block'
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": name,
        "aux": Api.ParseBDX.shareFUNC.lsSave[0],
        "cmddata":
        {
            "lastOutput": Api.ParseBDX.shareFUNC.lsSave[4],
            "command": Api.ParseBDX.shareFUNC.lsSave[2],
            "shouldTrackOutput": Api.ParseBDX.shareFUNC.lsSave[7],
            "isConditional": Api.ParseBDX.shareFUNC.lsSave[8],
            "executeOnFirstTick": Api.ParseBDX.shareFUNC.lsSave[6],
            "tickDelay": Api.ParseBDX.shareFUNC.lsSave[5],
            "name": Api.ParseBDX.shareFUNC.lsSave[3],
            "isRedStoneMode": Api.ParseBDX.shareFUNC.lsSave[9]
        }
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
    # 放置命令方块 - placeCommandBlockWithDataNew

def placeBlockWithChestData():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.resultList.append({
        "x": Api.ParseBDX.shareFUNC.penPos[0],
        "y": Api.ParseBDX.shareFUNC.penPos[1],
        "z": Api.ParseBDX.shareFUNC.penPos[2],
        "name": 'minecraft:' + Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][0],
        "aux": Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][1],
        "entitynbt": nbtlib.serialize_tag(nbtlib.tag.Compound(
                {
                    Api.ParseBDX.ContainerIndex.blockList[Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][0]][
                        str(Api.ParseBDX.shareFUNC.runtimeIdsBlockPalette[Api.ParseBDX.shareFUNC.lsSave[0]][1])
                    ][0]: Api.ParseBDX.shareFUNC.lsSave[1]
                }
            ))
    })
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 未使用的特性(但可调用) - 放置带有物品的容器

def recordBlockEntityData():
    exec(f'Api.ParseBDX.shareFUNC.lsSave = Api.ParseBDX.unpackData.{Api.ParseBDX.shareFUNC.functionName}(Api.ParseBDX.shareFUNC.BDXContext,Api.ParseBDX.shareFUNC.pointer)')
    Api.ParseBDX.shareFUNC.recordBlockEntityData.append(
        {
            "x": Api.ParseBDX.shareFUNC.penPos[0],
            "y": Api.ParseBDX.shareFUNC.penPos[1],
            "z": Api.ParseBDX.shareFUNC.penPos[2],
            "entitynbt": Api.ParseBDX.shareFUNC.lsSave[0],
            "location": Api.ParseBDX.shareFUNC.pointer
        }
    )
    Api.ParseBDX.shareFUNC.pointer = Api.ParseBDX.shareFUNC.lsSave[-1]
# 未被实现的特性/保留的特性
# 在 BDX 中支持一个可选的 Operation ，用于记录方块或实体的 NBT 数据
# https://github.com/LNSSPsd/PhoenixBuilder/issues/83

def collectionRecordBlockEntityData():
    indexList = {}
    for i in range(len(Api.ParseBDX.shareFUNC.resultList)):
        String = Api.ParseBDX.shareFUNC.resultList[i]
        String = str(String["x"]) + ',' + str(String["y"]) + ',' + str(String["z"])
        indexList[String] = i
    for i in Api.ParseBDX.shareFUNC.recordBlockEntityData:
        String = str(i["x"]) + ',' + str(i["y"]) + ',' + str(i["z"])
        if String in indexList:
            Api.ParseBDX.shareFUNC.resultList[indexList[String]]["entitynbt"] = str(b''.join([m.to_bytes(length=1,byteorder='big',signed=False) for m in i["entitynbt"]]))
        else:
            Api.ParseBDX.shareFUNC.recordBlockEntityDataErrorList.append(
                {
                    "x": i["x"],
                    "y": i["y"],
                    "z": i["z"],
                    "entitynbt": str(b''.join([m.to_bytes(length=1,byteorder='big',signed=False) for m in i["entitynbt"]])),
                    "errorType": "Block not found",
                    "errorLocation": i["location"]
                }
            )
# 将 operation39(recordBlockEntityData) 记录的 NBT 汇总并写入到具体的方块中