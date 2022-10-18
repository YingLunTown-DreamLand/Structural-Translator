def jumpSpace(command:str,pointer:int)->int:
    while True:
        if pointer >= len(command) - 1:
            return pointer
        elif command[pointer] == ' ' or command[pointer] == '/':
            pointer = pointer + 1
        else:
            return pointer





def highSearching(command:str,pointer:int,input:list)->int:
    List = [[command.find(i,pointer),len(i)] for i in input]
    ans = []
    for i in List:
        if i[0] != -1:
            ans.append(i)
    ans.sort()
    return [
        ans[0][0],
        ans[0][1]
    ]





def getRightBarrier(command:str,pointer:int)->int:
    while True:
        quotationMark = command.find('"',pointer)
        barrier = command.index(']',pointer)
        if quotationMark == -1:
            return barrier
        elif quotationMark < barrier:
            pointer = command.find('"',quotationMark+1) + 1
        else:
            return barrier





def searchForExecute(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    if command[pointer:pointer+7].replace('E','e').replace('X','x').replace('C','c').replace('U','u',).replace('T','t') == 'execute':
        return [pointer+7,True]
    else:
        return [pointer,False]





def getSelector(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    if command[pointer] == '@':
        transit = highSearching(command,pointer,['@s','@a','@p','@e','@r','@initiator','@c','@v'])
        selector = command[
            pointer:
            transit[0] + transit[1]
        ]
        pointer = jumpSpace(command,transit[0] + transit[1])
        if pointer >= len(command) - 1:
            return [selector,pointer]
        elif command[pointer] != '[':
            return [selector,pointer]
        else:
            transit = getRightBarrier(command,pointer)
            return [
                selector + command[
                    pointer:
                    transit + 1
                ],
                transit + 1
            ]
    elif command[pointer] == '"':
        transit = command.index('"',pointer + 1)
        return [
            command[pointer:transit + 1],
            transit + 1
        ]
    else:
        transit = highSearching(command,pointer,[' ','^','~'])
        return [
            command[
                pointer:
                transit[0] + transit[1] - 1
            ],
            transit[0] + transit[1] - 1
        ]





def getPos(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    ans = []
    for i in range(3):
        transit = highSearching(command,pointer+1,[' ','^','~','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
        'P','Q','R','S','T','U','V','W','X','Y','Z','?','/'])

        successStates = False
        for i in ['^','~','0','1','2','3','4','5','6','7','8','9']:
            if command[pointer][0] == i:
                successStates = True

        if successStates == False:
            return False

        ans.append(
            command[
                pointer:
                transit[0]
            ])
        pointer = jumpSpace(command,transit[0])
    return [
        ans[0] + ' ' + ans[1] + ' ' + ans[2],
        pointer
    ]





def detectBlock(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    if command[pointer:pointer+6].replace('D','d').replace('E','e').replace('T','t').replace('C','c') == 'detect':
        pointer = getPos(command,jumpSpace(command,pointer+6))
        pos = pointer[0]
        startLocation = pointer = jumpSpace(command,pointer[-1])
        endLocation = command.index(' ',pointer)
        spaceLocation = command.index(' ',jumpSpace(command,endLocation + 1))
        return [
            True,
            f' if block {pos} {command[startLocation:endLocation]} {command[endLocation + 1:spaceLocation]}',
            spaceLocation
        ]
    else:
        return [
            False,
            pointer
        ]





def run(command:str)->str:
    ans = []
    pointer = -1


    while True:
        pointer = pointer + 1
        markable = searchForExecute(command,pointer)

        if markable[1] == True:
            selector = getSelector(command,markable[0])
            pos = getPos(command,selector[-1])
            detect = detectBlock(command,pos[-1])
            pointer = detect[-1] - 1

            selector = selector[0]
            pos = pos[0]
            detect = detect[1] if detect[0] == True else ''

            ans.append(
                f'execute as {selector} at {selector}{detect} run 'f'execute as {selector} at {selector}{detect} run ' if (
                    pos == '~ ~ ~') else f'execute as {selector} at {selector} positioned {pos}{detect} run '
            )
        else:
            ans.append(command[markable[0]:])
            break


    return "".join(ans)