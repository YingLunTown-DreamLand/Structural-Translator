import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    name = share.name
    #
    if name == 'minecraft:stone_block_slab':
        type = share.ans["stone_slab_type:8"]
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if type == 'smooth_stone':
            if top_slot_bit == 0:
                return 0
            else:
                return 8
        if type == 'sandstone':
            if top_slot_bit == 0:
                return 1
            else:
                return 9
        if type == 'wood':
            if top_slot_bit == 0:
                return 2
            else:
                return 10
        if type == 'cobblestone':
            if top_slot_bit == 0:
                return 3
            else:
                return 11
        if type == 'brick':
            if top_slot_bit == 0:
                return 4
            else:
                return 12
        if type == 'stone_brick':
            if top_slot_bit == 0:
                return 5
            else:
                return 13
        if type == 'quartz':
            if top_slot_bit == 0:
                return 6
            else:
                return 14
        if type == 'nether_brick':
            if top_slot_bit == 0:
                return 7
            else:
                return 15
        #
    #
    if name == 'minecraft:stone_block_slab4':
        type = share.ans["stone_slab_type_4:8"]
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if type == 'stone':
            if top_slot_bit == 0:
                return 2
            else:
                return 10
        if type == 'mossy_stone_brick':
            if top_slot_bit == 0:
                return 0
            else:
                return 8
        if type == 'smooth_quartz':
            if top_slot_bit == 0:
                return 1
            else:
                return 9
        if type == 'cut_sandstone':
            if top_slot_bit == 0:
                return 3
            else:
                return 11
        if type == 'cut_red_sandstone':
            if top_slot_bit == 0:
                return 4
            else:
                return 12
        #
    #
    if name == 'minecraft:stone_block_slab2':
        type = share.ans["stone_slab_type_2:8"]
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if type == 'red_sandstone':
            if top_slot_bit == 0:
                return 0
            else:
                return 8
        if type == 'purpur':
            if top_slot_bit == 0:
                return 1
            else:
                return 9
        if type == 'prismarine_rough':
            if top_slot_bit == 0:
                return 2
            else:
                return 10
        if type == 'prismarine_dark':
            if top_slot_bit == 0:
                return 3
            else:
                return 11
        if type == 'prismarine_brick':
            if top_slot_bit == 0:
                return 4
            else:
                return 12
        if type == 'mossy_cobblestone':
            if top_slot_bit == 0:
                return 5
            else:
                return 13
        if type == 'smooth_sandstone':
            if top_slot_bit == 0:
                return 6
            else:
                return 14
        if type == 'red_nether_brick':
            if top_slot_bit == 0:
                return 7
            else:
                return 15
        #
    #
    if name == 'minecraft:wooden_slab':
        type = share.ans["wood_type:8"]
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if type == 'oak':
            if top_slot_bit == 0:
                return 0
            else:
                return 8
        if type == 'spruce':
            if top_slot_bit == 0:
                return 1
            else:
                return 9
        if type == 'birch':
            if top_slot_bit == 0:
                return 2
            else:
                return 10
        if type == 'jungle':
            if top_slot_bit == 0:
                return 3
            else:
                return 11
        if type == 'acacia':
            if top_slot_bit == 0:
                return 4
            else:
                return 12
        if type == 'dark_oak':
            if top_slot_bit == 0:
                return 5
            else:
                return 13
        #
    #
    if (name == 'minecraft:mangrove_slab') or (name == 'minecraft:crimson_slab') or (name == 'minecraft:warped_slab') or (name == 'minecraft:blackstone_slab') or (name == 'minecraft:polished_blackstone_slab') or (name == 'minecraft:cut_copper_slab') or (name == 'minecraft:exposed_cut_copper_slab') or (name == 'minecraft:weathered_cut_copper_slab') or (name == 'minecraft:cobbled_deepslate_slab') or (name == 'minecraft:polished_deepslate_slab') or (name == 'minecraft:deepslate_tile_slab') or (name == 'minecraft:deepslate_brick_slab') or (name == 'minecraft:mud_brick_slab'):
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if top_slot_bit == 0:
            return 0
        else:
            return 1
        #
    #
    if name == 'minecraft:stone_block_slab3':
        type = share.ans["stone_slab_type_3:8"]
        top_slot_bit = share.ans["top_slot_bit:1"]
        #
        if type == 'granite':
            if top_slot_bit == 0:
                return 0
            else:
                return 8
        if type == 'smooth_red_sandstone':
            if top_slot_bit == 0:
                return 1
            else:
                return 9
        if type == 'polished_andesite':
            if top_slot_bit == 0:
                return 2
            else:
                return 10
        if type == 'andesite':
            if top_slot_bit == 0:
                return 3
            else:
                return 11
        if type == 'diorite':
            if top_slot_bit == 0:
                return 4
            else:
                return 12
        if type == 'polished_diorite':
            if top_slot_bit == 0:
                return 5
            else:
                return 13
        if type == 'granite':
            if top_slot_bit == 0:
                return 6
            else:
                return 14
        if type == 'polished_granite':
            if top_slot_bit == 0:
                return 7
            else:
                return 15
        #
    #
    if name == 'minecraft:double_stone_block_slab':
        type = share.ans["stone_slab_type:8"]
        #
        if type == 'smooth_stone':
            return 0
        if type == 'sandstone':
            return 1
        if type == 'wood':
            return 2
        if type == 'cobblestone':
            return 3
        if type == 'brick':
            return 4
        if type == 'stone_brick':
            return 5
        if type == 'quartz':
            return 6
        if type == 'nether_brick':
            return 7
        #
    #
    if name == 'minecraft:double_stone_block_slab4':
        type = share.ans["stone_slab_type_4:8"]
        #
        if type == 'stone':
            return 2
        if type == 'mossy_stone_brick':
            return 0
        if type == 'smooth_quartz':
            return 1
        if type == 'cut_sandstone':
            return 3
        if type == 'cut_red_sandstone':
            return 4
        #
    #
    if name == 'minecraft:double_stone_block_slab2':
        type = share.ans["stone_slab_type_2:8"]
        #
        if type == 'red_sandstone':
            return 0
        if type == 'purpur':
            return 1
        if type == 'prismarine_rough':
            return 2
        if type == 'prismarine_dark':
            return 3
        if type == 'prismarine_brick':
            return 4
        if type == 'mossy_cobblestone':
            return 5
        if type == 'smooth_sandstone':
            return 6
        if type == 'red_nether_brick':
            return 7
        #
    #
    if name == 'minecraft:double_wooden_slab':
        type = share.ans["wood_type:8"]
        #
        if type == 'oak':
            return 0
        if type == 'spruce':
            return 1
        if type == 'birch':
            return 2
        if type == 'jungle':
            return 3
        if type == 'acacia':
            return 4
        if type == 'dark_oak':
            return 5
        #
    #
    if name == 'minecraft:double_stone_block_slab3':
        type = share.ans["stone_slab_type_3:8"]
        #
        if type == 'granite':
            return 0
        if type == 'smooth_red_sandstone':
            return 1
        if type == 'polished_andesite':
            return 2
        if type == 'andesite':
            return 3
        if type == 'diorite':
            return 4
        if type == 'polished_diorite':
            return 5
        if type == 'granite':
            return 6
        if type == 'polished_granite':
            return 7
        #
    #
    return 0
    #