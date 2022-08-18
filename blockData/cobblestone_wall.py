import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    dirt_type = share.ans["wall_block_type:8"]
    #
    if dirt_type == 'cobblestone':
        return 0
    if dirt_type == 'mossy_cobblestone':
        return 1
    if dirt_type == 'granite':
        return 2
    if dirt_type == 'diorite':
        return 3
    if dirt_type == 'andesite':
        return 4
    if dirt_type == 'sandstone':
        return 5
    if dirt_type == 'brick':
        return 6
    if dirt_type == 'stone_brick':
        return 7
    if dirt_type == 'mossy_stone_brick':
        return 8
    if dirt_type == 'nether_brick':
        return 9
    if dirt_type == 'end_brick':
        return 10
    if dirt_type == 'prismarine':
        return 11
    if dirt_type == 'red_sandstone':
        return 12
    if dirt_type == 'red_nether_brick':
        return 13
    #