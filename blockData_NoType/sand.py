import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    sand_type = share.ans["sand_type"]
    #
    if sand_type == 'normal':
        return 0
    if sand_type == 'red':
        return 1
    #