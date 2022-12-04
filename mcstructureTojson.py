import json
import struct
import os
# 载入依赖项







class mcstructureTojson:
    def __init__(
        self,
        inputPath:str,
        CreatorMode:list = [False, '']
    )->None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `.mcstructure` 文件的路径
        `CreatorMode:list` 指的是开发者选项。列表中元素的格式为 `[是否要生成 JSON 文件:bool, 生成路径:str]`
           # 默认值为 `[False, '']`
        """
        # 函数声明

        self.inputPath = inputPath    # 文件输入路径
        self.fileContext = bytearray(b'')    # 文件内容
        self.jsonList = []    # 转义时储存数据的列表
        self.json = {}    # 转义结果
        self.CreatorMode = CreatorMode    # 开发者选项
        # 实例化

    # 实例化函数





    def MemoryProtect(self)->None:
        """
        \n摘要
        本函数用于解决超大结构可能导致的内存爆掉的问题
        \n运行机制
        当 `len(self.jsonList) >= 1000000` 时将列表内容缓存到当前目录的 `translator.tmp` 中
        \n返回值
        不会返回任何东西(`None`)
        """
        # 函数声明

        if len(self.jsonList) >= 1000000:
            with open("translator.tmp","a",encoding='utf-8') as file:
                if self.jsonList[-1] == ',':
                    del self.jsonList[-1]
                    file.write("".join(self.jsonList))
                    self.jsonList = [',']
                else:
                    file.write("".join(self.jsonList))
                    self.jsonList = []
        # 实现具体方法

    # 防止内存爆掉





    def GetInf(input:bytearray,pointer:int=0,Type:int=None)->list:
        """
        \n摘要
        取得 JSON 数据的最小化模块
        \n参数
        `input:str` 指要解析的 `bytearray` 内容
        `pointer:int` 指解析起始点(将指针移动到 `input` 的哪里)
            # 默认为 `0`
        `Type:int` 指要解析的类型(专门为列表设计，因为列表内的元素是没有 `type` 的)
        \n返回值
        返回 `list` ，格式为 `[类型:int, 名称:str, 内容:str|int|list, 指针位置:int]`
        返回的 `类型` 是 `int` ，它们(数字)分别指代以下事物
            `1(int):Bytes`
            `2(int):short`
            `3(int):int`
            `4(int):long`
            `5(float):float`
            `6(float):double`
            `7(list):byte_array`
            `8(str):string`
            `9(list):list`
            `10(dict):compound`
            `11(list):int_array`
            `12(list):long_array`
        如果解析类型属于 `9` ，即 `list` 类型，则返回的`内容`的类型是 `list` ，格式为 `[列表元素类型, 列表元素个数]`
        \n注意事项
        返回的 `内容` 或 `名称` 如果是 `str` 类型，那么在解析前，若这个被解析的 `input` 存在 `\\n` ，那么会被强制转译为 `\\\\n` ；对于 `\\n` ，则会被替换为 `-----Mark of use 0x10-----` ；对于 `"` ，则会被强制转译为 `\\"`
        """
        # 函数声明



        if Type == None:
            Type = struct.unpack('<b',input[pointer:pointer+1])[0]
            name = input[pointer+3:pointer+3+struct.unpack('<h',input[pointer+1:pointer+3])[0]].decode(encoding='UTF-8')
            name = json.dumps(name,ensure_ascii=False)[1:-1]
            if name == '':
                name = 'undefined'
            pointer = pointer + 3 + struct.unpack('<h',input[pointer+1:pointer+3])[0]
        else:
            name = None
        # 获取类型及名称



        if Type == 1:
            return [Type,name,struct.unpack('<b',input[pointer:pointer+1])[0],pointer+1]

        if Type == 2:
            return [Type,name,struct.unpack('<h',input[pointer:pointer+2])[0],pointer+2]
    
        if Type == 3:
            return [Type,name,struct.unpack('<i',input[pointer:pointer+4])[0],pointer+4]

        if Type == 4:
            return [Type,name,struct.unpack('<q',input[pointer+4:pointer+8]+input[pointer:pointer+4])[0],pointer+8]

        if Type == 5:
            return [Type,name,struct.unpack('<f',input[pointer:pointer+4])[0],pointer+4]

        if Type == 6:
            return [Type,name,struct.unpack('<d',input[pointer:pointer+8])[0],pointer+8]

        if Type == 7:
            pointerSave = pointer
            LenList = struct.unpack('<i',input[pointer:pointer+4])[0]
            pointer = pointer + 4
            ListSelf = []
            while LenList > 0:
                ListSelf.append(struct.unpack('<b',input[pointer:pointer+1])[0])
                LenList = LenList - 1
                pointer = pointer + 1
            pointer = pointerSave
            return [Type,name,ListSelf,pointer+4+struct.unpack('<i',input[pointer:pointer+4])[0]]

        if Type == 8:
            string = input[pointer+2:pointer+2+struct.unpack('<h',input[pointer:pointer+2])[0]].decode(encoding='UTF-8')
            string = json.dumps(string,ensure_ascii=False)[1:-1]
            return [Type,name,string,
            pointer+2+struct.unpack('<h',input[pointer:pointer+2])[0]]

        if Type == 9:
            return [Type,name,
            [struct.unpack('<b',input[pointer:pointer+1])[0],
            struct.unpack('<i',input[pointer+1:pointer+5])[0]],
            pointer+5]

        if Type == 10:
            return [Type,name,pointer]

        if Type == 11:
            pointerSave = pointer
            LenList = struct.unpack('<i',input[pointer:pointer+4])[0]
            pointer = pointer + 4
            ListSelf = []
            while LenList > 0:
                ListSelf.append(struct.unpack('<i',input[pointer:pointer+4])[0])
                LenList = LenList - 1
                pointer = pointer + 4
            pointer = pointerSave
            return [Type,name,ListSelf,pointer+4+4*struct.unpack('<i',input[pointer:pointer+4])[0]]

        if Type == 12:
            pointerSave = pointer
            LenList = struct.unpack('<i',input[pointer:pointer+4])[0]
            pointer = pointer + 4
            ListSelf = []
            while LenList > 0:
                ListSelf.append(struct.unpack('<q',input[pointer+4:pointer+8]+input[pointer:pointer+4])[0])
                LenList = LenList - 1
                pointer = pointer + 8
            pointer = pointerSave
            return [Type,name,ListSelf,pointer+4+8*struct.unpack('<i',input[pointer:pointer+4])[0]]

        # 返回 [类型:int, 名称:str|None, 内容:str|int|list, 指针位置:int]
    # 获取结构信息的最小化模块





    def Compound(self,input:bytearray,pointer:int=0)->int:
        """
        \n摘要
        处理 `Compound` 类型及其子成员(可调用函数本身或被 `List` 函数调用)
        \n参数
        `self` 指的是已经被实例化的项目
        `input:bytearray` 指要处理的 `bytearray`
        `pointer:int` 指处理位置(将指针移动到 `input` 的哪里)
            # 默认为 `0`
        \n运行机制
        在运行过程中向列表 `self.jsonList` 插入 `JSON` 内容(插入的是 `str` )，而非返回完整的 `JSON` 内容
        \n返回值
        返回指针位置 `pointer:int` ，用于调用自身或被 `List` 函数调用时的承上启下之衔接
        """
        # 函数声明



        while True:
            mcstructureTojson.MemoryProtect(self)
            # 防止内存爆掉

            if input[pointer:pointer+1] == bytearray(b'\x00'):
                try:
                    if self.jsonList[-1] == ',':
                        del self.jsonList[-1]
                except:
                    None
                self.jsonList.append('}')
                self.jsonList.append(',')
                pointer = pointer + 1
                if len(input) == pointer:
                    pointer = pointer - 1
                break
            # 结束递归

            ans = mcstructureTojson.GetInf(input,pointer)
            # 取得基本信息

            self.jsonList.append(f'"{ans[1]}:{ans[0]}":')
            # 插入名称

            if ans[0] == 10:
                self.jsonList.append('{')
                pointer = mcstructureTojson.Compound(self,input,ans[-1])
                continue
            # 调用组函数，如果当前是组的话

            if ans[0] == 9:
                self.jsonList.append('[')
                pointer = mcstructureTojson.List(self,input,ans[2][0],ans[2][1],ans[-1])
                continue
            # 调用列表函数，如果当前是列表的话

            if ans[0] != 8:
                self.jsonList.append(str(ans[2]))
                self.jsonList.append(',')
                pointer = ans[-1]
                continue
            else:
                self.jsonList.append(f'"{ans[2]}"')
                self.jsonList.append(',')
                pointer = ans[-1]
            # 处理非 compound、list 情况

        return pointer
    # 处理组





    def List(self,input:bytearray,Type:int,repeat:int,pointer:int)->int:
        """
        \n摘要
        处理 `list` 类型及其子成员(可调用函数本身或被 `Compound` 函数调用)
        \n参数
        `self` 指的是已经被实例化的项目
        `input:bytearray` 指要处理的 `bytearray`
        `Type:int` 指列表中的元素类型
        `repeat:int` 指列表中的元素个数(此数据将会被视为循环次数)
        `pointer:int` 指处理位置(将指针移动到 `input` 的哪里)
        \n运行机制
        在运行过程中向列表 `self.jsonList` 插入 `JSON` 内容(插入的是 `str` )，而非返回完整的 `JSON` 内容
        \n返回值
        返回指针位置 `pointer:int` ，用于调用自身或被 `Compound` 函数调用时的承上启下之衔接
        """
        # 函数声明



        while True:
            mcstructureTojson.MemoryProtect(self)
            # 防止内存爆掉

            repeat = repeat - 1
            if repeat < 0:
                try:
                    if self.jsonList[-1] == ',':
                        del self.jsonList[-1]
                except:
                    None
                self.jsonList.append(']')
                self.jsonList.append(',')
                break
            # 结束递归

            ans = mcstructureTojson.GetInf(input,pointer,Type)
            # 取得基本信息

            if ans[0] == 10:
                self.jsonList.append('{')
                pointer = mcstructureTojson.Compound(self,input,ans[-1])
                continue
            # 调用组函数，如果当前是组的话

            if ans[0] == 9:
                self.jsonList.append('[')
                pointer = mcstructureTojson.List(self,input,ans[2][0],ans[2][1],ans[-1])
                continue
            # 调用列表函数，如果当前是列表的话

            if 1 <= ans[0] <= 12:
                typeAddList = {
                    "1":":01",
                    "2":":02",
                    "4":":04",
                    "5":":05",
                    "6":":06",
                    "8":":08"
                }
                if str(ans[0]) in typeAddList:
                    self.jsonList.append(f'"{ans[2]}' + typeAddList[str(ans[0])] + '"')
                else:
                    if ans[0] == 7 or ans[0] == 11 or ans[0] == 12:
                        typeAddList2 = {
                            "7":":07",
                            "11":":11",
                            "12":":12"
                        }
                        if len(ans[2]) > 0:
                            self.jsonList.append((f'{[str(i) + typeAddList2[str(ans[0])] for i in ans[2]]}').replace('\'','"'))
                        else:
                            self.jsonList.append(f'["empty{typeAddList2[str(ans[0])]}"]')
                    else:
                        self.jsonList.append(str(ans[2]))
                self.jsonList.append(',')
                pointer = ans[-1]
            # 处理非 compound、list 情况

        return pointer
    # 处理列表





    def main(self):
        """
        \n摘要
        本函数是 `class: mcstructureTojson` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)，但转义得到的 `字典` 将会储存在 `self.json` 中
        """
        # 函数声明



        with open(self.inputPath,"r+b") as file:
            self.fileContext = bytearray(b'').join(file.readlines())
        # 获取文本信息并放入内存

        with open("translator.tmp","w+") as file:
            file.write('')
        # 重缓存文件

        mcstructureTojson.Compound(self,self.fileContext,0)
        # 取得 JSON 初始形式

        with open("translator.tmp","r+",encoding='utf-8') as file:
            self.jsonList = '{"Root' + (('{' + "".join(file.readlines()) + "".join(self.jsonList))[:-1]).split('{"undefined',maxsplit=1)[1]
        # 取得正确的 JSON

        os.remove('translator.tmp')
        # 删除缓存文件

        self.json = json.loads(self.jsonList)
        # 生成字典形式

        del self.jsonList
        del self.fileContext
        # 删除放入到内存的结构

        if self.CreatorMode[0] == True:
            with open(self.CreatorMode[1],"w+",encoding='UTF-8') as file:
                file.write(json.dumps(self.json,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
        # 开发者选项

    # 主函数