import sys
sys.path.append(".")
import Api.ParseBDX.function
import Api.ParseBDX.share
import Api.ParseBDX.indexList
import Api.ParseBDX.unpackData
import Api.ParseBDX.RuntimeIdPalette
import Api.ParseBDX.ContainerIndex
# 载入依赖项







class PaeseBDX:
    def __init__(self,inputPath:str) -> None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `.bdx` 文件的输入路径
        """
        # 函数声明

        self.inputPath = inputPath
        self.resultList = {}
        self.logList = []

    # 实例化





    def main(self) -> None:
        """
        \n摘要
        本函数是 `class: PaeseBDX` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)，但转义得到的 `字典` 和有关日志会分别储存在 `self.resultList` 和 `self.logList` 中。
        """
        # 函数声明



        Api.ParseBDX.share.reset()
        # 重置全局共享变量



        Api.ParseBDX.share.BDXContext = Api.ParseBDX.unpackData.getBDXdata(self.inputPath)
        # 取得解压后的 BDX 数据
        # 舍弃内部文件头 BDX



        authorName = Api.ParseBDX.unpackData.getBDXauthor(Api.ParseBDX.share.BDXContext,0)
        Api.ParseBDX.share.BDXContext = Api.ParseBDX.share.BDXContext[authorName[-1]:]
        authorName = authorName[0]
        # 取得作者之名



        Api.ParseBDX.share.pointer = 0
        Api.ParseBDX.share.penPos = [0,0,0]
        Api.ParseBDX.share.blockPalette = []
        Api.ParseBDX.share.resultList = []
        Api.ParseBDX.share.runtimeIdsBlockPalette = []
        Api.ParseBDX.share.successStates = False
        # 初始化


        while True:
            if Api.ParseBDX.share.BDXContext[Api.ParseBDX.share.pointer:Api.ParseBDX.share.pointer+1] == b'\x58':
                Api.ParseBDX.share.successStates = True
                break
            # 判断是否需要结束

            Api.ParseBDX.share.functionName = Api.ParseBDX.unpackData.getType(Api.ParseBDX.share.BDXContext,Api.ParseBDX.share.pointer)
            if Api.ParseBDX.share.functionName == False:
                break
            Api.ParseBDX.share.pointer = Api.ParseBDX.share.functionName[-1]
            Api.ParseBDX.share.operation = Api.ParseBDX.share.functionName[1]
            operationNum = Api.ParseBDX.share.functionName[2]
            Api.ParseBDX.share.functionName = Api.ParseBDX.share.functionName[0]
            # 取得函数名、操作编号的 Bytes 及 Int 形式
            # 若 Api.ParseBDX.unpackData.getType 返回 False ，则表明文件可能已损坏

            exec(f'Api.ParseBDX.function.{Api.ParseBDX.indexList.indexListforMain[operationNum]}()')
            # 解析 Operation



        if len(Api.ParseBDX.share.recordBlockEntityData) > 0:
            Api.ParseBDX.function.collectionRecordBlockEntityData()
        # 将 operation39(recordBlockEntityData) 找到的 NBT 写入到主列表 Api.ParseBDX.share.resultList 中




        self.resultList = Api.ParseBDX.share.resultList
        # 保存结果



        self.logList = {
            "inputPath": self.inputPath,    # 文件输入路径
            "blockNBT_find_out": [],    # 找到的可以被解析为 str 的 operation 39
            "blockNBT_error": [],    # 找到的无法被解析为 str 的 operation 39
            "authorName": authorName if not authorName == '' else 'unknown',    # 作者名称
            "file_is_integrity": Api.ParseBDX.share.successStates    # 文件是否完整
        }
        # 初始化日志表

        for i in Api.ParseBDX.share.resultList:
            if 'entitynbt' in i:
                self.logList['blockNBT_find_out'].append(i)
        # 写入方块实体日志

        self.logList['blockNBT_error'] = Api.ParseBDX.share.recordBlockEntityDataErrorList
        # 写入方块实体错误日志



        Api.ParseBDX.share.reset()
        # 再次重置全局变量