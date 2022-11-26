import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    name = share.name
    pillar_axis = share.ans["pillar_axis"]
    #
    if name == 'minecraft:log' or name == 'minecraft:log2':
        try:
            type = share.ans["old_log_type"]
        except:
            None
        try:
            type = share.ans["new_log_type"]
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