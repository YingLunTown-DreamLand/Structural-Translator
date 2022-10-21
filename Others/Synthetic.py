import sys
sys.path.append(".")
import Others.CommandBlock
import Others.NBTtranslate
import blockNBT.main
# 载入依赖项



def main(input:dict)->list:
    """
    \n摘要
    根据 `JSON` 记录的命令方块或容器数据，返回 `.mcstructure` 所支持的 `方块实体` 格式。
    \n参数
    `input:dict` 形如下述格式。
        `{"x":0, "y":0, "z":1, "name":"minecraft:glass", "aux":7}`
    \n返回值
    当待处理的方块是命令方块或支持的容器时，返回一个字典，格式如下。\n
    `{`
        `"block_entity_data:10": dict(Return)`
    `}`\n
    否则，返回 `None` 。
    """
    # 函数声明

    indexList = blockNBT.main.blockList
    # 载入资源

    if ('cmddata' in input) and ((input['name'] == 'minecraft:command_block') or (
        input['name'] == 'minecraft:chain_command_block') or (input['name'] == 'minecraft:repeating_command_block')):
        return {"block_entity_data:10":Others.CommandBlock.cbGet(input['cmddata'])}
    # 若为命令方块
    if ('entitynbt' in input) and (input['name'] in indexList):
        return {"block_entity_data:10":Others.NBTtranslate.getAns(input['entitynbt'])}
    # 若为容器
    return None
    # 如果既不是命令方块也不是容器，则返回 None