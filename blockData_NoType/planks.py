import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    #
    Type = share.ans["wood_type"]
    #
    if Type == 'oak':
        return 0
    if Type == 'spruce':
        return 1
    if Type == 'birch':
        return 2
    if Type == 'jungle':
        return 3
    if Type == 'acacia':
        return 4
    if Type == 'dark_oak':
        return 5
    #