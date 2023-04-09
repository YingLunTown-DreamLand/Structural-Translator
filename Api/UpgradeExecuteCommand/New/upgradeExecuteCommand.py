class CommandReader:
    """
    CommandReader 是一个命令阅读器，用于从中阅读 Execute 命令
    """

    def __init__(self,context:str,pointer:int) -> None:
        """
        概述
            此函数用于初始化一个命令阅读器，其内部包含一条完整的命令和阅读进度。
        参数
            context:str | 一个完整的 execute 命令
            pointer:int | 用于指示当前阅读进度
        """
        self.context:str = context
        self.pointer:int = pointer
    
    def read(self, length:int) -> str:
        """
        概述
            从 self.context 的 self.pointer 处阅读 length 个字符。
            当 self.pointer 为负数时，将会自动修正到 0 并阅读 length 个字符
        参数
            length:int | 要阅读的长度
        """
        if self.pointer < 0:
            self.pointer = 0
        string = self.context[self.pointer:self.pointer+length]
        self.pointer = self.pointer + length
        return string
    
    def jumpSpace(self,jumpSlash:bool):
        """
        概述
            持续阅读直到读到非空格或 / 字符
        参数
            jumpSlash:bool | 为真时将会同时跳过字符 "/" 但只会跳过一次
        """
        slashIsJumped = False
        while True:
            readAns = self.read(1)
            if jumpSlash == True and readAns == "/" and slashIsJumped == False:
                slashIsJumped = False
                jumpSlash = False
                continue
            if readAns != " ":
                self.pointer = self.pointer - 1
                break
    
    def index(self,search:str) -> list:
        """
        概述
            从 self.context 的 self.pointer 处查找 search
        参数
            search:str | 要查找的字符串
        返回值
            返回一个列表且只有两个元素。
            其第一项代表 search 在 self.context 的起始位置，
            其第二项代表查找结果，且只有为真时代表找到，否则反之
        """
        location =  self.context.find(search,self.pointer)
        if location == -1:
            return [-1,False]
        return [location,True]
    
    def highSearching(self,searchList:list[str]) -> list:
        """
        概述
            枚举 searchList 中的每个字符串并得到
            距离 self.pointer 最近的字符串，
            同时在找到目标字符串时更新阅读器的阅读进度
        参数
            searchList:list[str] | 一个列表且其内部只装有字符串，对应上文中的列表
        返回值
            返回一个列表且只有三个元素。
            self.context[第一项: 第二项] 代表找到的距离 self.pointer 最近的字符串。
            第三项代表查找结果，且只有为真时代表找到，否则反之
        """
        tmp = [] # tmp = [ [0,1], [2,3] ]
        returnValue = [] # ans = [0, 1]
        minToRecord = 2147483647
        # init values
        for i in searchList:
            ans = self.index(i)
            if ans[1] == False:
                continue
            tmp.append([ans[0],ans[0]+len(i)])
        # get each result
        for i in tmp:
            if i[1] < minToRecord:
                returnValue = i
                minToRecord = i[1]
        # get the min values
        if len(returnValue) > 0:
            self.pointer = returnValue[1]
            return [returnValue[0],returnValue[1],True]
        else:
            return [-1,-1,False]
        # return
    
    def getRightBarrier(self,mode:int) -> list:
        """
        概述
            从 self.context 的 self.pointer 处寻找下一个边界符号，
            也就是 "]" 或 "\"" 并返回其所在位置加一的值。
            当找到时，将同时更新阅读器的阅读进度
        参数
            mode:int | 指代寻找模式，为 0 时寻找 "]" ，否则寻找 "\""
        返回值
            返回一个列表且只有两个元素。
            其第一项代表边界符号在 self.context 中所在位置加一的值，
            其第二项代表查找结果，且只有为真时代表找到，否则反之
        """
        tmp = self.pointer
        def exitFunc(value:int,states:bool):
            if states == False:
                self.pointer = tmp
            else:
                self.pointer = value
            return [value,states]
        # init values
        if mode == 0:
            while True:
                quotationMark = self.index('"')
                rightBarrier = self.index(']')
                #
                if rightBarrier[1] == False:
                    return exitFunc(-1,False)
                if quotationMark[1] == False:
                    return exitFunc(rightBarrier[0]+1,True)
                #
                elif quotationMark[0] < rightBarrier[0]:
                    self.pointer = quotationMark[0]+1
                    tmpFindAns = self.getRightBarrier(1)
                    if tmpFindAns[1] == False:
                        return exitFunc(-1,False)
                else:
                    return exitFunc(rightBarrier[0]+1,True)
        # find "]"
        else:
            while True:
                readAns = self.read(1)
                match readAns:
                    case '':
                        return exitFunc(-1,False)
                    case '\\':
                        self.read(1)
                        continue
                    case '"':
                        returnValue = self.pointer
                        return exitFunc(returnValue,True)
        # find "\""

class SinglePos:
    """
    SinglePos 类用于描述一个单个的坐标
    """

    def __init__(self) -> None:
        """
        概述
            此函数用于初始化一个坐标，其内部包含以下信息
                header:str | 指代坐标的前缀，也就是 "^"、"~"、"+" 和 "-"
                number:int|float | 指代坐标的实际值(可正可负)，且类型只可能为 int 或 float
                string:str | 该坐标的字符串表达形式
                self.isNotNumber:bool | 用于标识该坐标是否不为纯数字，为真时不为纯数字，否则反之
        """
        self.header:str = ""
        self.number:int|float = 0
        self.string:str = "0"
        self.isNotNumber:bool = False
    
    def format(self) -> None:
        """
        概述
            将规范且最简的形式的坐标保存到 self.string 中
        """
        self.header.replace(' ','',-1)
        # remove all the space
        if type(self.number) == int:
            numberString = str(int(self.number))
        else:
            numberString = str(float(self.number))
        # get correct string of the number
        if self.isNotNumber == True and (numberString == '0' or numberString == '0.0' or numberString == '-0.0'):
            numberString = ''
        if self.header == '+' or f'{self.header}{numberString}' == '-0.0' or f'{self.header}{numberString}' == '-0':
            header = ''
        else:
            header = self.header
        # make it minimization
        self.string = f'{header}{numberString}'
        # write datas
    
    def parse(self,reader:CommandReader) -> bool:
        """
        概述
            从 reader.context 的 reader.pointer 处解析一个坐标
            并在解析成功时更新 reader 的阅读进度。
            解析结果不会直接返回，而是保存在 self.string 中
        参数
            reader:CommandReader | 指代一个命令阅读器，用于从中阅读 Execute 命令
        返回值
            返回一个布尔值以指代解析的结果，且为真时代表解析成功，
            为假时代表解析失败
        """
        tmp = reader.pointer
        def failedFunc():
            reader.pointer = tmp
            return False
        # init values
        reader.jumpSpace(False)
        # jump space
        string = reader.read(1)
        # read header
        if string == '~' or string == '^':
            self.isNotNumber = True
            self.header = string
        elif string == '+' or string == '-':
            self.isNotNumber = False
            self.header = string
        else:
            self.isNotNumber = False
            self.header = ''
        # set header
        if self.header == '':
            reader.pointer = reader.pointer - 1
        # correct the pointer of reader
        startLocation = reader.pointer
        while True:
            string = reader.read(1)
            if string != '0' and string != '1' and string != '2' and (
            string != '3') and string != '4' and string != '5' and (
            string != '6') and string != '7' and string != '8' and (
            string != '9') and string != '.' and string != '+' and (
            string != '-'):
                reader.pointer = reader.pointer - 1
                break
        numberString = reader.context[startLocation:reader.pointer]
        if numberString.find('.') > 0:
            try:
                if numberString[-1] == '.':
                    return failedFunc()
                self.number = float(numberString)
            except:
                return failedFunc()
        else:
            try:
                if numberString == '':
                    self.number = int(0)
                else:
                    self.number = int(numberString)
            except:
                return failedFunc()
        # get the numbers
        self.format()
        return True
        # return

class Pos:
    """
    类 Pos 用于描述一个完整的坐标
    """

    def __init__(self,posx:SinglePos,posy:SinglePos,posz:SinglePos) -> None:
        """
        概述
            此函数用于初始化一个完整的坐标
        参数
            posx:SinglePos | X 轴坐标
            posx:SinglePos | Y 轴坐标
            posx:SinglePos | Z 轴坐标
            self.verified:bool | 标识坐标是否完整，为真时代表完整，否则反之
        """
        self.posx:SinglePos = posx
        self.posy:SinglePos = posy
        self.posz:SinglePos = posz
        self.verified:bool = False
    
    def Checker(self):
        """
        概述
            此函数用于检验 self 中保存的三个坐标所
            构成的一个完整坐标是否满足语法规则。
            如果满足，则 self.verified 会被更新为
            True ，否则会被更新为 False
        """
        if self.posx.header == '^' or self.posy.header == '^' or (
        self.posz.header == '^'):
            if self.posx.header != '^' or self.posy.header != '^' or (
            self.posz.header != '^'):
                self.verified = False
                return
        self.verified = True

    def format(self) -> str:
        """
        概述 & 返回值
            返回字符串形式的坐标(规范格式)
        """
        return f'{self.posx.string} {self.posy.string} {self.posz.string}'
        # write datas

def searchForHeader(c:CommandReader,header:str,jumpSlash:bool) -> bool:
    """
    概述 & 返回值
        从 c.context 的 c.pointer 处寻找命令前缀 header 。
        当找到时，返回真并且修改阅读进度，否则返回假。
    参数
        c:CommandReader | 指代一个命令阅读器，用于从中阅读 Execute 命令
        header:str | 指代要查找的命令前缀
        jumpSlash:bool | 是否要跳过斜杠 "/" ，为真时代表需要跳过，否则反正
    """
    c.jumpSpace(jumpSlash)
    tmp = c.pointer
    headerGet = c.read(len(header)).lower()
    # jump space and read command header
    if headerGet == header:
        return True
    else:
        c.pointer = tmp
        return False
    # return

def getSelector(c:CommandReader) -> list:
    """
    概述
        从 c.context 的 c.pointer 处寻找选择器，
        并在找到时更新阅读器的阅读进度
    参数
        c:CommandReader | 指代一个命令阅读器，用于从中阅读 Execute 命令
    返回值
        返回一个列表且只有两个元素。
        其第一项代表找到的选择器，是一个字符串，
        其第二项代表查找结果，且只有为真时代表找到，否则反之
    """
    tmp = c.pointer
    def failedFunc():
        c.pointer = tmp
        return [-1,False]
    # init values
    c.jumpSpace(False)
    # jump space
    selectorStartLocation = c.pointer
    readAns = c.read(1)
    # read header
    if readAns == '@':
        findAns = c.highSearching(
            [
                "s", "a", "p", "e", "r", "initiator", "c", "v"
            ]
        )
        if findAns[2] == False:
            return failedFunc()
        if findAns[0] != selectorStartLocation+1:
            return failedFunc()
        selectorEndLocation = c.pointer
        # try to find @...
        c.jumpSpace(False)
        # jump space
        string = c.read(1)
        # read ... in @...
        if string == '[':
            parameterStartLocation = c.pointer - 1
            parameterEndLocation = c.getRightBarrier(0)
            if parameterEndLocation[1] == False:
                return failedFunc()
            return [
                f'{c.context[selectorStartLocation:selectorEndLocation]}{c.context[parameterStartLocation: parameterEndLocation[0]]}',
                True
            ]
            # @...[...]
        else:
            c.pointer = findAns[1]
            return [
                c.context[selectorStartLocation: findAns[1]],
                True
            ]
            # @...
        # @...[...] or @...
    elif readAns == '"':
        findAns = c.getRightBarrier(1)
        if findAns[1] == False:
            return failedFunc()
        return [
            c.context[selectorStartLocation: findAns[0]],
            True
        ]
        # "..."
    else:
        if tmp == selectorStartLocation:
            return failedFunc()
        findAns = c.highSearching([" ","~","^","+"])
        if findAns[2] == False:
            return failedFunc()
        c.pointer = c.pointer-1
        return [
            c.context[selectorStartLocation: c.pointer],
            True
        ]
        # ...

def getPos(c:CommandReader) -> Pos:
    """
    概述
        从 c.context 的 c.pointer 处寻找一组三维坐标，
        并在每解析一个坐标时更新阅读器的阅读进度。
        特别地，在最终检验语法时发现了语法错误，
        则阅读器的阅读进度会回溯到调用此函数前的状态
    参数
        c:CommandReader | 指代一个命令阅读器，用于从中阅读 Execute 命令
    返回值
        返回一个完整的坐标 Pos
    """
    ans = Pos(
        SinglePos(),
        SinglePos(),
        SinglePos()
    )
    tmp = c.pointer
    # init values
    for i in range(0,3):
        newPos = SinglePos()
        successStates = newPos.parse(c)
        if successStates == False:
            return ans
        match i:
            case 0:
                ans.posx = newPos
            case 1:
                ans.posy = newPos
            case 2:
                ans.posz = newPos
    # get posx, posy, posz
    ans.Checker()
    if ans.verified == False:
        c.pointer = tmp
    return ans
    # return

def detectBlock(c:CommandReader) -> list:
    """
    概述
        从 c.context 的 c.pointer 处解析一组 detect block 信息，
        并在成功解析时更新阅读器的阅读进度
    参数
        c:CommandReader | 指代一个命令阅读器，用于从中阅读 Execute 命令
    返回值
        返回一个列表且只有三个元素。
        其第一项代表是否找到了 detect block 信息，为真时代表找到，否则没有找到；
        其第二项是一个字符串，包含了 detect block 信息在新语法下的表示；
        其第三项表示 detect block 信息的解析结果，为真时代表解析成功，否则反之
    """
    if searchForHeader(c,'detect',False) == True:
        tmp = c.pointer
        def failedFunc():
            c.pointer = tmp
            return [True,"",False]
        # init values
        position = getPos(c)
        if position.verified == False:
            return failedFunc()
        posString = position.format()
        # pos
        save = c.pointer
        c.jumpSpace(False)
        if c.pointer == save and position.posz.isNotNumber == False:
            return failedFunc()
        # for example, "~~ +5air 0" is wrong
        blockNameAndblockData = []
        for _ in range(0,2):
            c.jumpSpace(False)
            startLocation = c.pointer
            findAns = c.index(' ')
            if findAns[1] == False:
                return failedFunc()
            blockNameAndblockData.append(c.context[startLocation:findAns[0]])
            c.pointer = findAns[0]
        # block name and block data
        c.jumpSpace(True)
        # jump space and slash
        return [
            True,
            f' if block {posString} {blockNameAndblockData[0]} {blockNameAndblockData[1]}',
            True
        ]
        # return
    else:
        return [False,"",False]
        # return

def upgrade(command:str) -> list:
    """
    概述
        将 command 升级为新格式
    参数
        command:str | 指代待升级的 execute 命令
    返回值
        返回一个列表且只有四个元素。
        其第一项代表升级结果，是一个字符串；
        其第二项代表升级状态，为真时表示升级成功，否则失败；
        其第三项代表错误信息，是一个字符串；
        其第四项代表指令中可能错误的字段，是一个字符串
    """
    ans = []
    newReader = CommandReader(command,0)
    def failedFunc(errInfo:str):
        return [
            "",
            False,
            errInfo,
            f"{newReader.context[newReader.pointer:]}"
        ]
    # init values
    while True:
        if searchForHeader(newReader,'execute',True):
            selector = getSelector(newReader)
            if selector[1] == False:
                return failedFunc(f"无法解析位于 {newReader.pointer} 处的选择器及其参数，请更正格式")
            # selector
            tmp = newReader.pointer
            newReader.jumpSpace(False)
            save = newReader.pointer
            # check prepare
            pos = getPos(newReader)
            if pos.verified == False:
                return failedFunc(f"无法解析位于 {newReader.pointer} 处的坐标，请更正格式")
            posString = pos.format()
            # pos
            if tmp == save and pos.posx.isNotNumber == False and pos.posx.header == '' and selector[0][0] == "@" and selector[0][-1] != "]":
                newReader.pointer = tmp - 5
                return failedFunc(f"位置 {newReader.pointer} 附近发生了语法错误，请更正格式")
            # for example, "@s1 ~5~3" is wrong
            tmp = newReader.pointer
            newReader.jumpSpace(False)
            if tmp == newReader.pointer and pos.posz.isNotNumber == False:
                newReader.pointer = newReader.pointer - 5
                return failedFunc(f"位置 {newReader.pointer} 附近发生了语法错误，请更正格式")
            # for example, "~~ +5w @s" is wrong
            tmp = newReader.pointer
            detect = detectBlock(newReader)
            if detect[0] == True and detect[2] == False:
                return failedFunc(f"无法解析位于 {newReader.pointer} 处的 Detect Block 数据，请更正格式")
            # detect
            if posString == "~ ~ ~" or posString == "^ ^ ^":
                ans.append(
                    f"as {selector[0]} at @s{detect[1]} "
                )
            else:
                ans.append(
                    f"as {selector[0]} at @s positioned {posString}{detect[1]} "
                )
            # submit subcommand
        else:
            ans.append(newReader.context[newReader.pointer:])
            break
    # get all the subcommand
    if len(ans) <= 1:
        return ["".join(ans),True,"",""]
    else:
        ans[-1] = f'run {ans[-1]}'
        return [
            f'execute {"".join(ans)}',
            True,"",""
        ]
    # return

def main(commandLine:str) -> str:
    """
    概述
        这是一个示例函数，用于将诸如 `trexecute@s~~~say 1` 之类的字符串转换为
        新格式
    参数
        commandLine:str | 用户在 QQ 群发送的消息
    返回值
        返回一个字符串，包含了各种各样的信息
    """
    if commandLine[0:2] == "tr":
        commandLine = commandLine[2:]
        get = upgrade(commandLine)
        if get[1] == False:
            return f"升级 Execute 命令时发生了错误，具体如下。\n错误信息：{get[2]}\n错误字段：{get[3]}"
        else:
            return get[0]
    else:
        return ""

# test1
print(main('trexecute @s ~ ~ ~ say 123'))
print(main('trexecute @s -1 -5 ~ say'))
print(main('trexecute@s~~~say'))
print(main('trexecute t ~ ~ ~ say'))
print(main('trexecute MYNAMEISHAPPY2018new 0 0 0 say'))
print(main('trexecute MYNAMEISHAPPY2018new0 2 0 0 say'))
print(main('trexecute @a[name="MYNAMEISHAPPY2018new"] ~ ~ ~ say'))
print(main('trexecute @s ~ ~ ~ say ABC'))
print(main('trexecute @s ^ ^ ^ say'))
print(main('trexecute @s ~ ~ ~ detect ^ ^ ^ air 0 say'))
print(main('trexecute @s[name="] 0 0 0 say 123"] ~ ~ ~ say'))
print(main('tr/execute @s ~ ~ ~ say'))

print()

# test2
print(main('trexecute @s[name="\\"\\"] 0 0 0 say 123\\"\\""] ~ ~ ~ say'))
print(main('trexecute    @s ~ ~2.3 +62.11111000000 say'))
print(main('trexecute@s~1.2~2.8 +5 say'))
print(main('trexecute@s 1 ~5~3 say'))
print(main('trexecute@s ~3 2~3 say'))
print(main('trexecute"H"~2 ~2 ~2 say'))
print(main('trexecute HS~2 ~2 ~2 say'))
print(main('trexecute@s~1.0~5~3 say'))
print(main('trexecute@s 1.00 7~3.20 say'))
print(main('trexecute@s 1.0 5 3.0000 say'))
print(main('trexecute@s~~~execute@s~~~execute@s~~~'))
print(main('trexecute    @s ~~~execute@s~~~say'))
print(main('trexecute @s +0.0 -0.0 +0.0 say 1'))
print(main('trexecute @s +0 -0 +0 say 1'))
print(main('trexecute@s-1 2 2 say'))
print(main('trexecute@s+1 2 2 say'))
print(main('trexecute H+1 2 2 say'))

print()

#test3
print(main('trexecute@s~2.~~say'))
print(main('trexecute "H" ~2 ~2 ^2 say'))
print(main('trexecuteH~2 ~2 ~2 say'))
print(main('trexecute@s-1 2 2say'))
print(main('trexecute@s -1 2 ^2say'))
print(main('trexecute@s[tag="]",name="]"]~~~detect~~~air0say'))
print(main('trexecute H-1 2 2 say'))

print()

#others
print(main('trexecute @a[name="abc 123"] ~~ ~ execute @s ~9 346 ~-8 detect ^6 ^7 ^2 concrete 18 execute @p[r=3,scores={a=3}] 324 ~324 5 scoreboard players add @s[tag="999 888aasd asd "] QWE_AS 2'))
print(main('trexecute@s[tag="[][]  你妈死了"]~ 1~576detect^6^^66concrete 1 execute @s         [scores={n=0}] ~ ~ ~0.09 execute@s~~~detect 0 0 0 bedrock -1 execute@a [name="999去他奶奶的 jjj"]~~ ~/execute@s[tag="℃♞"]~ 32 ~5423give @s command_block 1 1 {"name_tag":["a":"b操你妈逼"]}'))
print(main('tr/execute @a~~~/w @s aaa'))