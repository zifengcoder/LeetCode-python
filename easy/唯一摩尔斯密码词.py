class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        temp = {}
        for i in range(97,123):
            temp[chr(i)] = mos[i-97]
        mos_list = set()
        for item in words:
            mos_str = ''
            for i in item:
                mos_str += temp[i]
            mos_list.add(mos_str)
        return len(mos_list)