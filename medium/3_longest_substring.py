# longest substring without repeating characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        string = 0
        start = 0
        res = ""
        i = 0
        while i < len(s):

            if s[i] not in res:
                if (len(res) == 0):
                    start = i
                res = res + s[i]
                if i == len(s) - 1:
                    string = max(string, len(res))
                    return string
                else:
                    i = i + 1

            else:
                string = max(string, len(res))
                res = ""
                i = start + 1
        return string
        