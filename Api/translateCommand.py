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





def run(command:str)->str:
    ans = []
    pointer = -1


    while True:
        pointer = pointer + 1
        markable = searchForExecute(command,pointer)

        if markable[1] == True:
            selector = getSelector(command,markable[0])
            pos = getPos(command,selector[-1])
            pointer = pos[-1] - 1

            selector = selector[0]
            pos = pos[0]
            ans.append(f'execute as {selector} at {selector} positioned {pos} run ')
        else:
            ans.append(command[markable[0]:])
            break


    return "".join(ans)