import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    open_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["open_bit:1"]
    #
    if open_bit == 1:
        direction = direction + 4
    #
    return direction