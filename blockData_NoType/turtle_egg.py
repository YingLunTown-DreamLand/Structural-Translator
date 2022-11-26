import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cracked_state = share.ans["cracked_state"]
    turtle_egg_count = share.ans["turtle_egg_count"]
    #
    if turtle_egg_count == 'one_egg':
        data = 0
    if turtle_egg_count == 'two_egg':
        data = 1
    if turtle_egg_count == 'three_egg':
        data = 2
    if turtle_egg_count == 'four_egg':
        data = 3
    #
    if cracked_state == 'no_cracks':
        return data
    if cracked_state == 'cracked':
        return data + 4
    if cracked_state == 'max_cracked':
        return data + 8
    #