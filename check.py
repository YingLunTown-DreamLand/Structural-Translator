import share
import os
import sys
# 载入依赖项



check = 0
print('进度：检查文件完整性……')
# 初始化值
if (check == 0) and (list(share.mcs) == ["Root:10"]):
    check = 1
if (check == 1) and (set(list(share.mcs["Root:10"])) == 
set(["format_version:3","size:9","structure:10","structure_world_origin:9"])):
    check = 2
if (check == 2) and ((share.mcs["Root:10"]["size:9"][0] > 0) and (share.mcs["Root:10"]["size:9"][0] > 0) and (
    share.mcs["Root:10"]["size:9"][2] > 0)):
    check = 3
if (check == 3) and ((set(list(share.mcs["Root:10"]["structure:10"])) == set(["block_indices:9","palette:10","entities:9"])) or (
    set(list(share.mcs["Root:10"]["structure:10"])) == set(["block_indices:9","palette:10"]))):
    check = 4
if (check == 4):
    try:
        list(share.mcs["Root:10"]["structure:10"]["palette:10"]).index("default:10")
        check = 5
    except:
        None
if (check == 5) and ((set(list(share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]))) == set(
    list(["block_palette:9","block_position_data:10"]))):
    check = 6
if (check == 6) and (len(share.mcs["Root:10"]["structure:10"]["block_indices:9"][0]) == len(
    share.mcs["Root:10"]["structure:10"]["block_indices:9"][1])):
    check = 7
if (check == 7) and ((
    share.mcs["Root:10"]["size:9"][0] * share.mcs["Root:10"]["size:9"][1] * share.mcs["Root:10"]["size:9"][2]) == len(
    share.mcs["Root:10"]["structure:10"]["block_indices:9"][0])):
    check = 8
if (check == 8) and (((min(share.mcs["Root:10"]["structure:10"]["block_indices:9"][0]) >= -1) and (min(
    share.mcs["Root:10"]["structure:10"]["block_indices:9"][1]) >= -1)) and ((max(
    share.mcs["Root:10"]["structure:10"]["block_indices:9"][0]) <= (
    len(share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"]) - 1)) and (
    max(share.mcs["Root:10"]["structure:10"]["block_indices:9"][1]) <= (
    len(share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"]) - 1)))):
    check = 9
if (check == 9):
    try:
        for i in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"]:
            i["name:8"].split('minecraft:')[1]
        check = 10
    except:
        None
# 判定错误类型
if check != 10:
    print('错误：您提供的文件的确满足 MCStructure 之编码格式，但文件内含信息不完整或无效，因此本翻译器拒绝继续翻译.')
    if check == 0:
        print('具体错误发生在：你正尝试修改源代码，但你似乎改错了……')
    if check == 1:
        print('具体错误发生在：文件可能已损坏')
    if check == 2:
        print('具体错误发生在：文件中声明的结构大小为负数')
    if check == 3:
        print('具体错误发生在：缺少方块索引表或调色板中至少其一')
    if check == 4:
        print('具体错误发生在：未找到原版调色板')
    if check == 5:
        print('具体错误发生在：原版调色板缺少方块状态数据或方块实体数据中至少其一')
    if check == 6:
        print('具体错误发生在：方块索引表中前景层和背景层的方块数目不等价')
    if check == 7:
        print('具体错误发生在：声明的方块数跟结构中实际记录的方块数不等价')
    if check == 8:
        print('具体错误发生在：方块索引表中指定的方块超出原版调色板范围')
    if check == 9:
        print('具体错误发生在：原版调色板中存在某一个方块未指定方块名或未指定命名空间')
# 打印错误详情
    os.system("pause")
    sys.exit()
print('进度：文件基本完整.')
# 善后
# 检查文件内容是否完整