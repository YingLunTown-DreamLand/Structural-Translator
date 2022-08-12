import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    sponge_type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["sponge_type:8"]
    #
    if sponge_type == 'dry':
        return 0
    if sponge_type == 'wet':
        return 1
    #