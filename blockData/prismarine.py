import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.ans["prismarine_block_type:8"]
    #
    if type == 'default':
        return 0
    if type == 'dark':
        return 1
    if type == 'bricks':
        return 2
    #