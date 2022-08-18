import share
import function
# 载入依赖项

share.errorList = []
share.pool = []
share.pointer = -1
print('进度：开始提取方块池……')
# 初始化
for i in share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"]:
    share.pointer = share.pointer + 1
    # 移动指针
    if len(i["states:10"]) == 0:
        share.pool.append([i["name:8"],0])
    else:
        i1 = function.searchingFor(i["name:8"])
        try:
            share.ans = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]
            share.name = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["name:8"]
            exec(i1[1])
            exec(f'share.pool.append([i["name:8"],{i1[2]}])')
            if share.pool[-1][-1] == None:
                0/0
            if type(share.pool[-1][-1]) == list:
                if share.pool[-1][-1][-1] == '摆烂':
                    share.pool[-1] = [share.pool[-1][0],share.pool[-1][1][0],'摆烂']
        except ZeroDivisionError:
            share.pool[-1][-1] = 0
            share.errorList.append(['Block','function.return.none',share.pointer,i])
        except TypeError:
            share.pool.append([i["name:8"],0])
            share.errorList.append(['Block','block.not.found',share.pointer,i])
        except:
            share.pool.append([i["name:8"],0])
            share.errorList.append(['Block','translate.error',share.pointer,i])
    # 取得方块名称及数据值
print('进度：已成功提取方块池！')
# 取得方块池