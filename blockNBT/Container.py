import sys
sys.path.append(".")
import share
import function
# 载入依赖项



def main(runtimeId:int,pointer:int,Type:str):
    """
    \n摘要
    将结构中记录的容器数据转换为 `BDX` 支持的编码格式
    \n参数
    `runtimeId:int` 指的是此方块在 `117` 版本下的 `runtimeId`
    `pointer:int` 指的是指针位置
    `Type:str` 指的是此容器储存的物品所对应的列表(或组)之名
    \n返回值
    返回一个 `bytes` ，其为 `bytearray` 型
    """
    # 函数声明
    global share
    global function
    # 声明全局变量
    try:
        data = share.mcs["Root:10"]["structure:10"]["palette:10"][
            "default:10"]["block_position_data:10"][f"{pointer}:10"][
            "block_entity_data:10"][Type]
    except:
        share.errorList.append(['Container','unknown.error',pointer,share.mcs["Root:10"]["structure:10"]["palette:10"][
        "default:10"]["block_position_data:10"][f"{pointer}:10"][
        "block_entity_data:10"]])
        0/0
    repeat = legth = len(data)
    List = []
    location = -1
    # 初始化

    if repeat == 0:
        share.errorList.append(['Container','container.empty',pointer,share.mcs["Root:10"]["structure:10"]["palette:10"][
        "default:10"]["block_position_data:10"][f"{pointer}:10"][
        "block_entity_data:10"]])
        0/0
    # 当容器没有物品时

    while repeat > 0:
        repeat = repeat - 1
        location = location + 1
        # 改变数值
        try:
            dataLocation = data[location]
        except:
            dataLocation = data
            repeat = 0
            legth = 1
        # 取得当前正在访问的槽位数据
        Count = dataLocation["Count:1"]
        Damage = dataLocation["Damage:2"]
        Name = dataLocation["Name:8"]
        try:
            Slot = dataLocation["Slot:1"]
        except:
            Slot = 0
        try:
            share.ans = dataLocation["Block:10"]["states:10"]
            share.name = dataLocation["Block:10"]["name:8"]
            if len(share.ans) <= 0:
                0/0
            successMark = True
        except:
            successMark = False
        try:
            if successMark == True:
                i = function.searchingFor(share.name)
                exec(i[1])
                exec(f'List.append({i[2]})')
                if List[-1] == None:
                    0/0
                if type(List[-1]) == list:
                    if List[-1][-1] == '摆烂':
                        List[-1] = List[-1][0]
        except ZeroDivisionError:
            List[-1] = 0
            share.errorList.append(['Container','function.return.none',pointer,location,dataLocation])
        except TypeError:
            List.append(0)
            share.errorList.append(['Container','block.not.found',pointer,location,dataLocation])
        except:
            List.append(0)
            share.errorList.append(['Container','translate.error',pointer,location,dataLocation])
        # 取得具体数据
        try:
            Damage2 = dataLocation["tag:10"]["Damage:3"]
        except:
            Damage2 = None
        # 取得物品损坏数据(如剑之类的)
        damageAns = 0
        if Damage != 0:
            damageAns = Damage
        if Damage2 != None:
            damageAns = Damage2
        if successMark == True:
            damageAns = List[-1]
            del List[-1]
        # 决定最终数据值

        import replaceBlockID
        if replaceBlockID.replaceBlockID == True:
            try:
                for i in replaceBlockID.rbiList:
                    if (Name == i[0] and damageAns == i[1]) or (Name == i[0] and i[1] == -1):
                        Name = i[2]
                        if i[3] != -1:
                            damageAns = i[3]
            except AttributeError:
                None
        # 组件 - 替换方块ID

        share.experimental.append([Name,Count,damageAns,Slot,dataLocation])
        # 实验性功能

        List.append((Name.split('minecraft:')[1]).encode() + bytearray(b'\x00') + Count.to_bytes(length=1,byteorder='big',signed=False) + 
        damageAns.to_bytes(length=2,byteorder='big',signed=False) + Slot.to_bytes(length=1,byteorder='big',signed=False))
        # 放入结构体

    return bytearray(b'\x26') + runtimeId.to_bytes(length=4,byteorder='big',signed=False) + legth.to_bytes(
        length=1,byteorder='big',signed=False) + bytearray(b'').join(List)
    # 返回结果