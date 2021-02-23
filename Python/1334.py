import collections, heapq

class Solution:
    # Dijkstra
    def findTheCity_dijkstra(self, n, edges, distanceThreshold):
        '''
        :type: n: int
        :type: edges: List[List[int]]
        :type: distanceThreshold: int
        :rtype: int
        '''
        g = collections.defaultdict(dict)
        for fr, to, w in edges:
            g[fr][to] = w
            g[to][fr] = w
        sssps = []
        for i in range(n):
            sssps.append(self.dijkstra(i, edges, g, n))
        min_available_city_num = float('inf')
        min_available_city_idx = 0
        for i, sssp in enumerate(sssps):
            count = 0
            for node, d in sssp.items():
                if node != i and d <= distanceThreshold:
                    count += 1
            if count < min_available_city_num:
                min_available_city_num = count
                min_available_city_idx = i
            elif count == min_available_city_num:
                if i > min_available_city_idx:
                    min_available_city_idx = i
                
        return min_available_city_idx
        
    def dijkstra(self, start_node, edges, g, n):
        heap = [(0, start_node)] # (dis, node)
        all_d = {}
        while heap and len(all_d) < n:
            d, node = heapq.heappop(heap)
            if node not in all_d:
                all_d[node] = d
                for nb_node, nb_d in g[node].items():
                    heapq.heappush(heap, (d + nb_d, nb_node))
        return all_d

    # Floyd–Warshall
    def findTheCity_floyd(self, n, edges, distanceThreshold):
        '''
        :type: n: int
        :type: edges: List[List[int]]
        :type: distanceThreshold: int
        :rtype: int
        '''
        mem_table = [[float('inf')] * n for i in range(n)]
        for fr, to, w in edges:
            mem_table[fr][to] = w
            mem_table[to][fr] = w
        for i in range(n):
            mem_table[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mem_table[i][j] = min(mem_table[i][j], mem_table[i][k] + mem_table[k][j]) 
    
        min_available_city_num, min_available_city_idx = float('inf'), 0
        for i, mem in enumerate(mem_table):
            s = sum(m <= distanceThreshold for m in mem) - 1
            if min_available_city_num > s:
                min_available_city_num = s
                min_available_city_idx = i
            elif min_available_city_num == s and min_available_city_idx < i:
                min_available_city_idx = i
            
        return min_available_city_idx