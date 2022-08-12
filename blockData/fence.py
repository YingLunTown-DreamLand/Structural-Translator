import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    wood_type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["wood_type:8"]
    #
    if wood_type == 'oak':
        return 0
    if wood_type == 'spruce':
        return 1
    if wood_type == 'birch':
        return 2
    if wood_type == 'jungle':
        return 3
    if wood_type == 'acacia':
        return 4
    if wood_type == 'dark_oak':
        return 5
    #