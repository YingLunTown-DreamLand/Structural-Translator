indexList = {
        bytearray(b'\x01'): 'getBDXauthor', # addToBlockPalette
        bytearray(b'\x02'): 'addX', # addX
        bytearray(b'\x03'): 'Xaddadd', # X++
        bytearray(b'\x04'): 'addX', # addY
        bytearray(b'\x05'): 'Xaddadd', # Y++
        bytearray(b'\x06'): 'addX', # addZ
        bytearray(b'\x07'): 'placeBlock', # placeBlock
        bytearray(b'\x08'): 'Xaddadd', # Z++
        bytearray(b'\x09'): 'NOP', # NOP
        bytearray(b'\x0a'): 'jumpX', # jumpX
        bytearray(b'\x0b'): 'jumpX', # jumpY
        bytearray(b'\x0c'): 'jumpX', # jumpZ
        bytearray(b'\x0d'): 'NOP', # reserved
        bytearray(b'\x0e'): 'Xaddadd', # *X++
        bytearray(b'\x0f'): 'Xaddadd', # *X--
        bytearray(b'\x10'): 'Xaddadd', # *Y++
        bytearray(b'\x11'): 'Xaddadd', # *Y--
        bytearray(b'\x12'): 'Xaddadd', # *Z++
        bytearray(b'\x13'): 'Xaddadd', # *Z--
        bytearray(b'\x14'): 'addX_int16', # addX(int16_t)
        bytearray(b'\x15'): 'addX_int32', # addX(int32_t)
        bytearray(b'\x16'): 'addX_int16', # addY(int16_t)
        bytearray(b'\x17'): 'addX_int32', # addY(int32_t)
        bytearray(b'\x18'): 'addX_int16', # addZ(int16_t)
        bytearray(b'\x19'): 'addX_int32', # addZ(int32_t)
        bytearray(b'\x1a'): 'assignCommandBlockData', # assignCommandBlockData
        bytearray(b'\x1b'): 'placeCommandBlockWithData', # placeCommandBlockWithData
        bytearray(b'\x1c'): 'addX_int8', # addX(int8_t)
        bytearray(b'\x1d'): 'addX_int8', # addY(int8_t)
        bytearray(b'\x1e'): 'addX_int8', # addZ(int8_t)
        bytearray(b'\x1f'): 'useRuntimeIdPalette', # useRuntimeIdPalette
        bytearray(b'\x20'): 'addX', # placeBlockWithRuntimeId(uint16_t)	
        bytearray(b'\x21'): 'jumpX', # placeBlockWithRuntimeId
        bytearray(b'\x22'): 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId(uint16_t)
        bytearray(b'\x23'): 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithRuntimeId
        bytearray(b'\x24'): 'placeCommandBlockWithRuntimeId', # placeCommandBlockWithDataNew
        bytearray(b'\x25'): 'placeBlockWithChestData_int16', # placeBlockWithChestData(uint16_t)
    }
# 这个列表中每个键是操作编号，其对应的值则是应该调用的 Api.unpack 中的函数



indexListforMain = {
    bytearray(b'\x01'): 'addToBlockPalette', # addToBlockPalette
    bytearray(b'\x02'): 'x+Move-old', # addX
    bytearray(b'\x03'): 'x+Move-old', # X++
    bytearray(b'\x04'): 'y+Move-old', # addY
    bytearray(b'\x05'): 'y+Move-old', # Y++
    bytearray(b'\x06'): 'z+Move-old', # addZ
    bytearray(b'\x08'): 'z+Move-old', # Z++
    bytearray(b'\x07'): 'placeBlock', # placeBlock
}