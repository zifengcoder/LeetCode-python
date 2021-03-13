class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        temp = {}
        for i in range(97,123):
            temp[chr(i)] = widths[i-97]
        str_leng = 0
        count = 1
        for i in s:
            str_leng += temp[i]
            if str_leng>100:
                str_leng = 0
                str_leng += temp[i]
                count += 1
        return [count, str_leng]