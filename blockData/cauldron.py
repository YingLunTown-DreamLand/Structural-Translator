import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cauldron_liquid = share.ans["cauldron_liquid:8"]
    fill_level = share.ans["fill_level:3"]
    #
    if cauldron_liquid == 'water':
        return fill_level
    if cauldron_liquid == 'lava':
        return fill_level + 8
    #