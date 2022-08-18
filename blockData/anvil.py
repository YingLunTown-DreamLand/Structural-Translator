import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    damage = share.ans["damage:8"]
    #
    if damage == 'undamaged':
        return direction
    if damage == 'slightly_damaged':
        return direction + 4
    if damage == 'very_damaged':
        return direction + 8
    #