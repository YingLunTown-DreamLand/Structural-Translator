import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction"]
    open_bit = share.ans["open_bit"]
    try:
        upside_down_bit = share.ans["upside_down_bit"]
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