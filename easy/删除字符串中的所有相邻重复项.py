def removeDuplicates(S):
    """
    :type S: str
    :rtype: str
    """
    stack = []
    for i in S:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)


if __name__ == '__main__':
    S = "abbaca"
    print removeDuplicates(S)
