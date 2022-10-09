indexList = [
    '', # 占位符
    'getBDXauthor', # addToBlockPalette
    'addX', # addX
    'Xaddadd', # X++
    'addX', # addY
    'Xaddadd', # Y++
    'addX', # addZ
    'placeBlock', # placeBlock
    'Xaddadd', # Z++
    '', # NOP
    'jumpX', # jumpX
    'jumpX', # jumpY
    'jumpX', # jumpZ
    '', # reserved
    'Xaddadd', # *X++
    'Xaddadd', # *X--
    'Xaddadd', # *Y++
    'Xaddadd', # *Y--
    'Xaddadd', # *Z++
    'Xaddadd', # *Z--
    'addX_int16', # addX(int16_t)
    'addX_int32', # addX(int32_t)
    'addX_int16', # addY(int16_t)
    'addX_int32', # addY(int32_t)
    'addX_int16', # addZ(int16_t)
    'addX_int32', # addZ(int32_t)
    'assignCommandBlockData', # assignCommandBlockData
    'placeCommandBlockWithData', # placeCommandBlockWithData
    'addX_int8', # addX(int8_t)
    'addX_int8', # addY(int8_t)
    'addX_int8', # addZ(int8_t)
    'useRuntimeIdPalette', # useRuntimeIdPalette
    'addX', # placeBlockWithRuntimeId(uint16_t)	
    'jumpX', # placeBlockWithRuntimeId
    'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId(uint16_t)
    'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId
    'placeCommandBlockWithRuntimeId', # placeCommandBlockWithDataNew
    'placeBlockWithChestData_int16', # placeBlockWithChestData(uint16_t)
    'placeBlockWithChestData', # placeBlockWithChestData
    ]
# 此列表用于解包部分
# Api.unpack



indexListforMain = [
    '', # 占位符
    'addToBlockPalette', # addToBlockPalette
    'xMoveOld', # addX
    'xMoveOld', # X++
    'yMoveOld', # addY
    'yMoveOld', # Y++
    'zMoveOld', # addZ
    'placeBlock', # placeBlock
    'zMoveOld', # Z++
    '', # NOP
    'xMoveOld', # jumpX
    'yMoveOld', # jumpY
    'zMoveOld', # jumpZ
    '', # reserved
    'xMove', # *X++
    'xMove', # *X--
    'yMove', # *Y++
    'yMove', # *Y--
    'zMove', # *Z++
    'zMove', # *Z--
    'xMove', # addX(int16_t)
    'xMove', # addX(int32_t)
    'yMove', # addY(int16_t)
    'yMove', # addY(int32_t)
    'zMove', # addZ(int16_t)
    'zMove', # addZ(int32_t)
    'assignCommandBlockData', # assignCommandBlockData
    'placeCommandBlockWithData', # placeCommandBlockWithData
    'xMove', # addX(int8_t)
    'yMove', # addY(int8_t)
    'zMove', # addZ(int8_t)
    'useRuntimeIdPalette', # useRuntimeIdPalette
    'placeBlockWithRuntimeId', # placeBlockWithRuntimeId(uint16_t)
    'placeBlockWithRuntimeId', # placeBlockWithRuntimeId
    'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId(uint16_t)
    'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId
    'placeCommandBlockWithDataNew', # placeCommandBlockWithDataNew
    'placeBlockWithChestData', # placeBlockWithChestData(uint16_t)
    'placeBlockWithChestData', # placeBlockWithChestData
    ]
# 此列表用于实现具体的 operation 方法
# Api.function
# 实现这些方法无非就是——画笔的移动、放置方块、放置特殊方块，然后再进行细分就可以了
