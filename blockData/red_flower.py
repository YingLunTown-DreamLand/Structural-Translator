import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["flower_type:8"]
    #
    if type == 'poppy':
        return 0
    if type == 'orchid':
        return 1
    if type == 'allium':
        return 2
    if type == 'houstonia':
        return 3
    if type == 'tulip_red':
        return 4
    if type == 'tulip_orange':
        return 5
    if type == 'tulip_white':
        return 6
    if type == 'tulip_pink':
        return 7
    if type == 'oxeye':
        return 8
    if type == 'cornflower':
        return 9
    if type == 'lily_of_the_valley':
        return 10
    #