def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = []
    for i in range(numRows):
        res.append([1] * (i + 1))
        if i > 1:
            for j in range(1, i ):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res

print generate(6)


