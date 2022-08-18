import json
import struct
import os
import share
# 载入依赖项



with open("input.mcstructure","r+b") as file:
    print('进度：正在将结构读入内存……')
    fileContext = bytearray(b'').join(file.readlines())
    print('进度：已成功将结构放入内存！')
# 获取文本信息并放入内存
with open("translator.tmp","w+") as file:
    file.write('')
    print('警告：已在当前目录下生成 translator.tmp 缓存文件，翻译期间请不要删除！')
# 重缓存文件



def MemoryProtect():
    """
    \n摘要
    本函数用于解决超大结构可能导致的内存爆掉的问题
    \n运行机制
    当`len(jsonList) >= 1000000`时将列表内容缓存到当前目录的`translator.tmp`中
    \n返回值
    不会返回任何东西(`None`)
    """
    global jsonList
    # 声明全局变量
    if len(jsonList) >= 1000000:
        with open("translator.tmp","a",encoding='utf-8') as file:
            if jsonList[-1] == ',':
                del jsonList[-1]
                file.write("".join(jsonList))
                jsonList = [',']
            else:
                file.write("".join(jsonList))
                jsonList = []
# 防止内存爆掉

def GetInf(input:bytearray,pointer:int=0,Type:int=None):
    """
    \n摘要
    取得 JSON 数据的最小化模块
    \n参数
    `input:str` 指要解析的`bytearray`内容
    `pointer:int` 指解析起始点(将指针移动到`input`的哪里)
        # 默认为`0`
    `Type:int` 指要解析的类型(专门为列表设计，因为列表内的元素是没有`type`的)
    \n返回值
    返回`list`，格式为`[类型:str|int, 名称:str|None, 内容:str|int|list, 指针位置:int]`
    如果解析结果应被丢弃(只要不是这些: `bytes`、`short`、`int`、`string`、`list`和`component`)，则返回的`类型`是`str(int)`，否则返回`int`
    对于返回的`类型`，即:可用`int()`函数变为数字的数字或字符串，它们(数字)分别指代以下事物
        `1(int):Bytes`
        `2(short):int`
        `3(int):int`
        `4:舍弃`
        `5:舍弃`
        `6:舍弃`
        `7:舍弃`
        `8(str):string`
        `9(list):list`
        `10(dict):component`
        `11:舍弃`
        `12:舍弃`
    如果解析类型属于`9`，即:`list`类型，则返回的`内容`的类型是`list`，格式为`[列表元素类型, 列表元素个数]`，否则返回的`内容`的类型是`str`(对于`字符串`)或`int`(对于`整数`)或`None`(其他)
    \n注意事项
    返回的`内容`如果是`str`类型，那么在解析前，若这个被解析的`input`存在`\\n`，那么会被强制转译为`\\\\n`；对于`\\n`，则会被替换为`-----Mark of use 0x10-----`；对于`"`，则会被强制转译为`\\"`
    返回的`名称`同理，因为它是`内容:str`类型，因此本处不再赘述
    """
    # 函数声明
    if Type == None:
        Type = ord(input[pointer:pointer+1])
        name = input[pointer+3:pointer+3+struct.unpack('<H',input[pointer+1:pointer+3])[0]].decode(encoding='UTF-8')
        name = name.replace('\\n','-----Mark of use 0x10-----')
        name = name.replace('\n','\\n')
        name = name.replace('"','\\"')
        if name == '':
            name = 'undefined'
        pointer = pointer + 3 + struct.unpack('<H',input[pointer+1:pointer+3])[0]
    else:
        name = None
    # 获取类型及名称
    if Type == 1:
        return [Type,name,ord(input[pointer:pointer+1]),pointer+1]
    if Type == 2:
        return [Type,name,struct.unpack('<h',input[pointer:pointer+2])[0],pointer+2]
    if Type == 3:
        return [Type,name,struct.unpack('<i',input[pointer:pointer+4])[0],pointer+4]
    if Type == 8:
        string = input[pointer+2:pointer+2+struct.unpack('<H',input[pointer:pointer+2])[0]].decode(encoding='UTF-8')
        string = string.replace('\\n','-----Mark of use 0x10-----')
        string = string.replace('\n','\\n')
        string = string.replace('"','\\"')
        return [Type,name,string,
        pointer+2+struct.unpack('<H',input[pointer:pointer+2])[0]]
    if Type == 9:
        return [Type,name,
        [ord(input[pointer:pointer+1]),
        struct.unpack('<i',input[pointer+1:pointer+5])[0]],
        pointer+5]
    if Type == 10:
        return [Type,name,pointer]
    if Type == 4 or Type == 6:
        return [str(Type),name,pointer+8]
    if Type == 5:
        return [str(Type),name,pointer+4]
    if Type == 7:
        return [str(Type),name,pointer+4+struct.unpack('<i',input[pointer:pointer+4])[0]]
    if Type == 11:
        return [str(Type),name,pointer+4+4*struct.unpack('<i',input[pointer:pointer+4])[0]]
    if Type == 12:
        return [str(Type),name,pointer+4+8*struct.unpack('<i',input[pointer:pointer+4])[0]]
    # 返回 [类型:str|int, 名称:str|None, 内容:str|int|list, 指针位置:int]
# 获取结构信息的最小化模块

def Component(input:bytearray,pointer:int=0):
    """
    \n摘要
    处理`component`类型及其子成员(可调用函数本身或被`List`函数调用，未限制递归深度)
    \n参数
    `input:bytearray` 指要处理的`bytearray`
    `pointer:int` 指处理位置(将指针移动到`input`的哪里)
        # 默认为`0`
    \n运行机制
    在运行过程中向列表`jsonList`(是全局变量)插入`JSON`内容(插入的是`str`)，而非返回完整的`JSON`内容
    \n返回值
    返回指针位置`pointer:int`，用于调用自身或被`List`函数调用时的承上启下之衔接
    """
    # 函数声明
    global jsonList
    global jumpList
    # 声明全局变量
    while True:
        MemoryProtect()
        # 防止内存爆掉
        if input[pointer:pointer+1] == bytearray(b'\x00'):
            try:
                if jsonList[-1] == ',':
                    del jsonList[-1]
            except:
                None
            jsonList.append('}')
            jsonList.append(',')
            pointer = pointer + 1
            if len(input) == pointer:
                pointer = pointer - 1
            break
        # 结束递归
        ans = GetInf(input,pointer)
        # 取得基本信息
        if type(ans[0]) != int:
            pointer = ans[-1]
            jumpList.append(ans)
            continue
        # 跳过无关内容
        jsonList.append(f'"{ans[1]}:{ans[0]}":')
        # 插入名称
        if ans[0] == 10:
            jsonList.append('{')
            pointer = Component(input,ans[-1])
            continue
        # 调用组函数，如果当前是组的话
        if ans[0] == 9:
            jsonList.append('[')
            pointer = List(input,ans[2][0],ans[2][1],ans[-1])
            continue
        # 调用列表函数，如果当前是列表的话
        if ans[0] != 8:
            jsonList.append(str(ans[2]))
            jsonList.append(',')
            pointer = ans[-1]
            continue
        else:
            jsonList.append(f'"{ans[2]}"')
            jsonList.append(',')
            pointer = ans[-1]
        # 处理 short, bytes, int, string 情况
    return pointer
# 处理组

def List(input:bytearray,Type:int,repeat:int,pointer:int):
    """
    \n摘要
    处理`list`类型及其子成员(可调用函数本身或被`Component`函数调用，未限制递归深度)
    \n参数
    `input:bytearray` 指要处理的`bytearray`
    `Type:int` 指列表中的元素类型
    `repeat:int` 指列表中的元素个数(此数据将会被视为循环次数)
    `pointer:int` 指处理位置(将指针移动到`input`的哪里)
    \n运行机制
    在运行过程中向列表`jsonList`(是全局变量)插入`JSON`内容(插入的是`str`)，而非返回完整的`JSON`内容
    \n返回值
    返回指针位置`pointer:int`，用于调用自身或被`Component`函数调用时的承上启下之衔接
    """
    # 函数声明
    global jsonList
    global jumpList
    # 声明全局变量
    while True:
        MemoryProtect()
        # 防止内存爆掉
        repeat = repeat - 1
        if repeat < 0:
            try:
                if jsonList[-1] == ',':
                    del jsonList[-1]
            except:
                None
            jsonList.append(']')
            jsonList.append(',')
            break
        # 结束递归
        ans = GetInf(input,pointer,Type)
        # 取得基本信息
        if type(ans[0]) != int:
            pointer = ans[-1]
            jumpList.append(ans)
            continue
        # 跳过无关内容
        if ans[0] == 10:
            jsonList.append('{')
            pointer = Component(input,ans[-1])
            continue
        # 调用组函数，如果当前是组的话
        if ans[0] == 9:
            jsonList.append('[')
            pointer = List(input,ans[2][0],ans[2][1],ans[-1])
            continue
        # 调用列表函数，如果当前是列表的话
        if ans[0] != 8:
            jsonList.append(str(ans[2]))
            jsonList.append(',')
            pointer = ans[-1]
            continue
        else:
            jsonList.append(f'"{ans[2]}"')
            jsonList.append(',')
            pointer = ans[-1]
        # 处理 short, bytes, int, string 情况
    return pointer
# 处理列表



jsonList = []
jumpList = []
# 创建列表
print('进度：正在转换格式……')
Component(fileContext,0)
# 取得 JSON 初始形式
with open("translator.tmp","r+",encoding='utf-8') as file:
    share.mcs = '{"Root' + (('{' + "".join(file.readlines()) + "".join(jsonList))[:-1]).split('{"undefined',maxsplit=1)[1]
# 取得正确的 JSON
print('进度：已删除 translator.tmp 缓存文件')
os.remove('translator.tmp')
# 删除缓存文件

###
while True:
    print('是否在当前目录下输出 MCStructure 的 JSON 形式？\n请回答 Yes 或 No')
    CreatorMode = input()
    if (CreatorMode == 'Yes') or (CreatorMode == 'yes') or (CreatorMode == 'y') or (CreatorMode == 'Y'):
        with open("ans.json","w+b") as file:
            file.write(share.mcs.encode(encoding='utf-8'))
        print('完成：已成功在当前目录下生成 ans.json 文件.')
        break
    if (CreatorMode == 'No') or (CreatorMode == 'no') or (CreatorMode == 'n') or (CreatorMode == 'N'):
        break
    print('错误：请不要答非所问.\n\n\n')
###

share.mcs = json.loads(share.mcs)
print('进度：已成功转换为 JSON 格式！')
del fileContext
del jsonList
# 生成字典形式并删除放入到内存的结构