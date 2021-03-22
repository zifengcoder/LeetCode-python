class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","").replace("+"," + ").replace("-"," -").replace("*"," * ").replace("/"," / ").split()
        for i in range(len(s)):
            num = s[i]
            if num == "+":
                s[i] = 0
            elif num == "*":
                s[i+1] = int(s[i-1]) * int(s[i+1])
                s[i-1],s[i] = 0,0
            elif num == "/":
                if '-' in str(s[i-1]) and int(s[i-1] % int(s[i+1])) != 0:
                    s[i+1] = int(s[i-1] / int(s[i+1])) + 1
                else:
                    s[i+1] = int(s[i - 1] / int(s[i + 1]))
                s[i - 1], s[i] = 0, 0
            else:
                s[i] = int(num)
        return sum(s)




if __name__ == '__main__':
    obj = Solution()
    s = "0/1"
    print obj.calculate(s)
