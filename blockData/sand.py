import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    sand_type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["sand_type:8"]
    #
    if sand_type == 'normal':
        return 0
    if sand_type == 'red':
        return 1
    #