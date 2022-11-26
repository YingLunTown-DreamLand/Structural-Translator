import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cauldron_liquid = share.ans["cauldron_liquid"]
    fill_level = share.ans["fill_level"]
    #
    if cauldron_liquid == 'water':
        return fill_level
    if cauldron_liquid == 'lava':
        return fill_level + 8
    #