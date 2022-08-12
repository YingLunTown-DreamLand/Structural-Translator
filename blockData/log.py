import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    name = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["name:8"]
    pillar_axis = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["pillar_axis:8"]
    #
    if name == 'minecraft:log' or name == 'minecraft:log2':
        try:
            type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["old_log_type:8"]
        except:
            None
        try:
            type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["new_log_type:8"]
        except:
            None
    else:
        type = None
    #
    if type =='oak' and pillar_axis =='y':
        return 0
    if type =='spruce' and pillar_axis =='y':
        return 1
    if type =='birch' and pillar_axis =='y':
        return 2
    if type =='jungle' and pillar_axis =='y':
        return 3
    #
    if type =='oak' and pillar_axis =='x':
        return 4
    if type =='spruce' and pillar_axis =='x':
        return 5
    if type =='birch' and pillar_axis =='x':
        return 6
    if type =='jungle' and pillar_axis =='x':
        return 7
    #
    if type =='oak' and pillar_axis =='z':
        return 8
    if type =='spruce' and pillar_axis =='z':
        return 9
    if type =='birch' and pillar_axis =='z':
        return 10
    if type =='jungle' and pillar_axis =='z':
        return 11
    #
    if type =='acacia' and pillar_axis =='y':
        return 0
    if type =='dark_oak' and pillar_axis =='y':
        return 1
    #
    if type =='acacia' and pillar_axis =='x':
        return 4
    if type =='dark_oak' and pillar_axis =='x':
        return 5
    #
    if type =='acacia' and pillar_axis =='z':
        return 8
    if type =='dark_oak' and pillar_axis =='z':
        return 9
    #
    if type == None and pillar_axis =='y':
        return 0
    if type == None and pillar_axis =='x':
        return 1
    if type == None and pillar_axis =='z':
        return 2
    #