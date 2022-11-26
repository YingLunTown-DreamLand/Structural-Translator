import share
import function
# 载入依赖项





def main()->None:
    share.pool_old = []
    # 初始化



    for i in share.pool:
        if type(i[1]) == int:
            share.pool_old.append([i[0],i[1]])
        elif i[1] == {}:
            share.pool_old.append([i[0],0])


        else:
            i1 = function.searchingFor(i[0])

            try:
                i1 = [
                    i1[0],
                    i1[1].replace('blockData','blockData_NoType'),
                    i1[2].replace('blockData','blockData_NoType')
                ]
                share.ans = i[1]
                share.name = i[0]
                exec(i1[1])
                exec(f'share.pool_old.append([i[0],{i1[2]}])')
                if share.pool_old[-1][-1] == None:
                    0/0
                if type(share.pool_old[-1][-1]) == list:
                    if share.pool_old[-1][-1][-1] == '摆烂':
                        share.pool_old[-1] = [share.pool_old[-1][0],share.pool_old[-1][1][0],'摆烂']

            except:
                share.pool_old.append([i[0],0])

        # 取得方块名称及数据值

    # 取得方块池





# 注意：
# 本函数主要用于容器相关，因为查找容器的 runtimeId 需要用到方块数据值.
# 原本的附加值格式正逐步被 MOJANG 弃用，这是旧版本改编内容.