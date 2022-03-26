'''
Medium 200 - Number of Islands
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # This problem is basically: find blocks of 1s
        def get_neighbors(sr, sc, dim):
            """
            Yield all adjacent neighbors given a starting coordinate

            Inputs:
                sr (int): starting row of the grid cell
                sc (int): starting column of the grid cell
                dim (tuple): dimension of the grid (numr, numc)
            """
            numr, numc = dim
            neighbors = set()
            min_delta, max_delta, step = -1, 1, 2
            for i in range(min_delta, max_delta+1, step):
                row_combo = (sr, min(max(0, sc+i), numc-1))
                col_combo = (min(max(0, sr+i), numr-1), sc)
                if row_combo != (sr, sc):
                    yield row_combo
                if col_combo != (sr, sc):
                    yield col_combo

        visited = set()
        # Explore the first grid cell by default
        num_islands = 0
        dim = (len(grid), len(grid[0]))

        # Explore the whole grid
        for i in range(dim[0]):
            for j in range(dim[1]):
                coord, val = (i, j), grid[i][j]
                is_land = (val == '1')
                is_new_cell = (coord not in visited)
                # Look for new land
                if is_new_cell and is_land:
                    visited.add(coord)
                    exploring = [coord]

                    while exploring:
                        sr, sc = exploring.pop()
                        # Check if land is an island by itself
                        neighbors = set(get_neighbors(sr, sc, dim))
                        for (nr, nc) in neighbors:
                            if grid[nr][nc] != '0' and ((nr, nc) not in visited):
                                visited.add((nr, nc))
                                exploring.append((nr, nc))

                    num_islands += 1

        return num_islands
