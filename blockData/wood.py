import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    #
    Type = share.ans["wood_type:8"]
    stripped_bit = share.ans["stripped_bit:1"]
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