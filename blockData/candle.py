import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    lit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["lit:1"]
    #
    try:
        candles = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["candles:3"]
    except:
        if lit == 1:
            return 1
        else:
            return 0
    #
    if lit == 1:
        candles = candles + 4
    #
    return candles
    #