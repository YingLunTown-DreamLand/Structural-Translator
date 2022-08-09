import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["double_plant_type:8"]
    upper_block_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["upper_block_bit:1"]
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