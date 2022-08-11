import blockData.blockList
# 载入已加入方块状态支持的方块列表

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
    global blockData
    # 声明全局变量
    for i in blockData.blockList.blockList:
        if i[0] == 0:
            if len(input.split(i[1])) > 1:
                return [i[1],i[2],i[3]]
            continue
        if i[0] == 1:
            if input == i[1]:
                return [i[1],i[2],i[3]]
# 查找字符串是否在列表 blockData.blockList.blockList 内，支持全查找或半查找

def bytearrayToStr(input:bytearray):
    """
    \n摘要
    将给定的`bytearray`转换为干净整洁的`str`
    \n参数
    `input:byerarray` 指要被转换的对象
    \n返回值
    返回一个干净整洁的`字符串`，类型是`str`
    """
    # 函数声明
    if type(input) != bytearray:
        return None
    else:
        input = str(input).split('bytearray(b\'',maxsplit=1)[1]
        input = input.split('\')')
        del input[-1]
        return "".join(input)
# 将给定的 bytearray 转换为干净整洁的 str

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

    if input == 1 or input == 2 or input == 3:
        if Type == 'x':
            if input == 1:
                return bytearray(b'\x0e')
            if input == 2:
                return bytearray(b'\x0e\x0e')
            if input == 3:
                return bytearray(b'\x0e\x0e\x0e')
        if Type == 'y':
            if input == 1:
                return bytearray(b'\x10')
            if input == 2:
                return bytearray(b'\x10\x10')
            if input == 3:
                return bytearray(b'\x10\x10\x10')
        if Type == 'z':
            if input == 1:
                return bytearray(b'\x12')
            if input == 2:
                return bytearray(b'\x12\x12')
            if input == 3:
                return bytearray(b'\x12\x12\x12')

    if input == -1 or input == -2 or input == -3:
        if Type == 'x':
            if input == -1:
                return bytearray(b'\x0f')
            if input == -2:
                return bytearray(b'\x0f\x0f')
            if input == -3:
                return bytearray(b'\x0f\x0f\x0f')
        if Type == 'y':
            if input == -1:
                return bytearray(b'\x11')
            if input == -2:
                return bytearray(b'\x11\x11')
            if input == -3:
                return bytearray(b'\x11\x11\x11')
        if Type == 'z':
            if input == -1:
                return bytearray(b'\x13')
            if input == -2:
                return bytearray(b'\x13\x13')
            if input == -3:
                return bytearray(b'\x13\x13\x13')

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