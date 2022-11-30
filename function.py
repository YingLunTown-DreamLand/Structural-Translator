import share
import blockData.blockList
import Api.JsonToNBT.JsonTranslate
import nbtlib
import time, random, os
from nbtlib.tag import *
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





def outputNBT(input:dict|bytes,location:int)->bytes:
    """
    \n摘要
    访问对应方块下的 `方块实体` 数据，并返回二进制下的 NBT 信息
    \n参数
    `input:dict|list` 指的是装有 NBT 信息的字典或无法被解析为 NBT 的二进制字节串
    `location:int` 指的是这个方块在密集矩阵下的角标
    \n返回值
    返回一个 `Bytes` ，其记录着二进制下的 NBT 信息
    """
    # 函数声明



    NBTdata = input["Root:10"]["structure:10"]["palette:10"][
        "default:10"]["block_position_data:10"][f"{location}:10"]["block_entity_data:10"]
    # 获取方块实体数据

    if type(NBTdata) == dict:
        NBTdata = Api.JsonToNBT.JsonTranslate.JSONCompound(NBTdata)
        # 转换为 NBT 库下的格式
        return nbtlib.serialize_tag(NBTdata).encode(encoding='utf-8')
        # 返回值
    # 如果 NBTdata 是字典

    if type(NBTdata) == bytes:
        return NBTdata
    # 如果 NBTdata 已经是 bytes





def showStates(
    progress:str,
    provide:list,    # [工作目录的绝对路径:str, 文件输入路径: str, 文件输出路径: str, 当前进度: int, 总进度: int]
    officalRun:list = [],    # [executeStates: int, areaPosStates[0]: int, areaPosStates[1]: int, areaPos: list]
) -> None:
    """
    \n摘要
    本函数用于在控制台打印程序执行进度。
    \n参数
    `progress:str` 指的是当前正在做或刚刚做完的事情，是一个字符串，分别对应本函数中 `indexDict` 中的键
    `provide:list` 指的是处理进度列表，格式为 `[全局配置中的“文件搜索路径”: str, 文件输入路径: str, 文件输出路径: str, 当前进度: int, 总进度: int]`
    `officalRun:list` 指的是正式翻时传入的进度数据，格式为 `[ 执行次数: int, 横轴区块数: int, 纵轴区块数: int, 当前正在处理的区块: [横轴角标: int, 纵轴角标: int] ]`
       # 默认值为 `[]`
    \n返回值
    不返回任何东西，即 `None` 。
    """
    # 函数声明



    indexDict = {
        "get structure info / start": "\033[0;33;2018m正在解析结构……\033[0m",    # 取得结构信息
        "get structure info / end": ["\033[0;33;2018m已成功解析结构.\033[0m"],    # 取得结构信息

        "check structure / start": "\033[0;33;2018m正在检查结构完整性……\033[0m",    # 检查结构完整性
        "check structure / end": ["\033[0;33;2018m结构完整.\033[0m"],    # 检查结构完整性

        "get block pool / start": ["\033[0;33;2018m正在提取方块池……\033[0m"],    # 提取方块池
        "get block pool / end": ["\033[0;33;2018m已成功获取方块池.\033[0m"],    # 提取方块池

        "get json info / start": "\033[0;33;2018m正在解析 JSON 文件……\033[0m",    # 取得 JSON 信息
        "get json info / end": ["\033[0;33;2018m已成功解析文件.\033[0m"],    # 取得 JSON 信息

        "replaceBlockID / start": ["\033[0;33;2018m正在替换方块 ID ……\033[0m"],    # 组件 - 替换方块ID
        "replaceBlockID / end": ["\033[0;33;2018m已成功替换方块 ID .\033[0m"],    # 组件 - 替换方块ID

        "officalRun / start": 'math',    # 翻译进行时
        "officalRun / end": ["\033[0;33;2018m翻译完成.\033[0m"],    # 翻译进行时

        "writing / start": "\033[0;33;2018m正在将翻译结果写入到文件……\033[0m",    # 写入结果到文件
        "writing / end": ["\033[0;33;2018m已完成写入到文件.\033[0m"],    # 写入结果到文件

        "down": f"\033[0;33;2018m此文件处理完成，结果保存在\033[0m \033[0;36;2018m{provide[2]}\033[0m \033[0;33;2018m处.\033[0m",    # 完成
        "failed": ["\033[0;31;2018m当前文件处理失败.\033[0m"]    # 失败
    }
    # 定义查找表



    provide[0] = os.path.normpath(provide[0]).replace('\\','/')
    provide[1] = os.path.normpath(provide[1]).replace('\\','/')
    provide[2] = os.path.normpath(provide[2]).replace('\\','/')
    # 格式化路径



    provide[1] = provide[1].replace(provide[0] + '/','',1)
    # 提取输入路径的相对路径



    print("\r" + " " * share.showStates,end="")
    String = f"\r\033[0;37;45m{provide[3]}/{provide[4]} - {provide[1]}\033[0m"
    print(String,end="")
    share.showStates = len(String)
    # 显示文件基本信息

    
    if progress == 'down' or progress == 'failed':
        enter = "\n"
    else:
        enter = ""
    # 是否换行


    progress = indexDict[progress]

    if progress == 'math':
        rate = str(( officalRun[0] / (officalRun[1] * officalRun[2]) ) * 100)
        String = f'翻译文件 - 当前进度 {rate} % | 当前正在处理区块 {officalRun[3]} | 总区块数 {officalRun[1] * officalRun[2]}'
        String = f" \033[0;33;2018m{String}\033[0m"
        print(String,end=enter,flush=True)
        share.showStates = len(String) + share.showStates

    elif type(progress) == str:
        print(" " + progress,end=enter,flush=True)
        share.showStates = len(progress) + share.showStates

    elif type(progress) == list:
        print(" " + progress[0],end=enter,flush=True)
        share.showStates = len(progress[0]) + share.showStates
        time.sleep(random.randint(5,10) / 10)

    # 显示后方文本部分





def outputJsonNBT_Compound(input:nbtlib.tag.Compound) -> dict:
    """
    \n摘要
    本函数用于输出 `nbtlib.tag.Compound` 的纯 `JSON` 形式，且不会记录数据类型。
    \n参数
    `input:nbtlib.tag.Compound` 指的是需要被转换为纯 `JSON` 形式的 `复合标签`
    \n返回值
    返回 `input:nbtlib.tag.Compound` 对应的 `dict` 且不记录数据类型。
    """
    # 函数声明



    ans = {}


    for i in input:
        if type(input[i]) == Byte:
            if int(input[i]) != 0 and int(input[i]) != 1:
                ans[i] = int(input[i])
            else:
                ans[i] = bool(input[i])
            continue
        # Byte

        if type(input[i]) == Short or type(input[i]) == Int or type(input[i]) == Long:
            ans[i] = int(input[i])
            continue
        # Short, Int, Long

        if type(input[i]) == Float or type(input[i]) == Double:
            ans[i] = float(input[i])
            continue
        # Float, Double

        if type(input[i]) == ByteArray or type(input[i]) == IntArray or type(input[i]) == LongArray:
            ans[i] = [int(i) for i in input[i]]
            continue
        # byte_array, int_array, long_array

        if type(input[i]) == String:
            ans[i] = str(input[i])
            continue
        # String

        if type(input[i]) == Compound:
            ans[i] = outputJsonNBT_Compound(input[i])
            continue
        # Compound

        ans[i] = outputJsonNBT_List(input[i])
        # List


    return ans





def outputJsonNBT_List(input:List[any]) -> list:
    """
    \n摘要
    本函数用于输出 `nbtlib.tag.List[any]` 的纯 `list` 形式，且不会记录数据类型。
    \n参数
    `nbtlib.tag.List[any]` 指的是需要被转换为纯 `list` 形式的 `列表`
    \n返回值
    返回 `nbtlib.tag.List[any]` 对应的 `list` 且不记录数据类型。
    """
    # 函数声明


    if len(input) == 0:
        return []
    # while input = []

    if type(input[0]) == Byte:
        ByteList = [int(i) for i in input]
        maxValue = max(ByteList)
        minValue = min(ByteList)
        if (maxValue != 0 and maxValue != 1) or (minValue != 0 and minValue != 0):
            return [int(i) for i in input]
        else:
            return [bool(i) for i in input]
    # Byte

    if type(input[0]) == Short or type(input[0]) == Int or type(input[0]) == Long:
        return [int(i) for i in input]
    # Short, Int, Long

    if type(input[0]) == Float or type(input[0]) == Double:
        return [float(i) for i in input]
    # Float, Double

    if type(input[0]) == ByteArray or type(input[0]) == IntArray or type(input[0]) == LongArray:
        return [[int(i1) for i1 in i] for i in input]
    # byte_array, int_array, long_array

    if type(input[0]) == String:
        return [str(i) for i in input]
    # String

    if type(input[0]) == Compound:
        return [outputJsonNBT_Compound(i) for i in input]
    # Compound

    return [outputJsonNBT_List(i) for i in input]
    # List