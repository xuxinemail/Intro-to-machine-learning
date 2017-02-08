# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
A = [-7, 1, 5, 2, -4, 3, 0]
def solution(A):
    leftsum = 0
    rightsum = sum(A)
    result = []
    # write your code in Python 2.7
    for i, value in enumerate(A):
        rightsum -= value
        if leftsum == rightsum:
            result.append(i)
        leftsum += value
    if result == []:
        return -1
    else: return result[0]


print solution(A)