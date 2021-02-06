class Solution:
    def findOrder(self, numCourses, prerequisites):
        '''
        type: numCourses: int
        type: prerequisites: List[List[int]]
        rtype: List[int]
        '''
        output = []
        indegree = [0] * numCourses
        g = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1
        bts = [i for i in range(len(indegree)) if indegree[i] == 0]  # idx
        for i in bts:
            output.append(i)
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    bts.append(j)
        if len(bts) != numCourses:
            return []
        else:
            return output