import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["tall_grass_type:8"]
    #
    if type == 'default':
        return 0
    if type == 'tall':
        return 1
    if type == 'fern':
        return 2
    if type == 'snow':
        return 3
    #