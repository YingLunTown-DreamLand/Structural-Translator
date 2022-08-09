import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    damage = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["damage:8"]
    #
    if damage == 'undamaged':
        return direction
    if damage == 'slightly_damaged':
        return direction + 4
    if damage == 'very_damaged':
        return direction + 8
    #