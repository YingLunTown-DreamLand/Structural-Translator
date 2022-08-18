import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    age_bit = share.ans["age_bit:1"]
    bamboo_leaf_size = share.ans["bamboo_leaf_size:8"]
    bamboo_stalk_thickness = share.ans["bamboo_stalk_thickness:8"]
    #
    if bamboo_stalk_thickness == 'thick':
        data = 1
    else:
        data = 0
    #
    if bamboo_leaf_size == 'small_leaves':
        data = data + 2
    if bamboo_leaf_size == 'large_leaves':
        data = data + 4
    #
    if age_bit == 1:
        return data + 8
    else:
        return data
    #