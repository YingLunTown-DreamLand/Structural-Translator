import os
import sys
import traceback
import share
import function
import brotli
# 载入依赖项





###
while True:
    print('您希望翻译 MCStructure 吗？(回答 Yes 或 No)\n注：选择 No 将翻译 白墙JSON 文件！')
    translateMode = input()
    if (translateMode == 'Yes') or (translateMode == 'yes') or (translateMode == 'y') or (translateMode == 'Y'):
        translateMode = True
        break
    if (translateMode == 'No') or (translateMode == 'no') or (translateMode == 'n') or (translateMode == 'N'):
        translateMode = False
        break
    print('错误：请不要答非所问.\n\n\n')
###
# 确定翻译模式

if translateMode == True:
    try:
        import mcstructureTojson
    except:
        print('错误：您可能未提供文件或提供了无效文件.\n请将正确的文件置于当前目录并命名为"input.mcstructure".')
        print('具体错误如下：\n')
        print(traceback.format_exc())
        os.system("pause")
        sys.exit()
        # 善后
    # 取得结构信息
else:
    try:
        import Others.TranslateJSON
    except:
        print('错误：您可能未提供文件或提供了无效文件.\n请将正确的文件置于当前目录并命名为"input.json".')
        print('具体错误如下：\n')
        print(traceback.format_exc())
        os.system("pause")
        sys.exit()
        # 善后
    # 取得 JSON 信息
# 取得信息





if translateMode == True:
    import check
    # 检查结构完整性
    import pool
    errorList = pool.errorList
    # 提取方块池





import replaceBlockID
# 组件 - 替换方块ID





###
while True:
    print('您可以选择在翻译时跳过空气方块，这样在一定程度上可以提高效率.\n您真的希望跳过空气吗？(回答 Yes 或 No)')
    jumpAir = input()
    if (jumpAir == 'Yes') or (jumpAir == 'yes') or (jumpAir == 'y') or (jumpAir == 'Y'):
        jumpAir = True
        break
    if (jumpAir == 'No') or (jumpAir == 'no') or (jumpAir == 'n') or (jumpAir == 'N'):
        jumpAir = False
        break
    print('错误：请不要答非所问.\n\n\n')
###
# 询问是否跳过空气方块



print('进度：即将开始翻译……')
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
outputCommand.append(bytearray(b'BDX\x00\xe9\x98\xbf\xe5\xa4\x9a\xe7\xb1\xb3\xe5\xb0\xbc\xe6\x96\xaf\xe5\xa4\x9a\xe9\x9b\xb7\xe7\x89\xb9\x00'))
for i in share.pool:
    outputCommand.append(bytearray(b'\x01' + (i[0].split('minecraft:',maxsplit=1)[1]).encode() + bytearray(b'\x00')))
# 将方块池写入到指令列表

with open("ans.bdx","w+") as file:
    file.write('')
# 创建文件

executeStates = 0
pointer = 0
moveFacing = 1
pointerPos = [0,0,0]
T = share.mcs["Root:10"]["size:9"][2]
# # 初始化(1)
yMove = share.mcs["Root:10"]["size:9"][1]
if share.mcs["Root:10"]["size:9"][0] < 16:
    xMove = share.mcs["Root:10"]["size:9"][0]
else:
    xMove = 16
if share.mcs["Root:10"]["size:9"][2] < 16:
    zMove = share.mcs["Root:10"]["size:9"][2]
else:
    zMove = 16
# # 初始化(2)
partPosz = zMove - 1
partPosx = xMove - 1
fgIsWater = False
# # 初始化(3)
# 初始化
print('进度：翻译开始.')
while True:
    executeStates = executeStates + 1
    rate = str(( executeStates / (areaPosStates[0] * areaPosStates[1]) ) * 100)
    print(f'当前进度 {rate} % | 当前正在处理区块 {areaPos} | 总区块数 {areaPosStates[0] * areaPosStates[1]}')
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
                    with open("ans.bdx","a+b") as file:
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
                    foreground = [None,0]
                if bgId != -1:
                    background = share.pool[bgId]
                else:
                    background = [None,0]
                # 得到待处理方块的背景层和前景层

                if ((foreground[0] == 'minecraft:air' and background[0] == None) or (
                    foreground[0] == None and background[0] == 'minecraft:air') or (
                    foreground[0] == 'minecraft:air' and background[0] == 'minecraft:air')) and (jumpAir == True):
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
                        fgIsWater = True
                        outputCommand.append(bytearray(b'\x07') + 
                        bgId.to_bytes(length=2,byteorder='big') + 
                        background[1].to_bytes(length=2,byteorder='big'))
                # 处理含水方块(若需要处理的话)

                if ((foreground[0] == 'minecraft:command_block') or (
                    foreground[0] == 'minecraft:repeating_command_block') or (
                    foreground[0] == 'minecraft:chain_command_block')) and (translateMode == True):
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
                        command = command.replace('-----Mark of use 0x10-----','\\n')
                        command = command.replace('\\n','\n')
                        command = command.replace('\\"','"')
                        command = command.encode(encoding="utf-8")
                    except:
                        command = bytearray(b'')
                    # 命令方块内的指令
                    try:
                        name = share.mcs["Root:10"]["structure:10"]["palette:10"][
                            "default:10"]["block_position_data:10"][f"{pointer}:10"][
                                "block_entity_data:10"]["CustomName:8"]
                        name = name.replace('-----Mark of use 0x10-----','\\n')
                        name = name.replace('\\n','\n')
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
                    outputCommand.append(bytearray(b'\x24')+facing+Type+command+bytearray(b'\x00')+name+
                    bytearray(b'\x00')+bytearray(b'\x00')+delay+executeOnFirstTick+trackOutput+conditional+nrs)
                    # 写入放置命令
                elif foreground[-1] != '摆烂':
                    if upPointer == False:
                        outputCommand.append(bytearray(b'\x07') + 
                        fgId.to_bytes(length=2,byteorder='big') + 
                        foreground[1].to_bytes(length=2,byteorder='big'))
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





print('进度：正在将翻译结果写入到文件……')
with open("ans.bdx","r+b") as file:
    ans = bytearray(b'').join(file.readlines())
# 读取原缓存内容
with open("ans.bdx","w+b") as file:
    file.write(bytearray(b'BD@') + brotli.compress( ans + bytearray(b'').join(outputCommand) + bytearray(b'XE')))
if fgIsWater == True:
    print('警告：检测到此被翻译的结构存在含水方块，因此请在导入时不要使用 Omega 的 load 命令，否则会丢失这一特性！')
print('完成：翻译完成，保存在当前目录下的 ans.bdx 中.')
# 写入翻译结果





if translateMode == True:
    if len(mcstructureTojson.jumpList) > 0:
        print('警告：翻译时舍弃了部分 NBT 数据，现在正在输出 警告 日志……')
        with open("warning.log","w+") as file:
            for i in mcstructureTojson.jumpList:
                file.write(str(i) + '\n')
        print('完成：已输出警告日志，保存在当前目前下的 warning.log 中.')
    # 输出警告
    if len(errorList) > 0:
        print('错误：翻译时发生了错误，现在正在输出 错误 日志……')
        with open("error.log","w+") as file:
            for i in errorList:
                file.write(str(i) + '\n')
        print('完成：已输出错误日志，保存在当前目前下的 error.log 中.\n请通知开发者并附上此文件以修复Bug.')
    # 输出错误
    # 输出日志





print('\n完成：已完成全部工作')
os.system("pause")
sys.exit()
# 善后