indexList = {
        b'\x01': 'getBDXauthor', # addToBlockPalette
        b'\x02': 'addX', # addX
        b'\x03': 'Xaddadd', # X++
        b'\x04': 'addX', # addY
        b'\x05': 'Xaddadd', # Y++
        b'\x06': 'addX', # addZ
        b'\x07': 'placeBlock', # placeBlock
        b'\x08': 'Xaddadd', # Z++
        b'\x0a': 'jumpX', # jumpX
        b'\x0b': 'jumpX', # jumpY
        b'\x0c': 'jumpX', # jumpZ
        b'\x0e': 'Xaddadd', # *X++
        b'\x0f': 'Xaddadd', # *X--
        b'\x10': 'Xaddadd', # *Y++
        b'\x11': 'Xaddadd', # *Y--
        b'\x12': 'Xaddadd', # *Z++
        b'\x13': 'Xaddadd', # *Z--
        b'\x14': 'addX_int16', # addX(int16_t)
        b'\x15': 'addX_int32', # addX(int32_t)
        b'\x16': 'addX_int16', # addY(int16_t)
        b'\x17': 'addX_int32', # addY(int32_t)
        b'\x18': 'addX_int16', # addZ(int16_t)
        b'\x19': 'addX_int32', # addZ(int32_t)
        b'\x1a': 'assignCommandBlockData', # assignCommandBlockData
        b'\x1b': 'placeCommandBlockWithData', # placeCommandBlockWithData
        b'\x1c': 'addX_int8', # addX(int8_t)
        b'\x1d': 'addX_int8', # addY(int8_t)
        b'\x1e': 'addX_int8', # addZ(int8_t)
        b'\x1f': 'useRuntimeIdPalette', # useRuntimeIdPalette
        b'\x20': 'addX', # placeBlockWithRuntimeId(uint16_t)	
        b'\x21': 'jumpX', # placeBlockWithRuntimeId
        b'\x22': 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId(uint16_t)
        b'\x23': 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId
        b'\x24': 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithDataNew
        b'\x25': 'placeBlockWithChestData_int16', # placeBlockWithChestData(uint16_t)
        b'\x26': 'placeBlockWithChestData', # placeBlockWithChestData
    }
# 这个列表中每个键是操作编号，其对应的值则是应该调用的 Api.unpack 中的函数



indexListforMain = {
    b'\x01': 'addToBlockPalette', # addToBlockPalette
    b'\x02': 'x+Move-old', # addX
    b'\x03': 'x+Move-old', # X++
    b'\x04': 'y+Move-old', # addY
    b'\x05': 'y+Move-old', # Y++
    b'\x06': 'z+Move-old', # addZ
    b'\x07': 'placeBlock', # placeBlock
    b'\x08': 'z+Move-old', # Z++
    b'\x0a': 'x+Move-old', # jumpX
    b'\x0b': 'y+Move-old', # jumpY
    b'\x0c': 'z+Move-old', # jumpZ
    b'\x0e': 'xMove', # *X++
    b'\x0f': 'xMove', # *X--
    b'\x10': 'yMove', # *Y++
    b'\x11': 'yMove', # *Y--
    b'\x12': 'zMove', # *Z++
    b'\x13': 'zMove', # *Z--
    b'\x14': 'xMove', # addX(int16_t)
    b'\x15': 'xMove', # addX(int32_t)
    b'\x16': 'yMove', # addY(int16_t)
    b'\x17': 'yMove', # addY(int32_t)
    b'\x18': 'zMove', # addZ(int16_t)
    b'\x19': 'zMove', # addZ(int32_t)
    b'\x1a': 'assignCommandBlockData', # assignCommandBlockData
    b'\x1b': 'placeCommandBlockWithData', # placeCommandBlockWithData
    b'\x1c': 'xMove', # addX(int8_t)
    b'\x1d': 'yMove', # addY(int8_t)
    b'\x1e': 'zMove', # addZ(int8_t)
    b'\x1f': 'useRuntimeIdPalette', # useRuntimeIdPalette
    b'\x20': 'placeBlockWithRuntimeId', # placeBlockWithRuntimeId(uint16_t)
    b'\x21': 'placeBlockWithRuntimeId', # placeBlockWithRuntimeId
    b'\x22': 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId(uint16_t)
    b'\x23': 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId
    b'\x24': 'placeCommandBlockWithDataNew', # placeCommandBlockWithDataNew
    b'\x25': 'placeBlockWithChestData', # placeBlockWithChestData(uint16_t)
    b'\x26': 'placeBlockWithChestData', # placeBlockWithChestData
}
# 这个列表中每个键是操作编号，其对应的值则是要实现目标操作的方法名
# 方法无非就是——画笔的移动、放置方块、放置特殊方块，然后再进行细分就可以了