"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
# Time Complexity: O(n)
# Space Complexity: O(n)
from collections import deque


class Solution(object):
    result = 0

    #     BFS approach
    def Bfs(self, employees, id):
        #         initialize queue
        result = 0
        q = deque()

        # c = id - 1
        #         create map and add id to employee mapping
        hmap = {}

        for e in employees:
            hmap[e.id] = e

        #         Append the current id employee in queue
        q.append(hmap[id])

        #       Until queue is empty
        while q:
            #         we will op the first element
            emp = q.popleft()
            #             add the result of curren temp to result
            result += emp.importance
            #     iterate over the subordinates and add it to the queue
            for i in emp.subordinates:
                q.append(hmap[i])

        return result

    #     DFS approach
    def Dfs(self, id, hmap):
        #         take the emp from hashmap and add current emp importance to the result
        emp = hmap[id]
        self.result += emp.importance
        #       Iterate over the emp subordinates and recursively call the DFS on the sub ordinates
        for i in emp.subordinates:
            self.Dfs(i, hmap)

    def DfsMain(self, employees, id):
        hmap = {}

        for e in employees:
            hmap[e.id] = e

        self.Dfs(id, hmap)
        return self.result

    def getImportance(self, employees, id):
        return self.Bfs(employees, id)

        return self.DfsMain(employees, id)

        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
