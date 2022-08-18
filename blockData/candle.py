import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    lit = share.ans["lit:1"]
    #
    try:
        candles = share.ans["candles:3"]
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