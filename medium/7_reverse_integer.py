class Solution(object):
    def reverse(self, x):
        
        left = x
        output = 0
        multi = 1
        if x < 0:
            left = -1 * x
            multi = -1

        while left!=0:
            right = left % 10
            left = left//10
            output = 10*output + right

        if output > pow(2, 31):
            return 0
        else :
            return multi * output

        