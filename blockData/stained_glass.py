import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    type = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["color:8"]
    #
    if type == 'white':
        return 0
    if type == 'orange':
        return 1
    if type == 'magenta':
        return 2
    if type == 'light_blue':
        return 3
    if type == 'yellow':
        return 4
    if type == 'lime':
        return 5
    if type == 'pink':
        return 6
    if type == 'gray':
        return 7
    if type == 'silver':
        return 8
    if type == 'cyan':
        return 9
    if type == 'purple':
        return 10
    if type == 'blue':
        return 11
    if type == 'brown':
        return 12
    if type == 'green':
        return 13
    if type == 'red':
        return 14
    if type == 'black':
        return 15
    #