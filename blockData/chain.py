import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    pillar_axis = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["pillar_axis:8"]
    #
    if pillar_axis == 'y':
        return 0
    if pillar_axis == 'x':
        return 1
    if pillar_axis == 'z':
        return 2
    #