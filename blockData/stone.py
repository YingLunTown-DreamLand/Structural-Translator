import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    try:
        Type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["stone_type:8"]
    except:
        None
    try:
        Type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["type:8"]
    except:
        None
    #
    if Type == 'stone':
        return 0
    if Type == 'granite':
        return 1
    if Type == 'granite_smooth':
        return 2
    if Type == 'diorite':
        return 3
    if Type == 'diorite_smooth':
        return 4
    if Type == 'andesite':
        return 5
    if Type == 'andesite_smooth':
        return 6
    #