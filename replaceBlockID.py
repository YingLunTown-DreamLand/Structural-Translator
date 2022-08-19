import copy
import share
import function
# 载入依赖项



###
while True:
    print('您是否需要使用 替换方块ID 之功能？(新版本的方块ID跟网易租赁服版本的方块ID可能不同，您可能需要把新ID转换为旧ID)\n请回答 Yes 或 No\n注意：此功能会同时影响箱子内的物品！')
    replaceBlockID = input()
    if (replaceBlockID == 'Yes') or (replaceBlockID == 'yes') or (replaceBlockID == 'y') or (replaceBlockID == 'Y'):
        replaceBlockID = True
        break
    if (replaceBlockID == 'No') or (replaceBlockID == 'no') or (replaceBlockID == 'n') or (replaceBlockID == 'N'):
        replaceBlockID = False
        rbiSit = False
        break
    print('错误：请不要答非所问.\n\n\n')
###

if replaceBlockID == True:
    try:
        with open("replaceBlockID.txt","r+b") as file:
            rbiList = []
            unSuccessCount = 0
            unSuccessLine = 0
            unSuccessLineList = []
            #
            for i in file:
                unSuccessLine = unSuccessLine + 1
                #
                i = bytearray(i)
                if i[-1] == 10:
                    del i[-1]
                if i[-1] == 13:
                    del i[-1]
                i = i.split(bytearray(b','))
                #
                if (len(i) == 4) and (len(i[2].split(bytearray(b'minecraft:'))) == 2):
                    try:
                        if (len(i[1].split(bytearray(b'.'))) > 1) or (len(i[3].split(bytearray(b'.'))) > 1):
                            0/0
                        i[1] = int(i[1])
                        i[3] = int(i[3])
                        if ((i[1] < 0) and (i[1] != -1)) or ((i[3] < 0) and (i[3] != -1)):
                            0/0
                        blockName = function.bytearrayToStr(i[0])
                        blockName1 = function.bytearrayToStr(i[2])
                        rbiList.append([blockName,i[1],blockName1,i[3]])
                    except:
                        unSuccessCount = unSuccessCount + 1
                        unSuccessLineList.append(unSuccessLine)
                else:
                    unSuccessCount = unSuccessCount + 1
                    unSuccessLineList.append(unSuccessLine)
                #
            #
            if unSuccessCount > 0:
                heigh = len(str(max(unSuccessLineList)))
                outputErrorMessage = []
                while len(unSuccessLineList) > 10:
                    repeat = 10
                    outputErrorMessageLS = []
                    while repeat > 0:
                        i = str(unSuccessLineList[0])
                        while len(i) < heigh:
                            i = '0' + i
                        outputErrorMessageLS.append(i)
                        del unSuccessLineList[0]
                        repeat = repeat - 1
                    outputErrorMessage.append(outputErrorMessageLS)
                #
                print(f'替换方块ID：总计 {unSuccessCount} 处未能成功，错误发生在下列行数中：')
                #
                for i in outputErrorMessage:
                    i = ", ".join(i)
                    print(i)
                if len(unSuccessLineList) > 0:
                    unSuccessLineList = ", ".join([str(i) for i in unSuccessLineList])
                    print(unSuccessLineList)
                #
            #
        #
        rbiSit = True
        #
    except:
        rbiSit = False
        print('错误：替换方块ID 之功能未能成功，原因是未能找到当前目录下的 replaceBlockID.txt 文件')
        print('文件配置方法：每行只写1种方块，如果要把数据值为 m 的 A 方块改为数据值是 n 的 B 方块，则写“A,m,B,n”')
        print('例子：把新版本的数据值为 0 的 minecraft:grass 方块改变为数据值为 1 的 minecraft:glass 方块，则写：')
        print('minecraft:grass,0,minecraft:glass,1')
        print('其他一些例子：')
        print('minecraft:dirt,5,minecraft:anvil,7')
        print('minecraft:redstone_block,0,minecraft:end_portal,0')
        print('minecraft:kelp,10,minecraft:bamboo,3')
        print('注意：请一定在原本方块ID前加上“minecraft:”，否则会替换失败！')
        print('注意：目前不支持将方块改变为命令方块，请知悉.')
        print('注意：方块的数据值是正整数；通常地，方块的数据值是 0 .')
        print('注意：如果您希望忽略数据值，则请在对应数据值处填写 -1 .')
successCount = 0
if rbiSit == True:
    poolNew = []
    for i in share.pool:
        if i[-1] != '摆烂':
            poolNew.append([i[0],i[1]])
        else:
            poolNew.append([i[0],i[1],i[2]])
        #
        for i1 in rbiList:
            if ((i[0] == i1[0]) and (i[1] == i1[1])) or ((i[0] == i1[0]) and (i1[1] == -1)):
                poolNew[-1][0] = i1[2]
                successCount = successCount + 1
                if i1[3] != -1:
                    poolNew[-1][1] = i1[3]
                if i[-1] == '摆烂':
                    del poolNew[-1][2]
                break
    share.pool = copy.deepcopy(poolNew)
    print(f'替换方块ID：完成，已替换方块池中的 ID 及 数据值 ，总计替换 {successCount} 次.')
# 组件 - 替换方块ID