import copy
import share
import function
import blockNBT.main
import blockNBT.CommandBlock
import blockNBT.Container
import brotli
import json
# 载入依赖项













class startFunction:
    def __init__(
        self,
        currentProgress:int,
        allProgress:int,
        workPath:str,
        inputPath:str,
        outputPath:str,
        replaceBlockID:list = [],
        translateMode:bool = True,
        jumpAir:bool = True,
        CreatorMode:list = [False, '']
    )->None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `currentProgress:int` 指的是当前处理进度
        `allProgress:int` 指的是总进度
        `workPath:str` 指的是工作目录的绝对路径
        `inputPath:str` 指的是欲被转义的文件之所在路径
        `outputPath:str` 指的是文件输出路径
        `replaceBlockID:list` 指的是 `组件 - 替换方块ID` 的列表
           # 默认值为 `[]`
        `translateMode:bool` 此选项为 `True` 时，将翻译 `.mcstructure` 文件，否则翻译 `WhiteWallJson` 文件
           # 默认值为 `True`
        `jumpAir:bool` 指的是生成的 `BDX` 文件是否需要跳过空气
           # 默认值为 `True` ，即要跳过空气
        `CreatorMode:list` 指的是开发者选项，列表中元素的格式为 `[是否要生成 JSON 文件:bool, 生成路径:str]` 。应当特别说明的是，此选项只会在 `translateMode = True` 时生效。
           # 默认值为 `[False, '']`
        """
        # 函数声明

        self.currentProgress = currentProgress    # 当前处理进度
        self.allProgress = allProgress    # 总进度
        self.workPath = workPath     # 工作目录的绝对路径
        self.inputPath = inputPath    # 文件输入路径
        self.outputPath = outputPath    # 文件输出路径
        self.replaceBlockID = replaceBlockID    # “组件 - 替换方块ID”用到的列表
        self.rbi_errorLog = []    # “组件 - 替换方块ID”的错误日志
        self.rbi_result = []    # “组件 - 替换方块ID”得到的替换结果
        self.translateMode = translateMode    # 翻译模式
        self.jumpAir = jumpAir    # 是否跳过空气
        self.CreatorMode = CreatorMode    # 开发者选项
        self.check = 'Successful'    # 结构完整性的检查结果
        self.waterWarning = False     # 含水方块警告
        self.errorList = []    # 转义时产生的错误日志
        self.experimental = []    # 处理容器中物品时产生的日志
        # 实例化

    # 实例化函数










    def main(self)->bool:
        """
        \n摘要
        本函数是 `class: startFunction` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        返回布尔值。当转义成功时返回 `True` ，否则返回 `False` 。
        """
        # 函数声明







        share.reset()
        # 重置全局共享变量







        if self.translateMode == True:
            from mcstructureTojson import mcstructureTojson
            function.showStates(progress = "get structure info / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            share.mcs = mcstructureTojson(self.inputPath,self.CreatorMode)
            share.mcs.main()
            share.mcs = share.mcs.json
            function.showStates(progress = "get structure info / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            # 取得结构信息
            import check
            function.showStates(progress = "check structure / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            self.check = check.main()
            if self.check[0] == False:
                self.check = self.check[1]
                return False
            else:
                self.check = 'Successful'
            function.showStates(progress = "check structure / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            # 检查结构完整性
            import pool
            function.showStates(progress = "get block pool / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            pool.main()
            function.showStates(progress = "get block pool / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            # 提取方块池
        else:
            from Others.TranslateJSON import TranslateJSON
            function.showStates(progress = "get json info / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            ans = TranslateJSON(self.inputPath)
            TranslateJSON.main(ans)
            share.pool = ans.pool
            share.mcs = ans.json
            del ans
            function.showStates(progress = "get json info / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            # 取得 JSON 信息
        # 取得信息







        if len(self.replaceBlockID) > 0:
            from replaceBlockID import replaceBlockID
            function.showStates(progress = "replaceBlockID / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
            rbi = replaceBlockID(self.replaceBlockID)
            rbi.main()
            self.rbi_errorLog = rbi.errorLog
            self.rbi_result = rbi.result
            function.showStates(progress = "replaceBlockID / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
        else:
            self.rbi_errorLog = None
            self.rbi_result = None
        # 组件 - 替换方块ID







        import pool_old
        pool_old.main()
        # 生成纯数据值的方块池







        areaPosStates = [1,1]
        areaPos = [1,1]
        states = 0
        # 初始化
        if ((share.mcs["Root:10"]["size:9"][0]) % 16) != 0:
            areaPosStates[0] = int((share.mcs["Root:10"]["size:9"][0]) / 16) + 1
        else:
            areaPosStates[0] = int((share.mcs["Root:10"]["size:9"][0]) / 16)
        # 拆分 X 轴
        if ((share.mcs["Root:10"]["size:9"][2]) % 16) != 0:
            areaPosStates[1] = int((share.mcs["Root:10"]["size:9"][2]) / 16) + 1
        else:
            areaPosStates[1] = int((share.mcs["Root:10"]["size:9"][2]) / 16)
        # 拆分 Z 轴





        outputCommand = []
        outputCommand.append(bytearray(
            b'BDX\x00\xe9\x98\xbf\xe5\xa4\x9a\xe7\xb1\xb3\xe5\xb0\xbc\xe6\x96\xaf\xe5\xa4\x9a\xe9\x9b\xb7\xe7\x89\xb9\x00\x1f\x75'
            ))
        for i in share.pool:
            outputCommand.append(bytearray(b'\x01' + (i[0].split('minecraft:',maxsplit=1)[1]).encode() + bytearray(b'\x00')))
        # 将方块池写入到指令列表





        with open(self.outputPath,"w+") as file:
            file.write('')
        # 创建文件





        executeStates = 0
        pointer = 0
        moveFacing = 1
        pointerPos = [0,0,0]
        T = share.mcs["Root:10"]["size:9"][2]



        yMove = share.mcs["Root:10"]["size:9"][1]
        if share.mcs["Root:10"]["size:9"][0] < 16:
            xMove = share.mcs["Root:10"]["size:9"][0]
        else:
            xMove = 16
        if share.mcs["Root:10"]["size:9"][2] < 16:
            zMove = share.mcs["Root:10"]["size:9"][2]
        else:
            zMove = 16



        partPosz = zMove - 1
        partPosx = xMove - 1
        bgIsWater = False



        if "block_position_data:10" in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]:
            hasBlockNBT = True
        else:
            hasBlockNBT = False
        # 初始化



        while True:
            executeStates = executeStates + 1
            # 更新执行次数
            function.showStates(
                progress = 'officalRun / start',
                provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress],
                officalRun = [executeStates, areaPosStates[0], areaPosStates[1], areaPos]
            )
            # 打印进度
            lastPointer = pointer
            # 记录指针位置


            while xMove > 0:
                xMove = xMove - 1
                # 改变数值
                while yMove > 0:
                    yMove = yMove - 1
                    # 改变数值
                    while zMove > 0:
                        if len(outputCommand) >= 1000000:
                            with open(self.outputPath,"a+b") as file:
                                file.write(bytearray(b'').join(outputCommand))
                            outputCommand = []
                        # 防止内存爆炸
                        states = states + 1
                        zMove = zMove - 1
                        # 改变数值
                        fgId = share.mcs["Root:10"]["structure:10"]["block_indices:9"][0][pointer]
                        bgId = share.mcs["Root:10"]["structure:10"]["block_indices:9"][1][pointer]
                        # 得到待处理方块的背景层(id)和前景层(id)
                        if fgId != -1:
                            foreground = share.pool[fgId]
                        else:
                            foreground = [None,{}]
                        if bgId != -1:
                            background = share.pool[bgId]
                        else:
                            background = [None,{}]
                        # 得到待处理方块的背景层和前景层


                        if ((foreground[0] == 'minecraft:air' and background[0] == None) or (
                            foreground[0] == None and background[0] == 'minecraft:air') or (
                            foreground[0] == 'minecraft:air' and background[0] == 'minecraft:air')) and (self.jumpAir == True):
                            upPointer = True
                        else:
                            upPointer = False
                        # 确定是否提交指针位置改变


                        if upPointer == False:
                            if pointerPos[0] != 0:
                                outputCommand.append(function.moveCommand(pointerPos[0],'x'))
                                pointerPos[0] = 0
                            if pointerPos[1] != 0:
                                outputCommand.append(function.moveCommand(pointerPos[1],'y'))
                                pointerPos[1] = 0
                            if pointerPos[2] != 0:
                                outputCommand.append(function.moveCommand(pointerPos[2],'z'))
                                pointerPos[2] = 0
                        # 变更指针位置(若需要变更的话)


                        if background[0] != None:
                            if (len(background[0].split('water')) > 1) and (foreground[0] != None):
                                bgIsWater = True
                                outputCommand.append(
                                    (
                                        bytearray(b'\x07') + bgId.to_bytes(length=2,byteorder='big') + background[1].to_bytes(length=2,byteorder='big')
                                    )
                                    if type(background[1]) == int else
                                    (
                                        bytearray(b'\x0d') + bgId.to_bytes(length=2,byteorder='big') + b'[' + json.dumps(background[1],ensure_ascii=False).encode(encoding='utf-8')[1:-1] + b']\x00'
                                    )
                                )
                        # 处理含水方块(若需要处理的话)


                        success_to_translate = False
                        # 初始化

                        parseNBT = False
                        if hasBlockNBT == True:
                            if f"{pointer}:10" in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_position_data:10"]:
                                if type(share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_position_data:10"][f"{pointer}:10"]["block_entity_data:10"]) == dict:
                                    parseNBT = True
                        # 确定方块实体数据是否是字典

                        if ((foreground[0] == 'minecraft:command_block') or (
                            foreground[0] == 'minecraft:repeating_command_block') or 
                            (foreground[0] == 'minecraft:chain_command_block')) and (
                            upPointer == False) and (parseNBT == True):
                            outputCommand.append(blockNBT.CommandBlock.cbGet(share.pool_old[fgId],pointer))
                            success_to_translate = True
                        # # 翻译命令方块

                        if success_to_translate == False and upPointer == False:
                            if foreground[0] in blockNBT.main.blockList:
                                changesValue = blockNBT.main.blockList[foreground[0]][str(share.pool_old[fgId][1])]
                                # 取得参数
                                if 1083 <= changesValue[1] <= 1088:
                                    outputCommand.append(bytearray(b'\x26\x00\x00\x1b\xdf\x00'))
                                if 7135 <= changesValue[1] <= 7140:
                                    outputCommand.append(bytearray(b'\x26\x00\x00\x04;\x00'))
                                # 如果是 箱子 或 陷阱箱 ，则无论是否是大型箱，都需要进行断开处理
                                if parseNBT == True:
                                    try:
                                        outputCommand.append(blockNBT.Container.main(changesValue[1],pointer,changesValue[0]))
                                        success_to_translate = True
                                    except:
                                        pass
                        # # 翻译容器内的物品

                        if success_to_translate == False and foreground[-1] != '摆烂' and foreground[0] != None and upPointer == False:
                            outputCommand.append(
                                    (
                                        bytearray(b'\x07') + fgId.to_bytes(length=2,byteorder='big') + foreground[1].to_bytes(length=2,byteorder='big')
                                    )
                                    if type(foreground[1]) == int else
                                    (
                                        bytearray(b'\x0d') + fgId.to_bytes(length=2,byteorder='big') + b'[' + json.dumps(foreground[1],ensure_ascii=False).encode(encoding='utf-8')[1:-1] + b']\x00'
                                    )
                                )
                        # # 处理普通情况

                        if hasBlockNBT == True:
                            if f"{pointer}:10" in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_position_data:10"]:
                                entitynbt = function.outputNBT(share.mcs,pointer)
                                outputCommand.append(
                                    bytearray(b'\x27') + 
                                    len(entitynbt).to_bytes(length=4,byteorder='big',signed=False) + 
                                    entitynbt
                                )
                        # # 写入方块实体数据
                        # 写入命令


                        if zMove > 0:
                            pointer = pointer + 1
                            pointerPos[2] = pointerPos[2] + 1
                        # 移动指针
                    if yMove > 0:
                        pointer = pointer + T - partPosz
                        pointerPos[1] = pointerPos[1] + 1
                        pointerPos[2] = pointerPos[2] - partPosz
                        zMove = partPosz + 1
                    # 移动指针
                if xMove > 0:
                    pointer = pointer + T - partPosz
                    pointerPos[0] = pointerPos[0] + 1
                    pointerPos[1] = pointerPos[1] - share.mcs["Root:10"]["size:9"][1] + 1
                    pointerPos[2] = pointerPos[2] - partPosz
                    yMove = share.mcs["Root:10"]["size:9"][1]
                    zMove = partPosz + 1
                # 移动指针



            if moveFacing == 1:
                areaPos[1] = areaPos[1] + 1
            else:
                areaPos[1] = areaPos[1] - 1
            # 移动到下一个区块(不考虑溢出)



            if (areaPos[1] > areaPosStates[1]) or (areaPos[1] < 1):
                if moveFacing == 1:
                    areaPos[1] = areaPosStates[1]
                else:
                    areaPos[1] = 1
                moveFacing = moveFacing * -1
                areaPos[0] = areaPos[0] + 1
                # 处理 x 轴上的溢出
                pointer = pointer + T - partPosz
                pointerPos[0] = pointerPos[0] + 1
                pointerPos[1] = pointerPos[1] - share.mcs["Root:10"]["size:9"][1] + 1
                pointerPos[2] = pointerPos[2] - partPosz
                # 移动指针
            else:
                if moveFacing == 1:
                    pointer = lastPointer + partPosz + 1
                    pointerPos[0] = pointerPos[0] - partPosx
                    pointerPos[1] = pointerPos[1] - share.mcs["Root:10"]["size:9"][1] + 1
                    pointerPos[2] = pointerPos[2] + 1
                else:
                    pointer = lastPointer - 16
                    pointerPos[0] = pointerPos[0] - partPosx
                    pointerPos[1] = pointerPos[1] - share.mcs["Root:10"]["size:9"][1] + 1
                    pointerPos[2] = pointerPos[2] - partPosz - 16
            if areaPos[0] > areaPosStates[0]:
                break
            # 移动到下一个区块并移动指针(考虑溢出)、结束循环



            if (share.mcs["Root:10"]["size:9"][0] - (areaPos[0] - 1) * 16) >= 16:
                xMove = 16
                partPosx = 15
            else:
                xMove = share.mcs["Root:10"]["size:9"][0] - (areaPos[0] - 1) * 16
                partPosx = xMove - 1
            # x轴
            yMove = share.mcs["Root:10"]["size:9"][1]
            # y轴
            if (share.mcs["Root:10"]["size:9"][2] - (areaPos[1] - 1) * 16) >= 16:
                zMove = 16
                partPosz = 15
            else:
                zMove = share.mcs["Root:10"]["size:9"][2] - (areaPos[1] - 1) * 16
                partPosz = share.mcs["Root:10"]["size:9"][2] - (areaPos[1] - 1) * 16 - 1
            # z轴
            # 重设初始量
        # 取得建造命令







        del share.mcs
        # 删除不必要内容







        function.showStates(
            progress = "officalRun / end",
            provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress]
        )
        # 打印进度







        function.showStates(progress = "writing / start",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])

        with open(self.outputPath,"r+b") as file:
            ans = bytearray(b'').join(file.readlines())
        # 读取原缓存内容
        with open(self.outputPath,"w+b") as file:
            file.write(bytearray(b'BD@') + brotli.compress( ans + bytearray(b'').join(outputCommand) + bytearray(b'XE')))
        if bgIsWater == True:
            self.waterWarning = True    # 警告：检测到此被翻译的结构存在含水方块，因此请在导入时不要使用 Omega 的 load 命令，否则会丢失这一特性！
       
        function.showStates(progress = "writing / end",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
        # 写入翻译结果







        self.errorList = copy.deepcopy(share.errorList)
        # 输出错误日志
        self.experimental = copy.deepcopy(share.experimental)
        # 输出物品转换日志







        function.showStates(progress = "down",provide = [self.workPath,self.inputPath,self.outputPath,self.currentProgress,self.allProgress])
        return True
        # 返回值
    # 主函数