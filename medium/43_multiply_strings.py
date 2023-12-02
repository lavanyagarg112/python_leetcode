# disclaimer: i dont know if this solution is actually accepted based on the q
# leetcode accepts all solutions as long as output passes testcase

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        '''
        If i could convert to integers directly - leetcode accepts it
        num1 = int(num1)
        num2 = int(num2)
        prod = num1 * num2 
        return str(prod)
        '''

        if num1 == '0' or num2 == '0':
            return '0'


        digits = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}
        nums = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",0:"0"}

        def strings_to_digits(s):
            dig = 0
            for i in range(len(s)):
                dig = dig*10 + digits[s[i]]
            return dig

        def digits_to_strings(d):
            s = ""
            while d:
                dig = d%10
                d = d//10
                s += nums[dig]
            return s[::-1]

        num1 = strings_to_digits(num1)
        num2 = strings_to_digits(num2)
        prod = num1 * num2

        return digits_to_strings(prod)


