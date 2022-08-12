import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    dirt_type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["dirt_type:8"]
    #
    if dirt_type == 'normal':
        return 0
    if dirt_type == 'coarse':
        return 1
    #