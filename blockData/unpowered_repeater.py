import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    repeater_delay = share.ans["repeater_delay:3"]
    #
    if repeater_delay > 0:
        return direction + repeater_delay * 4
    else:
        return direction
    #