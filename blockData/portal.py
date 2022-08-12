import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    portal_axis = share.mcs["Root:10"]["structure:10"]["palette:10"]["default:10"]["block_palette:9"][share.pointer]["states:10"]["portal_axis:8"]
    #
    if portal_axis == 'unknown' or portal_axis == 'z':
        return 2
    if portal_axis == 'x':
        return 1
    #