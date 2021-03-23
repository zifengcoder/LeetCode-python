# coding=utf-8
import collections


class Solution(object):
    def findLongestSubarray(self, array):
        """
        :type array: List[str]
        :rtype: List[str]
        """
        result = {}
        for j in range(len(array)):
            num_list = []
            arr_list = []
            max_list = []
            for i in array[j:]:
                if i.isdigit():
                    num_list.append(i)
                else:
                    arr_list.append(i)
                if len(num_list) == len(arr_list):
                    max_list.append(arr_list + num_list)
            if max_list:
                result[j] = len(max(max_list))
        if result:
            start_index = min([k for k, v in result.items() if v == max(result.values())])
            end_index = max(result.values())
            return array[start_index:start_index + end_index]
        else:
            return []


    def findLongestSubarray2(self, array):
        """
        前缀和得方式，字母为1， 数字为-1
        :type array: List[str]
        :rtype: List[str]
        """
        array_len = len(array)
        memo = [-2 for i in range((array_len << 1) + 1)]
        memo[array_len] = -1
        begin, end = 0, 0
        res, count = 0, 0
        for i in range(array_len):
            is_num = True
            for ch in array[i]:
                if (ord(ch) < ord('0')) or (ord(ch) > ord('9')):
                    is_num = False
                    break
            count += -1 if is_num else 1
            if memo[count + array_len] <= -2:
                memo[count + array_len] = i
            elif i - memo[count + array_len] > res:
                begin, end = memo[count + array_len] + 1, i + 1
                res = i - memo[count + array_len]
        return array[begin:end]


    def findLongestSubarray3(self, array):
        l, r, t, d = 0, 0, 0, {}
        for i, c in enumerate(array):
            if t not in d:
                d[t] = i
            if i - d[t] > r - l:
                l, r = d[t], i
            t += c.isdigit() or -1
        if t in d and len(array) - d[t] > r - l:
            l, r = d[t], len(array)
        return array[l: r]


    def findLongestSubarray4(self, array):
        # 初始化一个字典，用于记录前缀和及其第一次出现的下标
        guid = {0: -1}
        # 前缀和
        pre = 0
        # 最长数组长度
        res = 0
        # 最长数组开始坐标
        start = -1

        for i, v in enumerate(array):
            if v.isalpha():
                pre += 1
            else:
                pre -= 1

            if pre in guid:
                if i - guid[pre] > res:
                    res = i - guid[pre]
                    start = guid[pre]
            else:
                guid[pre] = i

        return array[start + 1:start + res + 1]


if __name__ == '__main__':
    obj = Solution()
    # array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    array = ['1', 'a']
    # array = ['a', 'a']
    # array = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]
    # array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    # array = ["C","u","49","29","o","68","k","r","E","26","24","W","F","w","13","53","C","H","V","s","13","S","l","z","U","a","50","25","f","E","7","25","o","50","e","R","36","93","77","47","M","36","84","46","82","w","L","46","54","58","73","85","18","D","m","c","46","j","U","i","P","49","49","i","N","P","h","40","o","54","47","24","7","H","100","92","6","10","66","74","47","35","O","41","Z","9","37","S","A","g","78","C","X","1","28","B","s","R","81","q"]

    print obj.findLongestSubarray4(array)