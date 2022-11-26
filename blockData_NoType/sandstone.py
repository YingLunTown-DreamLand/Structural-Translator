import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.ans["sand_stone_type"]
    #
    if type == 'default':
        return 0
    if type == 'heiroglyphs':
        return 1
    if type == 'cut':
        return 2
    if type == 'smooth':
        return 3
    #