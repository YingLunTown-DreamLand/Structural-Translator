import share
# 载入依赖项

def cbGet(foreground:list,pointer:int):
    """
    \n摘要
    将结构中记录的命令方块数据转换为 `BDX` 支持的编码格式
    \n参数
    `foreground:list` 指的是前景层的方块名称及数据值
    `pointer:int` 指的是指针位置
    \n返回值
    返回一个 `bytes` ，其为 `bytearray` 型
    """
    # 函数声明
    global share
    # 声明全局变量
    facing = foreground[1].to_bytes(length=2,byteorder='big')
    # 朝向
    if foreground[0] == 'minecraft:command_block':
        Type = bytearray(b'\x00\x00\x00\x00')
    if foreground[0] == 'minecraft:repeating_command_block':
        Type = bytearray(b'\x00\x00\x00\x01')
    if foreground[0] == 'minecraft:chain_command_block':
        Type = bytearray(b'\x00\x00\x00\x02')
    # 类型(脉冲, 循环, 链)
    try:
        command = share.mcs["Root:10"]["structure:10"]["palette:10"][
                    "default:10"]["block_position_data:10"][f"{pointer}:10"][
                    "block_entity_data:10"]["Command:8"]
        command = command.replace('\\n','\n')
        command = command.replace('-----Mark of use 0x10-----','\\n')
        command = command.replace('\\"','"')
        command = command.encode(encoding="utf-8")
    except:
        command = bytearray(b'')
    # 命令方块内的指令
    try:
        name = share.mcs["Root:10"]["structure:10"]["palette:10"][
                "default:10"]["block_position_data:10"][f"{pointer}:10"][
                "block_entity_data:10"]["CustomName:8"]
        name = name.replace('\\n','\n')
        name = name.replace('-----Mark of use 0x10-----','\\n')
        name = name.replace('\\"','"')
        name = name.encode(encoding="utf-8")
    except:
        name = bytearray(b'')
    # 悬浮字
    try:
        delay = share.mcs["Root:10"]["structure:10"]["palette:10"][
                "default:10"]["block_position_data:10"][f"{pointer}:10"][
                "block_entity_data:10"]["TickDelay:3"].to_bytes(length=4,byteorder='big',signed=True)
    except:
        delay = bytearray(b'\x00\x00\x00\x00')
    # 延迟
    try:
        executeOnFirstTick = share.mcs["Root:10"]["structure:10"]["palette:10"][
                                "default:10"]["block_position_data:10"][f"{pointer}:10"][
                                "block_entity_data:10"]["ExecuteOnFirstTick:1"].to_bytes(length=1,byteorder='big',signed=True)
    except:
        executeOnFirstTick = bytearray(b'\x00')
    # 在启动后的第一时刻执行命令(仅限于 重复 命令方块)
    try:
        trackOutput = share.mcs["Root:10"]["structure:10"]["palette:10"][
                        "default:10"]["block_position_data:10"][f"{pointer}:10"][
                        "block_entity_data:10"]["TrackOutput:1"].to_bytes(length=1,byteorder='big',signed=True)
    except:
        trackOutput = bytearray(b'\x01')
    # 是否保留执行日志
    try:
        conditional = share.mcs["Root:10"]["structure:10"]["palette:10"][
                        "default:10"]["block_position_data:10"][f"{pointer}:10"][
                            "block_entity_data:10"]["conditionalMode:1"].to_bytes(length=1,byteorder='big',signed=True)
    except:
        conditional = bytearray(b'\x00')
    # 是否有条件
    try:
        needRedstone = share.mcs["Root:10"]["structure:10"]["palette:10"][
                        "default:10"]["block_position_data:10"][f"{pointer}:10"][
                        "block_entity_data:10"]["auto:1"]
        if needRedstone == 0:
            nrs = bytearray(b'\x01')
        else:
            nrs = bytearray(b'\x00')
    except:
        nrs = bytearray(b'\x01')
    # 是否需要红石
    return bytearray(b'\x24')+facing+Type+command+bytearray(b'\x00')+name+bytearray(b'\x00')+bytearray(b'\x00')+delay+executeOnFirstTick+trackOutput+conditional+nrs
    # 返回放置命令