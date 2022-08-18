import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    facing_direction = share.ans["torch_facing_direction:8"]
    #
    if facing_direction == 'top':
        return 0
    if facing_direction == 'west':
        return 1
    if facing_direction == 'east':
        return 2
    if facing_direction == 'north':
        return 3
    if facing_direction == 'south':
        return 4
    #