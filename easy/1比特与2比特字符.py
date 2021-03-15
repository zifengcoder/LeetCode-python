# coding=utf-8
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int] 100
        :rtype: bool
        """
        stack = []
        stack_2 = []
        for i in bits:
            if stack and stack[-1] == 1:
                stack_2.append(str(1) + str(i))
                stack = []
            else:
                if i == 0:
                    stack_2.append(str(0))
                stack.append(i)
        if stack_2[-1] == '0':
            return True
        else:
            return False

    def is_one_bit_character(self, strings):
        i = 0
        while i < len(strings):
            # 当前位置为0，且已经是最后一个元素，直接返回True
            if strings[i] == 0 and i == len(strings) - 1:
                return True
            if strings[i] == 1:  # 当前位置为1，则说明肯定是2比特的开头
                i += 2
                continue
            i += 1  # 当前位置为0（一比特），则从下一个位置开始计算
        return False  # 所有的元素都遍历完还没返回，说明最后一个字符肯定是2比特**


    def demo(self, bits):
        for inx, i in enumerate(bits):
            if i:
                bits[inx] = bits[inx + 1] = None
        return bits[-1] == 0



if __name__ == '__main__':
    obj = Solution()
    bits = [1,1,1,1,0]
    print obj.demo(bits)