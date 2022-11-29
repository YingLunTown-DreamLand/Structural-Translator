import sys
sys.path.append(".")
import Others.CommandBlock
import Others.NBTtranslate
# 载入依赖项





def main(input:dict)->list:
    """
    \n摘要
    根据 `JSON` 记录的命令方块或容器数据，返回 `.mcstructure` 所支持的 `方块实体` 格式。
    \n参数
    `input:dict` 形如下述格式。
        `{"x":0, "y":0, "z":1, "name":"minecraft:glass", "aux":7}`
    \n返回值
    当待处理的方块携带有 `方块实体数据` 或是一个 `命令方块` ，则返回一个 `字典` ，格式如下。\n
    `{`
        `"block_entity_data:10": dict(Return)`
    `}`\n
    否则，返回 `None` 。\n
    特别地，`方块实体数据` 具有更高的优先级，可以覆盖 `命令方块` 选项
    """
    # 函数声明



    if 'entitynbt' in input:
        try:
            if type(input['entitynbt']) == str:
                return {"block_entity_data:10": Others.NBTtranslate.getAns(input['entitynbt'])}
                # WhiteWallJson 中记录的是 str 形式

            if type(input['entitynbt']) == list:
                entitynbt = b''.join(
                    [i.to_bytes(length=1,byteorder='big',signed=False) for i in input['entitynbt']]
                )
                # example: input['entitynbt'] = [2,3,4] -> entitynbt = b'\x02\x03\x04'
                try:
                    return {"block_entity_data:10": Others.NBTtranslate.getAns(entitynbt.decode())}
                    # 当 entitynbt 是 SNBT 时
                except:
                    return {"block_entity_data:10": entitynbt}
                    # 当 entitynbt 是一堆没有意义的二进制串时
                # Api/ParseBDX 输出的 entitynbt 是 list 形式

        except:
            return None
    # 若携带有可解析的 NBT 数据


    if ('cmddata' in input) and ((input['name'] == 'minecraft:command_block') or (
        input['name'] == 'minecraft:chain_command_block') or (input['name'] == 'minecraft:repeating_command_block')):
        return {"block_entity_data:10":Others.CommandBlock.cbGet(input['cmddata'])}
    # 若为命令方块


    return None
    # 如果既不是命令方块也不是容器，则返回 None