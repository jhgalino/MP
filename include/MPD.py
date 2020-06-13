def top_and_bottom(li: list, n: int):
    returnList = []
    while len(li) >= n * 2:
        for i in range(n):
            returnList.append(li[0])
            li.pop(0)
        for i in range(n):
            returnList.append(li[-1])
            li.pop()
    print(li)
    print(returnList)


top_and_bottom([1, 2, 3, 4, 5, 6, 7], 2)
