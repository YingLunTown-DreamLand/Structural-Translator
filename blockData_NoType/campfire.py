import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction"]
    extinguished = share.ans["extinguished"]
    #
    if extinguished == 1:
        direction = direction + 4
    #
    return direction
    #