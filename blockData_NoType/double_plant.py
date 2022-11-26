import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.ans["double_plant_type"]
    upper_block_bit = share.ans["upper_block_bit"]
    #
    if type == 'sunflower':
        data = 0
    if type == 'syringa':
        data = 1
    if type == 'grass':
        data = 2
    if type == 'fern':
        data = 3
    if type == 'rose':
        data = 4
    if type == 'paeonia':
        data = 5
    #
    if upper_block_bit == 1:
        return [data,'摆烂']
    else:
        return data
    #