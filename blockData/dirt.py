import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    dirt_type = share.ans["dirt_type:8"]
    #
    if dirt_type == 'normal':
        return 0
    if dirt_type == 'coarse':
        return 1
    #