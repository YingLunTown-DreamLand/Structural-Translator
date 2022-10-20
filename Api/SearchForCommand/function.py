import json
# 载入依赖项



def run(path:str,outputPath:str,outputLogPath:str)->None:
    with open(path,"r+",encoding='utf-8') as file:
        WhiteWallJson = json.load(file)
    # 读取文件

    ans = []
    for i in WhiteWallJson:
        if 'cmddata' in i:
            ans.append(i)
    # 提纯

    with open(outputPath,'w+',encoding='utf-8') as file:
        file.write(json.dumps(ans,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
    with open(outputLogPath,'w+',encoding='utf-8') as file:
        for i in ans:
            file.write("['" + i['cmddata']['command'] + "']\n")
    # 输出提纯结果及相应日志