import sys
sys.path.append(".")
import Api.function
import Api.share
import Api.indexList
import Api.unpackData
import Api.RuntimeIdPalette
import Api.ContainerIndex
# 载入依赖项





Api.share.BDXContext = Api.unpackData.getBDXdata('Api/input.bdx')
# 取得解压后的 BDX 数据
# 舍弃内部文件头 BDX



authorName = Api.unpackData.getBDXauthor(Api.share.BDXContext,0)
Api.share.BDXContext = Api.share.BDXContext[authorName[-1]:]
authorName = authorName[0]
# 取得作者之名



Api.share.pointer = 0
Api.share.penPos = [0,0,0]
Api.share.blockPalette = []
Api.share.resultList = []
Api.share.runtimeIdsBlockPalette = []
Api.share.successStates = False
# 初始化


while True:
    if Api.share.BDXContext[Api.share.pointer:Api.share.pointer+1] == b'\x58':
        Api.share.successStates = True
        break
    # 判断是否需要结束

    Api.share.functionName = Api.unpackData.getType(Api.share.BDXContext,Api.share.pointer)
    if Api.share.functionName == False:
        break
    Api.share.pointer = Api.share.functionName[-1]
    Api.share.operation = Api.share.functionName[1]
    operationNum = Api.share.functionName[2]
    Api.share.functionName = Api.share.functionName[0]
    # 取得函数名、操作编号的 Bytes 及 Int 形式
    # 若 Api.unpackData.getType 返回 False ，则表明文件可能已损坏

    exec(f'Api.function.{Api.indexList.indexListforMain[operationNum]}()')
    # 解析 Operation



if authorName == '':
    print('作者未定义.')
else:
    print('作者之名: ' + authorName)
if Api.share.successStates == False:
    print('文件不完整或已损坏')
if Api.share.successStates == True:
    print('文件完整')
# 打印作者名称及文件完整结论
with open("Api/ans.json","w+",encoding='utf-8') as file:
    import json
    file.write(json.dumps(Api.share.resultList,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
# 输出结果
print('SUCCESS: 已成功解析目标文件，已保存在 Api 目录下，文件名是 ans.json .')
# 打印解析结果