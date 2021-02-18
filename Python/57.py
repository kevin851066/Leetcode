class Solution:
    def insert(self, intervals, newInterval):
        '''
        :type: intervals: List[List[int]]
        :type: newInterval: List[int]
        :rtype: List[List[int]]
        '''
        res = []
        i = 0
        while i < len(intervals):
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
        intervals.insert(i, newInterval)
        
        for i in range(len(intervals)-1):
            s1, e1 = intervals[i]
            s2, e2 = intervals[i+1]  
            if e1 >= s2:
                intervals[i+1] = [s1, max(e1, e2)]
            else:
                res.append(intervals[i])
        res.append(intervals[-1])
        return res