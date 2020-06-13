def top_and_bottom(li: list, n: int):
    returnList = []
    if checkLists(li) is False:  # check if there are no lists inside list
        while len(li) >= n * 2:  # n*2 to account for the back
            for i in range(n):
                returnList.append(li[0])
                li.pop(0)  # pop start
            for i in range(n):
                returnList.append(li[-1])
                li.pop()  # pop end
        returnList.append(li)
    else:
        while len(li) >= n * 2:
            for i in range(n):
                if type(li[i]) == list:
                    li[i] = top_and_bottom(li[i])  # recurse if type is list
    print(li)
    print(returnList)


def checkLists(li: list):
    for element in li:
        if type(element) == list:
            return True
    return False


top_and_bottom([1, 2, 3, 4, 5, 6, 7], 2)
