class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        '''
        type: releaseTimes: List[int]
        type: keysPressed: str
        rtype: str
        '''
        t, k = releaseTimes[0], keysPressed[0] 
        for i in range(len(releaseTimes) - 1):
            time = releaseTimes[i+1] - releaseTimes[i]
            if time > t:
                t = time
                k = keysPressed[i+1]
            elif time == t:
                t = time
                if keysPressed[i+1] > k:
                    k = keysPressed[i+1]
        return k