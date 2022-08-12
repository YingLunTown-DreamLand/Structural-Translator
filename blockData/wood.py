import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    #
    Type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["wood_type:8"]
    stripped_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["stripped_bit:1"]
    #
    if Type == 'oak':
        data = 0
    if Type == 'spruce':
        data = 1
    if Type == 'birch':
        data = 2
    if Type == 'jungle':
        data = 3
    if Type == 'acacia':
        data = 4
    if Type == 'dark_oak':
        data = 5
    #
    if stripped_bit == 1:
        return data + 8
    else:
        return data
    #