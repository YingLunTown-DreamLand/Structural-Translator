import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cauldron_liquid = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["cauldron_liquid:8"]
    fill_level = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["fill_level:3"]
    #
    if cauldron_liquid == 'water':
        return fill_level
    if cauldron_liquid == 'lava':
        return fill_level + 8
    #