class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        score = 0
        while tokens:
            if P >= min(tokens):
                P = P - min(tokens)
                score += 1
                tokens.remove(min(tokens))
            elif score > 0 and P<min(tokens):
                if len(tokens) == 1:
                    break
                P = P + max(tokens)
                score -= 1
                tokens.remove(max(tokens))
            else:
                break
        return score



if __name__ == '__main__':
    tokens = [100]
    P = 50
    obj = Solution()
    print obj.bagOfTokensScore(tokens=tokens, P=P)