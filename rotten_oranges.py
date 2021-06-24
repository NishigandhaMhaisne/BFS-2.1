# Time Complexity: O(mxn)
# Space Complexity: O(mxn)
from collections import deque


class Solution(object):

    def orangesRotting(self, grid):
        # initialize the queue
        q = deque()
        #         get the row and column in variable
        m = len(grid)
        n = len(grid[0])
        # Maintain fresh oranges count and timestamp
        fresh = 0
        timeStamp = 0
        #  Iterate over the grid and add all rotten oranges to the queue and update the fresh orange count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        #         if the grid has empty cells return 0
        if fresh == 0 and len(q) == 0:
            return 0
        # Iterate over queue and we will need the size of the queue here as
        # we will be updating timestamp after every level
        while q:
            leng = len(q)
            for i in range(leng):
                #                 get row and column of the pop element
                r, c = q.popleft()
                #   Here children of current element will be its 4 direction elements
                direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                # we will iterate over the 4 directions and update the row
                # and col value accordingly and check if it is fresh orange
                # then mak eit rotten and add it to the queue and update fresh count
                for d in direc:
                    row = r + d[0]
                    col = c + d[1]

                    if m > row >= 0 and n > col >= 0 and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
                    # print(fresh)
            #             we will be updating timestamp after each level
            timeStamp += 1

        #         if after all levels still fresh count is not 0 then we will return -1
        if fresh != 0:
            return -1
        # or else we will return timestamp - 1 , because we are updating timestamp
        # after level is done i.e we are updating timestamp one extra
        return timeStamp - 1;

        """
        :type grid: List[List[int]]
        :rtype: int
        """
