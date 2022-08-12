import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    monster_egg_stone_type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["monster_egg_stone_type:8"]
    #
    if monster_egg_stone_type == 'stone':
        return 0
    if monster_egg_stone_type == 'cobblestone':
        return 1
    if monster_egg_stone_type == 'stone_brick':
        return 2
    if monster_egg_stone_type == 'mossy_stone_brick':
        return 3
    if monster_egg_stone_type == 'cracked_stone_brick':
        return 4
    if monster_egg_stone_type == 'chiseled_stone_brick':
        return 5
    #