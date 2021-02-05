class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        '''
        type: flowerbed: List[int]
        type: n: int
        rtype: bool
        '''
        if n == 0:
            return True
        pad_flowerbed = [0] + flowerbed + [0]
        c = 0
        for i in range(1, len(pad_flowerbed)-1):
            if pad_flowerbed[i] == 0 and pad_flowerbed[i-1] == 0 and pad_flowerbed[i+1] == 0:
                pad_flowerbed[i] = 1
                c += 1
            if c == n:
                return True
        return False