class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """


        count = 0

        for i in words:
            charslst = list(chars)
            for j in i:
                if j in charslst:
                    charslst.remove(j)
                else:
                    break
            else:
                count += len(i)

        return count
        