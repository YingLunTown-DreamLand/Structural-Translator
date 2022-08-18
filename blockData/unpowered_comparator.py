import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    output_subtract_bit = share.ans["output_lit_bit:1"]
    #
    if output_subtract_bit == 1:
        return direction + 4
    else:
        return direction
    #