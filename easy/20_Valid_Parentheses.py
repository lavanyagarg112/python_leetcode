class Solution(object):
    def isValid(self, s):

        store = []

        for i in range(len(s)):
            if s[i] in "([{":
                store.append(s[i])

            elif len(store) != 0:
                if s[i] == ")":
                    if "(" == store[-1]:
                        store = store[:-1]
                    else:
                        return False

                elif s[i] == "]":
                    if "[" == store[-1]:
                        store = store[:-1]
                    else:
                        return False

                elif s[i] == "}":
                    if "{" == store[-1]:
                        store = store[:-1]
                    else:
                        return False
            else:
                return False

        
        if len(store)!= 0:
            return False
        else:
            return True

            

        """
        :type s: str
        :rtype: bool
        """
        