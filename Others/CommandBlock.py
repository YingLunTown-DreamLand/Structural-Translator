def cbGet(input:dict)->dict:
    """
    \n摘要
    专门针对白墙的 `JSON` 文件设计。本函数用于提取相关的 `NBT` 数据，并将其转换为 `.mcstructure` 文件中的 `NBT` 格式。
    \n参数
    `input:dict` 指的是白墙 `JSON` 文件中所记录的命令方块数据。一个示例如下。
        `"cmddata": `
            `{`
                `"lastOutput": "",`
                `"command": "kill @e",`
                `"shouldTrackOutput": false,`
                `"mode": "Tick",`
                `"isConditional": false,`
                `"executeOnFirstTick": false,`
                `"tickDelay": 0,`
                `"name": "",`
                `"isRedStoneMode": false`
            `}`
    需要注意的是，你应该直接向本函数传入 `cmddata` 的 `value` 部分。
    \n返回值
    返回 `.mcstructure` 文件下的 `NBT` 格式，其类型是一个 `字典` 。
    """
    # 函数声明

    ans = {}
    # 初始化

    try:
        ans['Command:8'] = input['command']
    except:
        ans['Command:8'] = ''
    # 命令
    try:
        ans['CustomName:8'] = input['name']
    except:
        ans['CustomName:8'] = ''
    # 悬浮字
    try:
        ans['TickDelay:3'] = input['tickDelay']
    except:
        ans['TickDelay:3'] = 0
    # 延迟
    try:
        ans['ExecuteOnFirstTick:1'] = input['executeOnFirstTick']
    except:
        ans['ExecuteOnFirstTick:1'] = 0
    # 在启动后的第一时刻执行命令(仅限于 重复 命令方块)
    try:
        ans['TrackOutput:1'] = input['shouldTrackOutput']
    except:
        ans['TrackOutput:1'] = 1
    # 是否保留执行日志
    try:
        ans['conditionalMode:1'] = input['isConditional']
    except:
        ans['conditionalMode:1'] = 0
    # 是否有条件
    try:
        if input['isRedStoneMode'] == 0:
            ans['auto:1'] = 1
        if input['isRedStoneMode'] == 1:
            ans['auto:1'] = 0
        if (input['isRedStoneMode'] != 0) or (input['isRedStoneMode'] != 1):
            ans['auto:1'] = 0
    except:
        ans['auto:1'] = 0
    # 是否需要红石

    return ans
    # 返回值