import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    lever_direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["lever_direction:8"]
    open_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["open_bit:1"]
    #
    if lever_direction == 'down_east_west':
        direction = 0
    if lever_direction == 'east':
        direction = 1
    if lever_direction == 'west':
        direction = 2
    if lever_direction == 'south':
        direction = 3
    if lever_direction == 'north':
        direction = 4
    if lever_direction == 'up_north_south':
        direction = 5
    if lever_direction == 'up_east_west':
        direction = 6
    if lever_direction == 'down_north_south':
        direction = 7
    #
    if open_bit == 1:
        return direction + 8
    else:
        return direction
    #