import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    attachment = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["attachment:8"]
    #
    direction = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["direction:3"]
    #
    if attachment == 'standing':
        return direction
    if attachment == 'hanging':
        return direction + 4
    if attachment == 'side':
        return direction + 8
    if attachment == 'multiple':
        return direction + 12
    #