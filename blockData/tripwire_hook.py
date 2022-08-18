import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    attached_bit = share.ans["attached_bit:1"]
    #
    if attached_bit == 1:
        return direction + 4
    else:
        return direction
    #