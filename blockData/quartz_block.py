import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["chisel_type:8"]
    pillar_axis = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["pillar_axis:8"]
    #
    if type == 'default' and pillar_axis == 'y':
        return 0
    if type == 'chiseled' and pillar_axis == 'y':
        return 1
    if type == 'lines' and pillar_axis == 'y':
        return 2
    if type == 'smooth' and pillar_axis == 'y':
        return 3
    if type == 'default' and pillar_axis == 'x':
        return 4
    if type == 'chiseled' and pillar_axis == 'x':
        return 5
    if type == 'lines' and pillar_axis == 'x':
        return 6
    if type == 'smooth' and pillar_axis == 'x':
        return 7
    if type == 'default' and pillar_axis == 'z':
        return 8
    if type == 'chiseled' and pillar_axis == 'z':
        return 9
    if type == 'lines' and pillar_axis == 'z':
        return 10
    if type == 'smooth' and pillar_axis == 'z':
        return 11
    #