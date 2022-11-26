import share, function
from Api.JsonToNBT.JsonTranslate import JSONCompound
# 载入依赖项



def main()->None:
    share.pool = []
    # 初始化

    for i in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"]:
        share.pool.append(
            [
                i["name:8"],
                function.outputJsonNBT_Compound(
                    JSONCompound(i["states:10"])
                ),
            ]
        )
        # 取得方块名称及对应的方块状态
    # 取得方块池