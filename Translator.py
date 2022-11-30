from startFunction import startFunction
import function
import os, json, time, random, traceback
# 载入依赖项

import colorama
colorama.init(autoreset=True)
# 显示彩色字





try:
    with open("settings.json","r+",encoding='utf-8') as file:
        file = json.load(file)
except:
    file = {}
# 读取 JSON 文件





default = {
    "全局设置":
    {
        "文件搜索路径": os.path.normpath(os.getcwd()).replace('\\','/'),
        "文件输出路径": os.path.normpath(f"{os.path.normpath(os.getcwd())}\\Output").replace('\\','/'),
        "组件 - 替换方块ID": [
            ['B', 'minecraft:double_stone_block_slab', -1, 'minecraft:double_stone_slab', -1],
            ['B', 'minecraft:double_stone_block_slab2', -1, 'minecraft:double_stone_slab2', -1],
            ['B', 'minecraft:double_stone_block_slab3', -1, 'minecraft:double_stone_slab3', -1],
            ['B', 'minecraft:double_stone_block_slab4', -1, 'minecraft:double_stone_slab4', -1],
            ['B', 'minecraft:stone_block_slab', -1, 'minecraft:stone_slab', -1],
            ['B', 'minecraft:stone_block_slab2', -1, 'minecraft:stone_slab2', -1],
            ['B', 'minecraft:stone_block_slab3', -1, 'minecraft:stone_slab3', -1],
            ['B', 'minecraft:stone_block_slab4', -1, 'minecraft:stone_slab4', -1],
            ['B', 'minecraft:sea_lantern', -1, 'minecraft:sealantern', -1],
            ['C', 'minecraft:double_stone_block_slab', -1, 'minecraft:double_stone_slab', -1],
            ['C', 'minecraft:double_stone_block_slab2', -1, 'minecraft:double_stone_slab2', -1],
            ['C', 'minecraft:double_stone_block_slab3', -1, 'minecraft:double_stone_slab3', -1],
            ['C', 'minecraft:double_stone_block_slab4', -1, 'minecraft:double_stone_slab4', -1],
            ['C', 'minecraft:stone_block_slab', -1, 'minecraft:stone_slab', -1],
            ['C', 'minecraft:stone_block_slab2', -1, 'minecraft:stone_slab2', -1],
            ['C', 'minecraft:stone_block_slab3', -1, 'minecraft:stone_slab3', -1],
            ['C', 'minecraft:stone_block_slab4', -1, 'minecraft:stone_slab4', -1],
            ['C', 'minecraft:sea_lantern', -1, 'minecraft:sealantern', -1]
        ],
        "是否跳过空气": True,
        "开发者选项 - 是否启用": False
    }
}
# 默认配置/表单





def beautifulSettings(needFix:dict,template:dict) -> dict:
    if not "文件搜索路径" in needFix:
        needFix["文件搜索路径"] = template["文件搜索路径"]
    if not "文件输出路径" in needFix:
        needFix["文件输出路径"] = template["文件输出路径"]
    if not "组件 - 替换方块ID" in needFix:
        needFix["组件 - 替换方块ID"] = template["组件 - 替换方块ID"]
    if not "是否跳过空气" in needFix:
        needFix["是否跳过空气"] = template["是否跳过空气"]
    if not "开发者选项 - 是否启用" in needFix:
        needFix["开发者选项 - 是否启用"] = template["开发者选项 - 是否启用"]
    return needFix

if "全局设置" in file:
    file["全局设置"] = beautifulSettings(file["全局设置"],default["全局设置"])
else:
    file["全局设置"] = default["全局设置"]

if not "自定义配置" in file:
    file["自定义配置"] = []

for i in range(len(file["自定义配置"])):
    try:
        file["自定义配置"][i] = beautifulSettings(file["自定义配置"][i],default["全局设置"])
    except:
        None
# 实现默认配置，同时将没有配置的部分设置为默认配置





file["全局设置"]["文件搜索路径"] = os.path.normpath(file["全局设置"]["文件搜索路径"]).replace('\\','/')
file["全局设置"]["文件输出路径"] = os.path.normpath(file["全局设置"]["文件输出路径"]).replace('\\','/')
for i in range(len(file["自定义配置"])):
    file["自定义配置"][i]["文件输入路径"] = [
        os.path.normpath(i1).replace('\\','/') for i1 in file["自定义配置"][i]["文件输入路径"]
    ]
    file["自定义配置"][i]["文件输出路径"] = os.path.normpath(file["自定义配置"][i]["文件输出路径"]).replace('\\','/')
# 格式化配置文件中的所有路径





for i in range(len(file["自定义配置"])):
    file["自定义配置"][i]["文件输入路径"] = [
        os.path.normpath(os.path.join(file["全局设置"]["文件搜索路径"],i1)).replace('\\','/') for i1 in file["自定义配置"][i]["文件输入路径"]
    ]
    if os.path.isabs(file["自定义配置"][i]["文件输出路径"]) == False:
        file["自定义配置"][i]["文件输出路径"] = default["全局设置"]["文件输出路径"]
# 将自定义配置下的所有相对路径更换为绝对路径





filePath = []
for root,dirs,files in os.walk(file["全局设置"]["文件搜索路径"]):
    for fileName in files:
        String = os.path.normpath(os.path.join(root,fileName)).replace('\\','/').split('/')
        String[-1] = String[-1].split('.')
        if len(String[-1]) > 0:
            String[-1][-1] = String[-1][-1].replace('M','m').replace('C','c').replace('S','s').replace('T','t').replace('R','r').replace(
                'U','u').replace('E','e').replace('J','j').replace('S','s').replace('O','o').replace('N','n')
        String[-1] = ".".join(String[-1])
        if os.path.splitext(String[-1])[-1] == '.mcstructure' or os.path.splitext(String[-1])[-1] == '.json' and String[-1] != 'settings.json' and String[-1] != 'translateLog.json':
            filePath.append("/".join(String))
# 查找到所有的待翻译文件





customPath = {}
for i in range(len(file["自定义配置"])):
    for i1 in file["自定义配置"][i]["文件输入路径"]:
        customPath[i1] = i
# 提取出自定义配置下的“文件输入路径”与“配置表”之间的对应关系
# example: customPath = {"test/demo.bdx": 0}





print('\033[1;37;46m----- 欢迎使用 Structural-Translator -----\033[0m')
time.sleep(1)
print(f'\033[0;32;2018m已找到\033[0m \033[0;37;2018m{len(filePath)}\033[0m \033[0;32;2018m个文件，即将开始翻译.\033[0m')
time.sleep(0.5)
# 打印提示语





workPath = file["全局设置"]["文件搜索路径"]
currentNum = 0
allNum = len(filePath)
translateLog = {}




for i in filePath:
    currentNum = currentNum + 1
    # 移动指针



    if i in customPath:
        fileType = i.split('/')
        if len(fileType[-1].split('.mcstructure')) > 1:
            fileType = True
        elif len(fileType[-1].split('.json')) > 1:
            fileType = False
        # 确定文件类型


        relativePath = i.replace(workPath + '/','',1) + '.bdx'

        mkdirPath = os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],relativePath)).replace('\\','/').split('/')
        del mkdirPath[-1]
        mkdirPath = "/".join(mkdirPath)

        creatorModeOutputPath = i.replace(workPath + '/','',1) + '(CreatorMode).json'
        # 确定输入文件的相对路径、文件夹创建路径和开发者模式下的输出路径


        if not os.path.exists(mkdirPath):
            os.makedirs(mkdirPath)
        # 生成文件夹用于输出文件


        Translate = startFunction(
            currentNum,
            allNum,
            workPath,
            i,
            os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],relativePath)).replace('\\','/'),
            file["自定义配置"][customPath[i]]["组件 - 替换方块ID"],
            fileType,
            file["自定义配置"][customPath[i]]["是否跳过空气"],
            [
                file["自定义配置"][customPath[i]]["开发者选项 - 是否启用"],
                os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],creatorModeOutputPath)).replace('\\','/')
            ]
        )
        # 初始化类


        try:
            translateAns = Translate.main()
            errorReason = None
        except:
            errorReason = traceback.format_exc()
            translateAns = False
        # 翻译并生成文件


        if translateAns == False:
            time.sleep(random.randint(5,10) / 10)
            function.showStates(progress = 'failed', provide = [workPath, i, os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],relativePath)).replace('\\','/'), currentNum, allNum])
        # 若失败


        translateLog[i.replace(workPath + '/','',1)] = {
            "SuccessStates": translateAns,
            "errorReason": errorReason,
            "replaceBlockID_errorLog": Translate.rbi_errorLog if translateAns == True else None,
            "replaceBlockID_result": Translate.rbi_result if translateAns == True else None,
            "checkStates": Translate.check if translateAns == True else None,
            "waterWarning": Translate.waterWarning if translateAns == True else None,
            "Warning": Translate.errorList if translateAns == True else None,
            "Container": Translate.experimental if translateAns == True else None,
            "CreatorMode": {
                "enabled": Translate.CreatorMode[0],
                "outputPath": os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],creatorModeOutputPath)).replace('\\','/') if Translate.CreatorMode[0] == True else None
            },
            "outputPath": os.path.normpath(os.path.join(file["自定义配置"][customPath[i]]["文件输出路径"],relativePath)).replace('\\','/') if translateAns == True else None
        }
        # 记录日志


        del Translate
        # 删除已经转换完成的内容



    else:
        fileType = i.split('/')
        if len(fileType[-1].split('.mcstructure')) > 1:
            fileType = True
        elif len(fileType[-1].split('.json')) > 1:
            fileType = False
        # 确定文件类型


        relativePath = i.replace(workPath + '/','',1) + '.bdx'

        mkdirPath = os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],relativePath)).replace('\\','/').split('/')
        del mkdirPath[-1]
        mkdirPath = "/".join(mkdirPath)

        creatorModeOutputPath = i.replace(workPath + '/','',1) + '(CreatorMode).json'
        # 确定输入文件的相对路径、文件夹创建路径和开发者模式下的输出路径


        if not os.path.exists(mkdirPath):
            os.makedirs(mkdirPath)
        # 生成文件夹用于输出文件


        Translate = startFunction(
            currentNum,
            allNum,
            workPath,
            i,
            os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],relativePath)).replace('\\','/'),
            file["全局设置"]["组件 - 替换方块ID"],
            fileType,
            file["全局设置"]["是否跳过空气"],
            [
                file["全局设置"]["开发者选项 - 是否启用"],
                os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],creatorModeOutputPath)).replace('\\','/')
            ]
        )
        # 初始化类


        try:
            translateAns = Translate.main()
            errorReason = None
        except:
            errorReason = traceback.format_exc()
            translateAns = False
        # 翻译并生成文件


        if translateAns == False:
            time.sleep(random.randint(5,10) / 10)
            function.showStates(progress = 'failed', provide = [workPath, i, os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],relativePath)).replace('\\','/'), currentNum, allNum])
        # 若失败


        translateLog[i.replace(workPath + '/','',1)] = {
            "SuccessStates": translateAns,
            "errorReason": errorReason,
            "replaceBlockID_errorLog": Translate.rbi_errorLog if translateAns == True else None,
            "replaceBlockID_result": Translate.rbi_result if translateAns == True else None,
            "checkStates": Translate.check if translateAns == True else None,
            "waterWarning": Translate.waterWarning if translateAns == True else None,
            "Warning": Translate.errorList if translateAns == True else None,
            "Container": Translate.experimental if translateAns == True else None,
            "CreatorMode": {
                "enabled": Translate.CreatorMode[0],
                "outputPath": os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],creatorModeOutputPath)).replace('\\','/') if Translate.CreatorMode[0] == True else None
            },
            "outputPath": os.path.normpath(os.path.join(file["全局设置"]["文件输出路径"],relativePath)).replace('\\','/') if translateAns == True else None
        }
        # 记录日志


        del Translate
        # 删除已经转换完成的内容



# 翻译文件




try:
    os.remove('translator.tmp')
except:
    pass
# 删除缓存用文件(如果存在的话)




with open("translateLog.json","w+",encoding='utf-8') as file:
    file.write(json.dumps(translateLog,sort_keys=True,indent=4,separators=(', ', ': '),ensure_ascii=False))
# 输出日志




print(f'\033[0;32;2018m已完成全部工作，总计遍历了 \033[0m\033[0;37;2018m{len(filePath)}\033[0m \033[0;32;2018m个文件.\033[0m')
print('\033[0;32;2018m翻译日志保存在\033[0m \033[0m\033[0;36;2018m' + os.path.normpath(os.getcwd()).replace('\\','/') + '/translateLog.json\033[0m \033[0;32;2018m处.\033[0m')
os.system("pause")
# 打印结束语