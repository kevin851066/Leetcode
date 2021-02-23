import collections, heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        '''
        :type: times: List[List[int]]
        :type: n: int
        :type: k: int
        :rtype: int
        '''
        g, heap = collections.defaultdict(dict), [(0, k)]
        for u, v, w in times:
            g[u][v] = w
        all_t = {}
        while heap:
            t, node = heapq.heappop(heap)
            if node not in all_t: # avoid cyclic graph
                all_t[node] = t
                for nb_node, nb_t in g[node].items():
                    heapq.heappush(heap, (t + nb_t, nb_node))
        return max(all_t.values()) if len(all_t) == n else -1