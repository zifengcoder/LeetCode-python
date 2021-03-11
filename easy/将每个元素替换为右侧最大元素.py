class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(0, len(arr), 1):
            if i == len(arr)-1:
                stack.append(-1)
                break
            temp = arr[i+1]
            for k in range(i+2,len(arr), 1):
                if arr[k] >= temp:
                    temp = arr[k]
            stack.append(temp)
        return stack


    def replaceElements2(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr



if __name__ == '__main__':
    obj = Solution()
    print obj.replaceElements2(arr=[17,18,5,4,6,1])