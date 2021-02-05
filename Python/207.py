class Solution:
    def canFinish(self, numCourses, prerequisites:
        '''
        type: numCourses: int
        type: prerequisites: List[List[int]]
        rtype: bool
        '''
        indegree = [0] * numCourses
        G = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            indegree[a] += 1
            G[b].append(a)
        b = [i for i in range(len(indegree)) if indegree[i] == 0]
        for i in b:
            for j in G[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    b.append(j)
        return len(b) == numCourses