import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    direction = share.ans["direction:3"]
    #
    end_portal_eye_bit = share.ans["end_portal_eye_bit:1"]
    #
    if end_portal_eye_bit == 1:
        direction = direction + 4
    #
    return direction
    #