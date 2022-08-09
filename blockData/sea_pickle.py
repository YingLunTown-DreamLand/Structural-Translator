import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cluster_count = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["cluster_count:3"]
    dead_bit = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["dead_bit:1"]
    #
    if dead_bit == 1:
        return cluster_count + 4
    else:
        return cluster_count
    #