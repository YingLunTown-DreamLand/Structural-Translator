import blockData.blockList   # 载入已加入方块状态支持的方块列表
import Api.JsonToNBT.JsonTranslate   # 载入 JSON 转 NBT 的模块
import nbtlib # 载入外部 NBT 库
# 载入依赖项





def searchingFor(input:str):
    """
    \n摘要
    查找字符串是否在列表`blockData.blockList.blockList`内，根据列表元素决定是全查找还是半查找
    \n参数
    `input:str` 指要被查找的字符串
    \n返回值
    返回`[匹配方块:str, import命令:str, 命令:str]`，类型是`list`
    `匹配方块:str` 指的是查找到的与`input`匹配的字段
    `import命令:str` 指的是要获取这种方块的数据值，应该预先执行的`import`命令
    `命令:str` 指的是要获取这种方块的数据值，应该执行的命令
    """
    # 函数声明
    for i in blockData.blockList.blockList:
        if i[0] == 0:
            if len(input.split(i[1])) > 1:
                return [i[1],i[2],i[3]]
            continue
        if i[0] == 1:
            if input == i[1]:
                return [i[1],i[2],i[3]]
# 查找字符串是否在列表 blockData.blockList.blockList 内，支持全查找或半查找





def moveCommand(input:int,Type:str):
    """
    \n摘要
    将给定的`int`转换为画笔的移动命令
    \n参数
    `input:int` 指要被转换的对象
    `Type:str` 指的是哪个轴上的移动，仅限`'x'`、`'y'`或`'z'`
    \n返回值
    返回一个`bytes`，是`bytearray`型
    """
    # 函数声明

    if input == 1 or input == 2:
        if Type == 'x':
            return bytearray(b'\x0e') * input
        if Type == 'y':
            return bytearray(b'\x10') * input
        if Type == 'z':
            return bytearray(b'\x12') * input

    if input == -1 or input == -2:
        if Type == 'x':
            return bytearray(b'\x0f') * abs(input)
        if Type == 'y':
            return bytearray(b'\x11') * abs(input)
        if Type == 'z':
            return bytearray(b'\x13') * abs(input)
    
    if -128 <= input <= 127:
        if Type == 'x':
            return bytearray(b'\x1c') + input.to_bytes(length=1,byteorder='big',signed=True)
        if Type == 'y':
            return bytearray(b'\x1d') + input.to_bytes(length=1,byteorder='big',signed=True)
        if Type == 'z':
            return bytearray(b'\x1e') + input.to_bytes(length=1,byteorder='big',signed=True)

    if -32768 <= input <= 65536:
        if Type == 'x':
            return bytearray(b'\x14') + input.to_bytes(length=2,byteorder='big',signed=True)
        if Type == 'y':
            return bytearray(b'\x16') + input.to_bytes(length=2,byteorder='big',signed=True)
        if Type == 'z':
            return bytearray(b'\x18') + input.to_bytes(length=2,byteorder='big',signed=True)

    if Type == 'x':
        return bytearray(b'\x15') + input.to_bytes(length=4,byteorder='big',signed=True)
    if Type == 'y':
        return bytearray(b'\x17') + input.to_bytes(length=4,byteorder='big',signed=True)
    if Type == 'z':
        return bytearray(b'\x19') + input.to_bytes(length=4,byteorder='big',signed=True)
# 根据移动大小输出移动命令





def outputStrNBT(input:dict,location:int)->str:
    """
    \n摘要
    访问对应方块下的 `方块实体` 数据，并返回 `Minecraft Java Edition` 下的 `NBT` 字符串形式
    \n参数
    `input:dict` 指的是装有 NBT 信息的字典
    `location:int` 指的是这个方块在密集矩阵下的角标
    \n返回值
    返回一个 `字符串` ，是 `Minecraft Java Edition` 下的 `NBT` 字符串形式
    """
    # 函数声明

    NBTdata = input["Root:10"]["structure:10"]["palette:10"][
        "default:10"]["block_position_data:10"][f"{location}:10"]["block_entity_data:10"]
    # 获取方块实体数据
    NBTdata = Api.JsonToNBT.JsonTranslate.JSONCompound(NBTdata)
    # 转换为 NBT 库下的格式
    return nbtlib.serialize_tag(NBTdata)
    # 返回值