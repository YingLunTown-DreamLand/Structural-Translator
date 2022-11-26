import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    try:
        Type = share.ans["stone_type"]
    except:
        None
    try:
        Type = share.ans["type"]
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