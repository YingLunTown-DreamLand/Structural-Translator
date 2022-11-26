import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    wood_type = share.ans["wood_type"]
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