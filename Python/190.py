class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        : type: n: int
        : rtype: int
        '''
        bit_str = ''
        while n > 0: # generate n to bits
            bit_str += str(n % 2)
            n = n // 2
        bit_str = bit_str[::-1].zfill(32) # reverse bits and pad to 32-bits => original bits
        result, power = 0, 0
        for i in bit_str:
            if i == '1':
                result = result + 2 ** power
            power += 1
        return result 