class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_list = [int(i) for i in str(n)]
        for i in range(-1, -len(n_list)-1, -1):
            if i == -len(n_list):
                break
            if n_list[i]>n_list[i-1]:
                temp = n_list[i-1]
                temp_list = []
                for x in n_list[i:]:
                    if x > temp:
                        temp_list.append(x)
                min_num_index = n_list.index(min(temp_list), i)
                n_list[i-1] = n_list[min_num_index]
                n_list[min_num_index] = temp
                n_list = n_list[:i] + sorted(n_list[i:])
                break
        n_list_str = [str(i) for i in n_list]
        if int("".join(n_list_str))>n and int("".join(n_list_str))<=(2**31-1):
            return int("".join(n_list_str))
        else:
            return -1






if __name__ == '__main__':
    obj = Solution()
    print obj.nextGreaterElement(n=12388123) # 230241-230412  2147483476-2147483647 101-110