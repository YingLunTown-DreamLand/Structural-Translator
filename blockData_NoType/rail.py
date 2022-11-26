import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    rail_direction = share.ans["rail_direction"]
    try:
        rail_data_bit = share.ans["rail_data_bit"]
    except:
        rail_data_bit = 0
    #
    if rail_data_bit == 1:
        return rail_direction + 8
    else:
        return rail_direction
    #