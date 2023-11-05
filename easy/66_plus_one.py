class Solution(object):
    def plusOne(self, digits):
        output = [0] + list(digits)
        carry = 1
        for i in range(len(output)-1, -1, -1):

            if i != 0:
                result = digits[i-1] + carry
            else:
                output[i] = carry
                break

            if result > 9:
                output[i] = result % 10
                carry = result//10
            else:
                output[i] = result                   
                break

        if i == 0:
            return output
        else:
            return output[1:]
                    

        