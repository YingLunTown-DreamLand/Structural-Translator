import brotli, struct, nbtlib, sys, json
sys.path.append(".")
import Api.ParseBDX.indexList
# 载入依赖项

def getBDXdata(path:str)->bytearray:
    with open(path,"r+b") as file:
        return (brotli.decompress((b''.join(file.readlines()))[3:]))[4:]
    # return BDXdata:bytes

def getBDXauthor(input:bytearray,pointer:int)->list:
    newPoiner = input.index(b'\x00',pointer)
    return [input[pointer:newPoiner].decode(encoding='utf-8'), newPoiner+1]
    # return [authorName:str, newPoiner:int]

def getType(input:bytearray,pointer:int)->list|bool:
    Type = input[pointer]
    TypeByte = input[pointer:pointer+1]
    if Type <= len(Api.ParseBDX.indexList.indexList) - 1:
        return [Api.ParseBDX.indexList.indexList[Type],TypeByte,Type,pointer+1]
    else:
        return False
    # return [functionName:str, operation:bytearray, operationNum:int, newPoiner:int]
    # return False:bool

def addX(input:bytearray,pointer:int)->list:
    return [struct.unpack('>H',input[pointer:pointer+2])[0],pointer+2]
    # return [addX:short(int), newPoiner:int]

def Xaddadd(input:bytearray,pointer:int)->list:
    return [1,pointer]
    # return [X++(1), newPoiner:int]

def placeBlock(input:bytearray,pointer:int)->list:
    return [
        struct.unpack('>H',input[pointer:pointer+2])[0],
        struct.unpack('>H',input[pointer+2:pointer+4])[0],
        pointer+4
        ]
    # return [blockID:short(int), blockData:short(int), newPoiner:int]

def jumpX(input:bytearray,pointer:int)->list:
    return [struct.unpack('>I',input[pointer:pointer+4])[0],pointer+4]
    # return [addX:int, newPoiner:int]

def PlaceBlockWithBlockStates(input:bytearray,pointer:int)->list:
    blockId = struct.unpack('>H',input[pointer:pointer+2])[0]
    # get blockId
    pointer = pointer + 2
    for i in input[pointer:]:
        if i == 32:
            pointer = pointer + 1
        else:
            break
    StringEndLocation = input[pointer:].index(b'\x00') + pointer
    blockStatesEndLocation = StringEndLocation - 1
    # pointer = blockStates_start_location
    # StringEndLocation = String_end_location
    while True:
        if input[blockStatesEndLocation] == 32:
            blockStatesEndLocation = blockStatesEndLocation - 1
        else:
            blockStatesEndLocation = blockStatesEndLocation + 1
            break
    # blockStatesEndLocation = blockStates_end_location
    return [
        blockId,
        json.loads('{' + input[pointer:blockStatesEndLocation].decode(encoding='utf-8')[1:-1] + '}'),
        StringEndLocation + 1
        ]
    # return [blockID:short(int), blockStates:dict, newPointer:int]

def addX_int16(input:bytearray,pointer:int):
    return [struct.unpack('>h',input[pointer:pointer+2])[0],pointer+2]
    # return [addX:short(int), newPoiner:int]

def addX_int32(input:bytearray,pointer:int):
    return [struct.unpack('>i',input[pointer:pointer+4])[0],pointer+4]
    # return [addX:int, newPoiner:int]

def assignCommandBlockData(input:bytearray,pointer:int)->list:
    location1 = input.index(b'\x00',pointer+4)
    command = input[pointer+4:location1]
    # command
    location2 = input.index(b'\x00',location1+1)
    name = input[location1+1:location2]
    # name
    location3 = input.index(b'\x00',location2+1)
    lastoutput = input[location2+1:location3]
    # lastoutput
    return [
        struct.unpack('>I',input[pointer:pointer+4])[0],
        command.decode(encoding='utf-8'),
        name.decode(encoding='utf-8'),
        lastoutput.decode(encoding='utf-8'),
        struct.unpack('>i',input[location3+1:location3+5])[0],
        struct.unpack('>?',input[location3+5:location3+6])[0],
        struct.unpack('>?',input[location3+6:location3+7])[0],
        struct.unpack('>?',input[location3+7:location3+8])[0],
        struct.unpack('>?',input[location3+8:location3+9])[0],
        location3 + 9
    ]
    # return [
    # mode:int, command:str, name:str, lastoutput:str, tickdelay:int, executeOnFirstTick:bool, 
    # trackOutput:bool, conditional:bool, needRedstone:bool, newPoiner:int
    # ]

def placeCommandBlockWithData(input:bytearray,pointer:int)->list:
    location1 = input.index(b'\x00',pointer+8)
    command = input[pointer+8:location1]
    # command
    location2 = input.index(b'\x00',location1+1)
    name = input[location1+1:location2]
    # name
    location3 = input.index(b'\x00',location2+1)
    lastoutput = input[location2+1:location3]
    # lastoutput
    return [
        struct.unpack('>H',input[pointer:pointer+2])[0],
        struct.unpack('>H',input[pointer+2:pointer+4])[0],
        struct.unpack('>I',input[pointer+4:pointer+8])[0],
        command.decode(encoding='utf-8'),
        name.decode(encoding='utf-8'),
        lastoutput.decode(encoding='utf-8'),
        struct.unpack('>i',input[location3+1:location3+5])[0],
        struct.unpack('>?',input[location3+5:location3+6])[0],
        struct.unpack('>?',input[location3+6:location3+7])[0],
        struct.unpack('>?',input[location3+7:location3+8])[0],
        struct.unpack('>?',input[location3+8:location3+9])[0],
        location3 + 9
    ]
    # return [
    # blockID:short(int), blockData:short(int), mode:int, command:str, name:str, 
    # lastoutput:str, tickdelay:int, executeOnFirstTick:bool, trackOutput:bool, 
    # conditional:bool, needRedstone:bool, newPoiner:int
    # ]

def addX_int8(input:bytearray,pointer:int)->list:
    return [struct.unpack('>b',input[pointer:pointer+1])[0],pointer+1]
    # return [addX:char(int), newPoiner:int]

def useRuntimeIdPalette(input:bytearray,pointer:int)->list:
    return [struct.unpack('>B',input[pointer:pointer+1])[0],pointer+1]
    # return [addX:char(int), newPoiner:int]

def placeCommandBlockWithRuntimeId(input:bytearray,pointer:int)->list:
    location1 = input.index(b'\x00',pointer+6)
    command = input[pointer+6:location1]
    # command
    location2 = input.index(b'\x00',location1+1)
    name = input[location1+1:location2]
    # name
    location3 = input.index(b'\x00',location2+1)
    lastoutput = input[location2+1:location3]
    # lastoutput
    return [
        struct.unpack('>H',input[pointer:pointer+2])[0],
        struct.unpack('>I',input[pointer+2:pointer+6])[0],
        command.decode(encoding='utf-8'),
        name.decode(encoding='utf-8'),
        lastoutput.decode(encoding='utf-8'),
        struct.unpack('>i',input[location3+1:location3+5])[0],
        struct.unpack('>?',input[location3+5:location3+6])[0],
        struct.unpack('>?',input[location3+6:location3+7])[0],
        struct.unpack('>?',input[location3+7:location3+8])[0],
        struct.unpack('>?',input[location3+8:location3+9])[0],
        location3 + 9
    ]
    # return [
    # runtimeId:short(int), mode:int, command:str, name:str, lastoutput:str, 
    # tickdelay:int, executeOnFirstTick:bool, trackOutput:bool, conditional:bool, 
    # needRedstone:bool, newPoiner:int
    # ]

def placeBlockWithChestData_int16(input:bytearray,pointer:int)->list:
    runtimeId = struct.unpack('>H',input[pointer:pointer+2])[0]
    repeatCount = struct.unpack('>B',input[pointer+2:pointer+3])[0]
    pointer = pointer + 3
    ChestData = nbtlib.tag.List[nbtlib.tag.Compound]()
    # prepare
    for i in range(repeatCount):
        location = input.index(b'\x00',pointer)
        itemName = input[pointer:location].decode(encoding='utf-8')
        # split by b'\x00'
        ChestData.append(nbtlib.tag.Compound({
            "Name": nbtlib.tag.String(itemName),
            "Count": nbtlib.tag.Byte(struct.unpack('>B',input[location+1:location+2])[0]),
            "Damage": nbtlib.tag.Short(struct.unpack('>H',input[location+2:location+4])[0]),
            "Slot": nbtlib.tag.Byte(struct.unpack('>B',input[location+4:location+5])[0])
        }))
        pointer = location + 5
        # set newPointer
    return [
        runtimeId,
        ChestData,
        pointer
    ]
    # return [runtimeId:short(int), ChestData:list, newPoiner:int]
    # ChestData:list = [{itemName:str, itemCount:char(int), itemData:short(int), slotID:char(int)}]

def placeBlockWithChestData(input:bytearray,pointer:int)->list:
    runtimeId = struct.unpack('>I',input[pointer:pointer+4])[0]
    repeatCount = struct.unpack('>B',input[pointer+4:pointer+5])[0]
    pointer = pointer + 5
    ChestData = nbtlib.tag.List[nbtlib.tag.Compound]()
    # prepare
    for i in range(repeatCount):
        location = input.index(b'\x00',pointer)
        itemName = input[pointer:location].decode(encoding='utf-8')
        # split by b'\x00'
        ChestData.append(nbtlib.tag.Compound({
            "Name": nbtlib.tag.String(itemName),
            "Count": nbtlib.tag.Byte(struct.unpack('>B',input[location+1:location+2])[0]),
            "Damage": nbtlib.tag.Short(struct.unpack('>H',input[location+2:location+4])[0]),
            "Slot": nbtlib.tag.Byte(struct.unpack('>B',input[location+4:location+5])[0])
        }))
        pointer = location + 5
        # set newPointer
    return [
        runtimeId,
        ChestData,
        pointer
    ]
    # return [runtimeId:int, ChestData:list, newPoiner:int]
    # ChestData:list = [{itemName:str, itemCount:char(int), itemData:short(int), slotID:char(int)}]

def recordBlockEntityData(input:bytearray,pointer:int)->list:
    newPointer = pointer + 4 + struct.unpack('>I',input[pointer:pointer+4])[0]
    buffer = []
    for i in input[pointer+4:newPointer]:
        buffer.append(i)
    return [
            buffer,
            newPointer
        ]
    # return [blockNBT:list, newPoiner:int]
    # example: blockNBT = [2,3,4,1] -> b'\x02\x03\x04\x01'