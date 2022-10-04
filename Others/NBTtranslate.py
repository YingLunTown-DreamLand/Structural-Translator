import nbtlib
# 载入依赖项



def Compound(input:nbtlib.tag.Compound)->dict:
    """
    \n摘要
    本函数主要用于处理已解析好的 `nbtlib.tag.Compound`
    \n参数
    `input:nbtlib.tag.Compound` 一个 `Compound` ，一般用一组花括号 `{}` 括起来。
    \n返回值
    返回一个字典。
    """
    # 函数声明

    ans = {}
    # 初始化

    for i in input.keys():
        if type(input[i]) == nbtlib.tag.Byte:
            ans[f'{i}:1'] = int(input[i])
            continue
        # byte
        if type(input[i]) == nbtlib.tag.Short:
            ans[f'{i}:2'] = int(input[i])
            continue
        # short
        if type(input[i]) == nbtlib.tag.Int:
            ans[f'{i}:3'] = int(input[i])
            continue
        # int
        if type(input[i]) == nbtlib.tag.Long:
            ans[f'{i}:4'] = int(input[i])
            continue
        # long
        if type(input[i]) == nbtlib.tag.Float:
            ans[f'{i}:5'] = float(input[i])
            continue
        # float
        if type(input[i]) == nbtlib.tag.Double:
            ans[f'{i}:6'] = float(input[i])
            continue
        # double
        if type(input[i]) == nbtlib.tag.String:
            ans[f'{i}:8'] = str(input[i])
            continue
        # string
        if type(input[i]) == nbtlib.tag.Compound:
            ans[f'{i}:10'] = Compound(input[i])
            continue
        # Compound
        if type(input[i]) == nbtlib.tag.ByteArray:
            ans[f'{i}:7'] = List(input[i])
            continue
        # byte_array
        if type(input[i]) == nbtlib.tag.IntArray:
            ans[f'{i}:11'] = List(input[i])
            continue
        # int_array
        if type(input[i]) == nbtlib.tag.LongArray:
            ans[f'{i}:12'] = List(input[i])
            continue
        # long_array
        ans[f'{i}:9'] = List(input[i])
        # list

    return ans
    # 返回值



def List(input)->list:
    """
    \n摘要
    本函数主要用于处理已解析好的 `nbtlib.tag.list`
    \n参数
    `input` 是一个 `nbtlib.tag.list` ，一般用一组花括号 `{}` 括起来。
    \n返回值
    返回一个列表。
    """
    # 函数声明


    ans = []
    # 初始化


    if type(input) == nbtlib.tag.ByteArray or type(input) == nbtlib.tag.IntArray or type(input) == nbtlib.tag.LongArray or type(
        input) == nbtlib.tag.List[nbtlib.tag.Int]:
        return [int(i) for i in input]
    # Int, byte_array, int_array, long_array

    if type(input) == nbtlib.tag.List[nbtlib.tag.Byte]:
        for i in input:
            ans.append(f'{int(i)}:01')
        return ans
    # byte
    if type(input) == nbtlib.tag.List[nbtlib.tag.Short]:
        for i in input:
            ans.append(f'{int(i)}:02')
        return ans
    # short
    if type(input) == nbtlib.tag.List[nbtlib.tag.Long]:
        for i in input:
            ans.append(f'{int(i)}:04')
        return ans
    # long
    if type(input) == nbtlib.tag.List[nbtlib.tag.Float]:
        for i in input:
            ans.append(f'{float(i)}:05')
        return ans
    # float
    if type(input) == nbtlib.tag.List[nbtlib.tag.Double]:
        for i in input:
            ans.append(f'{float(i)}:06')
        return ans
    # double
    if type(input) == nbtlib.tag.List[nbtlib.tag.String]:
        for i in input:
            ans.append(f'{str(i)}:08')
        return ans
    # string
    if type(input) == nbtlib.tag.List[nbtlib.tag.Compound]:
        for i in input:
            ans.append(Compound(i))
        return ans
    # compound

    if type(input) == nbtlib.tag.List[nbtlib.tag.ByteArray]:
        for i in input:
            memorySave = []
            for i1 in i:
                memorySave.append(f'{int(i1)}:07')
            ans.append(memorySave)
        return ans
    # list-byte_array
    if type(input) == nbtlib.tag.List[nbtlib.tag.IntArray]:
        for i in input:
            memorySave = []
            for i1 in i:
                memorySave.append(f'{int(i1)}:11')
            ans.append(memorySave)
        return ans
    # list-int_array
    if type(input) == nbtlib.tag.List[nbtlib.tag.LongArray]:
        for i in input:
            memorySave = []
            for i1 in i:
                memorySave.append(f'{int(i1)}:12')
            ans.append(memorySave)
        return ans
    # list-long_array

    for i in input:
        ans.append(List(i))
    return ans
    # list-list



def getAns(input:str)->dict:
    """
    \n摘要
    根据已经解析的 `NBT` 数据，将其转换为本系统支持的 `字典` 形式。
    \n参数
    `input:str` 指的是是 `Minecraft Java Edition` 下的 `NBT` 的字符串形式，且其必须是一个 `Compound` 。
    \n返回值
    返回本套系统支持的格式，数据类型是 `字典` 。
    """
    # 函数声明
    
    return Compound(nbtlib.parse_nbt(input))
    # 返回值