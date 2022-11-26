import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction"]
    attached_bit = share.ans["attached_bit"]
    #
    if attached_bit == 1:
        return direction + 4
    else:
        return direction
    #