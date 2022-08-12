import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    rail_direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["rail_direction:3"]
    try:
        rail_data_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["rail_data_bit:1"]
    except:
        rail_data_bit = 0
    #
    if rail_data_bit == 1:
        return rail_direction + 8
    else:
        return rail_direction
    #