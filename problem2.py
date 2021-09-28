'''

0 --- 1 ---- 2
  \   |  /   |
    \ 3/     4

# number of roads for each city
cities = {}

# then identify top two cities, calculate the roads

'''
from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n, roads):
        number_of_roads = 0
        cities = defaultdict(int)

        for road in roads:
            cities[road[0]] += 1
            cities[road[1]] += 1
        print(cities)
        print(cities.items())
        
        # top cities
        top_city, top_city_roads = -1, -1
        runner_up, runner_up_roads = -1, -1
        #for city in cities:
            
            
        
        
        

s = Solution()
s.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]])