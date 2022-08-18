import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    extinguished = share.ans["extinguished:1"]
    #
    if extinguished == 1:
        direction = direction + 4
    #
    return direction
    #