# coding=utf-8
class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        设n=p*K+q
        则n*10+1=10*p*K+q*10+1;
        有n%K=q
        有(n*10+1)%K=(10*p*K+q*10+1)%K=(q*10+1)%K
        又((n%K)*10+1)%K=(q*10+1)%K
        推断出：(n*10+1)%K = ((n%K)*10+1)%K

        :type K: int  1 <= K <= 10^5
        :rtype: int
        """
        if K % 2 == 0 or K %5 == 0:
            return -1
        i = 1
        l = 1
        while(i%K!=0):
            i = i % K
            i = 10*i +1
            l = l+1
        return l


if __name__ == '__main__':
    obj = Solution()
    print obj.smallestRepunitDivByK(K=19)