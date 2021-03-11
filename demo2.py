def merge(A, B):
    ans = []
    while A or B:
        bigger = A if A > B else B
        ans.append(bigger[0])
        bigger.pop(0)
    return ans

print merge(A=[6, 5], B=[9,8,3])