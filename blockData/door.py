import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    open_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["open_bit:1"]
    try:
        upside_down_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["upside_down_bit:1"]
    except:
        upside_down_bit = None
    #
    if (open_bit == 1 and upside_down_bit == None) or (open_bit == 0 and upside_down_bit == 1):
        direction = direction + 4
    if open_bit == 1 and upside_down_bit == 0:
        direction = direction + 8
    if open_bit == 1 and upside_down_bit == 1:
        direction = direction + 12
    #
    return direction
    #