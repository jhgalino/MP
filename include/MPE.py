def differentiate(fxn: str):
    hasCoeff = False
    hasExp = False
    hasTrig = False
    diff = ""

    # separate string into three parts which containe exponent, coeff,
    # and the function inside the parentheses
    def splitByParentheses(function: str):
        function = function.replace("(", "~", 1)
        function = function[::-1].replace(")", "~", 1)
        function = function[::-1].split("~")
        return function

    tempFxn = splitByParentheses(fxn)

    if len(tempFxn) < 3:  # if x is the only then left, omit x
        return

    if tempFxn[0] != "" and tempFxn[0].isdecimal():
        hasCoeff = True
    elif tempFxn[0] != "" and tempFxn[0].isalpha():
        hasTrig = True

    if tempFxn[-1] != "" and tempFxn[-1][-1].isdecimal():
        hasExp = True

    # if fxn is (x)
    if tempFxn[1] == "x" and tempFxn[0] == "" and tempFxn[2] == "":
        return 1

    if hasExp and hasCoeff:  # change coeff and exp into ints, then calculate
        tempFxn[0] = int(tempFxn[0])
        tempFxn[2] = int(tempFxn[2][1])
        tempFxn[0] = tempFxn[0] * tempFxn[2]
        tempFxn[2] -= 1
