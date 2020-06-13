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
        returnList.extend(li)
        return returnList
    else:
        while len(li) >= n * 2:
            for i in range(n):
                if type(li[0]) == list:
                    li[0] = top_and_bottom(li[0], n)  # recurse if type is list
                    returnList.append(li[0])
                    li.pop(0)
                else:
                    returnList.append(li[0])
                    li.pop(0)
            for i in range(n):
                if type(li[-1]) == list:
                    li[-1] = top_and_bottom(li[-1], n)
                    returnList.append(li[-1])
                    li.pop()
                else:
                    returnList.append(li[-1])
                    li.pop()
        returnList.extend(li)
        return returnList


def checkLists(li: list):
    for element in li:
        if type(element) == list:
            return True
    return False


print(top_and_bottom([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
