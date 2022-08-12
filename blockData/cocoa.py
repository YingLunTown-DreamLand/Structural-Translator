import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    age = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["age:3"]
    #
    return direction + age * 4
    #