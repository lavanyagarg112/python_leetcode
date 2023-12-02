class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split(' ')
        dup = list(words)
        for i in dup:
            if i == '':
                words.remove(i)
        return len(words[-1])
        