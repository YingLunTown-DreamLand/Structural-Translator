import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    name = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["name:8"]
    persistent_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["persistent_bit:1"]
    update_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["update_bit:1"]
    #
    if name == 'minecraft:leaves' or name == 'minecraft:leaves2':
        try:
            type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["old_leaf_type:8"]
        except:
            None
        try:
            type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["new_leaf_type:8"]
        except:
            None
    else:
        type = None
    #
    if type == 'oak':
        type = 0
        data = 0
    if type == 'spruce':
        type = 0
        data = 1
    if type == 'birch':
        type = 0
        data = 2
    if type == 'jungle':
        type = 0
        data = 3
    #
    if type == 'acacia':
        type = 1
        data = 0
    if type == 'dark_oak':
        type = 1
        data = 1
    #
    if type == 0 or type == 1:
        if persistent_bit == 0 and update_bit == 0:
            return data
        if persistent_bit == 0 and update_bit == 1:
            return data + 4
        if persistent_bit == 1 and update_bit == 0:
            return data + 8
        if persistent_bit == 1 and update_bit == 1:
            return data + 12
    #
    if type == None:
        return 0
    #