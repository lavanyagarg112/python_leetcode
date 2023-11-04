class Solution(object):
    def strStr(self, haystack, needle):

        if needle in haystack:

            for i in range(len(haystack)):

                if haystack[i] == needle[0]:

                    if len(haystack[i:]) >= len(needle):

                        for j in range(1,len(needle)):

                            if haystack[i+j] != needle[j]:
                                break
                                

                        else:

                            return i


        else:
            
            return -1

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        