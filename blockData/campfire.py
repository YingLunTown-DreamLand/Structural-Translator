import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    extinguished = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["extinguished:1"]
    #
    if extinguished == 1:
        direction = direction + 4
    #
    return direction
    #