import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    pillar_axis = share.ans["pillar_axis"]
    #
    if pillar_axis == 'y':
        return 0
    if pillar_axis == 'x':
        return 1
    if pillar_axis == 'z':
        return 2
    #