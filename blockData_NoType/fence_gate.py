import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction"]
    open_bit = share.ans["open_bit"]
    #
    if open_bit == 1:
        direction = direction + 4
    #
    return direction