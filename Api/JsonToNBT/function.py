from nbtlib.tag import *
# 载入依赖项





def JSONCompound(input:dict)->Compound:
    ans = Compound({})
    # 初始化


    for i in input:
        if i[-1:] == '1':
            if i[-2:] != '11':
                ans[i[:-2]] = Byte(input[i])
                continue
            else:
                ans[i[:-3]] = IntArray(input[i])
                continue
        # byte or int_array

        if i[-1:] == '2':
            if i[-2:] != '12':
                ans[i[:-2]] = Short(input[i])
                continue
            else:
                ans[i[:-3]] = LongArray(input[i])
                continue
        # short or long_array

        if i[-1:] == '3':
            ans[i[:-2]] = Int(input[i])
            continue
        # int
        if i[-1:] == '4':
            ans[i[:-2]] = Long(input[i])
            continue
        # long
        if i[-1:] == '5':
            ans[i[:-2]] = Float(input[i])
            continue
        # float
        if i[-1:] == '6':
            ans[i[:-2]] = Double(input[i])
            continue
        # double
        if i[-1:] == '7':
            ans[i[:-2]] = ByteArray(input[i])
            continue
        # list-byte_array
        if i[-1:] == '8':
            ans[i[:-2]] = String(input[i])
            continue
        # string
        if i[-1:] == '9':
            ans[i[:-2]] = JSONList(input[i])
            continue
        # list
        if i[-2:] == '10':
            ans[i[:-3]] = JSONCompound(input[i])
            continue
        # compound


    return ans
    # 返回值





def JSONList(input:list)->List:
    if len(input) == 0:
        return List([])
    # if input == []


    if type(input[0]) == int:
        return List[Int](input)
    # int


    if type(input[0]) == dict:
        return List[Compound]([JSONCompound(i) for i in input])
    # compound


    if type(input[0]) == list:
        if len(input[0]) == 0:
            return List([List([])])
            # input[0] == []

        if type(input[0][0]) == int:
            return List[IntArray](input)
            # int_array

        if type(input[0][0]) == list:
            return List[List]([JSONList(i) for i in input])
            # list

        if input[0][0][-2:] == '07':
            return List[ByteArray]([[int(i1[:-3]) for i1 in i] for i in input])
            # list-byte_array
        if input[0][0][-2:] == '12':

            return List[LongArray]([[int(i1[:-3]) for i1 in i] for i in input])
            # list-long-array
    # list


    if input[0][-2:] == '01':
        input = [int(i[:-3]) for i in input]
        return List[Byte](input)
    # byte
    if input[0][-2:] == '02':
        input = [int(i[:-3]) for i in input]
        return List[Short](input)
    # short
    if input[0][-2:] == '03':
        input = [int(i[:-3]) for i in input]
        return List[Int](input)
    # int
    if input[0][-2:] == '04':
        input = [int(i[:-3]) for i in input]
        return List[Long](input)
    # long
    if input[0][-2:] == '05':
        input = [float(i[:-3]) for i in input]
        return List[Float](input)
    # float
    if input[0][-2:] == '06':
        input = [float(i[:-3]) for i in input]
        return List[Double](input)
    # double
    if input[0][-2:] == '08':
        input = [i[:-3] for i in input]
        return List[String](input)
    # string