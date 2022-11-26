import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    portal_axis = share.ans["portal_axis"]
    #
    if portal_axis == 'unknown' or portal_axis == 'z':
        return 2
    if portal_axis == 'x':
        return 1
    #