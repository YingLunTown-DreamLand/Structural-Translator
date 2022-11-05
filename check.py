import share
# 载入依赖项





def main()->list:
    """
    \n摘要
    本函数用于判断 `share.mcs` 中的数据是否满足 `.mcstructure` 相关规范
    \n返回值
    当满足规范时，返回 `[True]` ，否则返回 `[False, 错误类型:int]`
    """
    # 函数声明



    check = 0
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



    if check == 10:
        return [True]
    else:
        return [False, check]
    # 检查文件内容是否完整