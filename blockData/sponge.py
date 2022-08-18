import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    sponge_type = share.ans["sponge_type:8"]
    #
    if sponge_type == 'dry':
        return 0
    if sponge_type == 'wet':
        return 1
    #