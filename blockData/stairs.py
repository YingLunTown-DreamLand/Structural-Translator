import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    weirdo_direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["weirdo_direction:3"]
    upside_down_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["upside_down_bit:1"]
    #
    if upside_down_bit == 1:
        weirdo_direction = weirdo_direction + 4
    #
    return weirdo_direction