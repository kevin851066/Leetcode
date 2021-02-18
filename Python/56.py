from operator import itemgetter

class Solution:
    def merge(self, intervals):
        '''
        :type: intervals: List[List[int]]
        :rtype: List[List[int]]
        '''
        intervals = sorted(intervals, key=itemgetter(0))
        res = []
        for i in range(len(intervals)-1):
            s1, e1 = intervals[i]
            s2, e2 = intervals[i+1]
            if e1 >= s2:
                intervals[i+1] = [s1, max(e1, e2)]
            else:
                res.append(intervals[i])
        res.append(intervals[-1])
        return res