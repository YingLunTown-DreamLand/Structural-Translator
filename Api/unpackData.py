import brotli
import struct
import sys
sys.path.append(".")
import Api.indexList
# 载入依赖项

def getBDXdata(path:str)->bytearray:
    with open(path,"r+b") as file:
        return (brotli.decompress((bytearray(b'').join(file.readlines()))[3:]))[4:]
    # return BDXdata:bytearray

def getBDXauthor(input:bytearray)->list:
    context = input.split(bytearray(b'\x00'),maxsplit=1)
    return [context[0].decode(encoding='utf-8'),context[1]]
    # return [authorName:str, remainder:bytearray]

def getType(input:bytearray)->list|bool:
    Type = input[0:1]
    if Type in Api.indexList.indexList:
        return [Api.indexList.indexList[Type],Type,input[1:]]
    else:
        return False
    # return [functionName:str, operation:bytearray, remainder:bytearray]
    # return False:bool

def addX(input:bytearray)->list:
    return [struct.unpack('>H',input[0:2])[0],input[2:]]
    # return [addX:short(int), remainder:bytearray]

def Xaddadd(input:bytearray)->list:
    return [1,input]
    # return [X++(1), remainder:bytearray]

def placeBlock(input:bytearray)->list:
    return [struct.unpack('>H',input[0:2])[0],struct.unpack('>H',input[2:4])[0],input[4:]]
    # return [blockID:short(int), blockData:short(int), remainder:bytearray]

def NOP(input:bytearray)->bytearray:
    return input
    # return remainder:bytearray

def jumpX(input:bytearray)->list:
    return [struct.unpack('>I',input[0:4])[0],input[4:]]
    # return [addX:int, remainder:bytearray]

def addX_int16(input:bytearray):
    return [struct.unpack('>h',input[0:2])[0],input[2:]]
    # return [addX:short(int), remainder:bytearray]

def addX_int32(input:bytearray):
    return [struct.unpack('>i',input[0:4])[0],input[4:]]
    # return [addX:int, remainder:bytearray]

def assignCommandBlockData(input:bytearray)->list:
    strPart = input[4:].split(bytearray(b'\x00'),maxsplit=3)
    return [
        struct.unpack('>I',input[0:4])[0],
        (strPart[0]).decode(encoding='utf-8'),
        (strPart[1]).decode(encoding='utf-8'),
        (strPart[2]).decode(encoding='utf-8'),
        struct.unpack('>i',(strPart[3])[0:4])[0],
        struct.unpack('>u',(strPart[3])[4:5])[0],
        struct.unpack('>u',(strPart[3])[5:6])[0],
        struct.unpack('>u',(strPart[3])[6:7])[0],
        struct.unpack('>u',(strPart[3])[7:8])[0],
        (strPart[3])[8:]
    ]
    # return [
    # mode:int, command:str, name:str, lastoutput:str, tickdelay:int, executeOnFirstTick:bool, 
    # trackOutput:bool, conditional:bool, needRedstone:bool, remainder:bytearray
    # ]

def placeCommandBlockWithData(input:bytearray)->list:
    strPart = input[8:].split(bytearray(b'\x00'),maxsplit=3)
    return [
        struct.unpack('>H',input[0:2])[0],
        struct.unpack('>H',input[2:4])[0],
        struct.unpack('>I',input[4:8])[0],
        (strPart[0]).decode(encoding='utf-8'),
        (strPart[1]).decode(encoding='utf-8'),
        (strPart[2]).decode(encoding='utf-8'),
        struct.unpack('>i',(strPart[3])[0:4])[0],
        struct.unpack('>u',(strPart[3])[4:5])[0],
        struct.unpack('>u',(strPart[3])[5:6])[0],
        struct.unpack('>u',(strPart[3])[6:7])[0],
        struct.unpack('>u',(strPart[3])[7:8])[0],
        (strPart[3])[8:]
    ]
    # return [
    # blockID:short(int), blockData:short(int), mode:int, command:str, name:str, 
    # lastoutput:str, tickdelay:int, executeOnFirstTick:bool, trackOutput:bool, 
    # conditional:bool, needRedstone:bool, remainder:bytearray
    # ]

def addX_int8(input:bytearray)->list:
    return [struct.unpack('>b',input[0:1])[0],input[1:]]
    # return [addX:char(int), remainder:bytearray]

def useRuntimeIdPalette(input:bytearray)->list:
    return [struct.unpack('>B',input[0:1])[0],input[1:]]
    # return [addX:char(int), remainder:bytearray]

def placeCommandBlockWithRuntimeId(input:bytearray)->list:
    strPart = input[6:].split(bytearray(b'\x00'),maxsplit=3)
    return [
        struct.unpack('>H',input[0:2])[0],
        struct.unpack('>I',input[2:6])[0],
        (strPart[0]).decode(encoding='utf-8'),
        (strPart[1]).decode(encoding='utf-8'),
        (strPart[2]).decode(encoding='utf-8'),
        struct.unpack('>i',(strPart[3])[0:4])[0],
        struct.unpack('>u',(strPart[3])[4:5])[0],
        struct.unpack('>u',(strPart[3])[5:6])[0],
        struct.unpack('>u',(strPart[3])[6:7])[0],
        struct.unpack('>u',(strPart[3])[7:8])[0],
        (strPart[3])[8:]
    ]
    # return [
    # runtimeId:short(int), mode:int, command:str, name:str, lastoutput:str, 
    # tickdelay:int, executeOnFirstTick:bool, trackOutput:bool, conditional:bool, 
    # needRedstone:bool, remainder:bytearray
    # ]

def placeBlockWithChestData_int16(input:bytearray)->list:
    runtimeId = struct.unpack('>H',input[0:2])[0]
    ChestDataCount = struct.unpack('>B',input[2:3])[0]
    input = input[3:]
    ChestData = []
    for i in range(ChestDataCount):
        itemName = input.split(bytearray(b'\x00'),maxsplit=1)
        ChestData.append({
            "itemName": (itemName[0]).decode(encoding='utf-8'),
            "itemCount": struct.unpack('>B',(itemName[1])[0:1]),
            "itemData": struct.unpack('>H',(itemName[1])[1:3]),
            "slotID": struct.unpack('>B',(itemName[1])[3:4])
        })
        input = (itemName[1])[4:]
    return [
        runtimeId,
        ChestDataCount,
        ChestData,
        input
    ]
    # return [runtimeId:short(int), slotCount:char(int), ChestData:list]
    # ChestData:list = [{itemName:str, itemCount:char(int), itemData:short(int), slotID:char(int)}]

def placeBlockWithChestData(input:bytearray)->list:
    runtimeId = struct.unpack('>I',input[0:4])[0]
    ChestDataCount = struct.unpack('>B',input[4:5])[0]
    input = input[5:]
    ChestData = []
    for i in range(ChestDataCount):
        itemName = input.split(bytearray(b'\x00'),maxsplit=1)
        ChestData.append({
            "itemName": (itemName[0]).decode(encoding='utf-8'),
            "itemCount": struct.unpack('>B',(itemName[1])[0:1]),
            "itemData": struct.unpack('>H',(itemName[1])[1:3]),
            "slotID": struct.unpack('>B',(itemName[1])[3:4])
        })
        input = (itemName[1])[4:]
    return [
        runtimeId,
        ChestDataCount,
        ChestData,
        input
    ]
    # return [runtimeId:int, slotCount:char(int), ChestData:list]
    # ChestData:list = [{itemName:str, itemCount:char(int), itemData:short(int), slotID:char(int)}]