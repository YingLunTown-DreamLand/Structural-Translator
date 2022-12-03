import gzip, struct, json
# 载入依赖项





class TranslateMCACBLOCK:
    def __init__(
        self,
        inputPath:str
    )->None:
        """
        \n摘要
        本函数用于去实例化某个项目
        \n参数
        `inputPath:str` 指的是 `.mcacblock` 文件的路径
        """
        # 函数声明

        self.inputPath = inputPath    # 文件输入路径
        self.mcacblock = b''    # mcacblock: bytes
        self.pool = []    # mcstructure 下的方块池
        self.json = {}    # 转义得到的结果
        # 实例化
    
    # 实例化函数



    def main(self) -> None:
        """
        \n摘要
        本函数是 `class: TranslateMCACBLOCK` 的主函数
        \n参数
        `self` 指的是已经被实例化的项目
        \n返回值
        不会返回任何东西(`None`)，但转义得到的 `字典` 将会储存在 `self.json` 中
        """
        # 函数声明

        with open(self.inputPath,"r+b") as file:
            self.mcacblock = gzip.decompress(b''.join(file.readlines()))
        # 取得 mcacblock 数据

        pool_byte_start = self.mcacblock.index(b'dict2strid_:')
        pool_byte_len = struct.unpack('>Q',self.mcacblock[pool_byte_start+12: pool_byte_start+20])[0]
        pool: dict = json.loads(str(self.mcacblock[pool_byte_start+20: pool_byte_start+20+pool_byte_len])[2:][:-1])
        maxNum = max([int(i) for i in list(pool.keys())])
        for i in range(maxNum):
            self.pool.append(pool[str(i+1)])
        # 取得方块池

        blockList_byte_start = self.mcacblock.index(b'DM3Tab_1id_:',pool_byte_start+20+pool_byte_len)
        xSize = struct.unpack('>H',self.mcacblock[blockList_byte_start+32: blockList_byte_start+34])[0]
        ySize = struct.unpack('>H',self.mcacblock[blockList_byte_start+34: blockList_byte_start+36])[0]
        zSize = struct.unpack('>H',self.mcacblock[blockList_byte_start+36: blockList_byte_start+38])[0]
        blockList_byte_len = xSize * ySize * zSize
        blockList = self.mcacblock[blockList_byte_start+38: blockList_byte_start+38+blockList_byte_len]
        blockList = [(i-1) for i in blockList]
        # 取得方块索引表

        self.json = {
            "Root:10":
            {
                "size:9":[xSize, ySize, zSize],
                "structure:10":
                {
                    "block_indices:9":
                    [
                        blockList,
                        [-1 for i in blockList]
                    ],
                    "palette:10":
                    {
                        "default:10":{}
                    }
                }
            }
        }
        # 保存结果