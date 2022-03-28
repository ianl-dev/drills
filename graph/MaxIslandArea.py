"""
Medium 695 - Max Area of Island
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_neighbors(sr, sc):
            """
            Yield 4-directionally connected neighbors

            Input:
                sr (int): starting cell row index
                sc (int): startinc cell column index
                dim (tuple): height, width of the grid in (num_rows, num_cols) format  

            """
            current = grid[sr][sc]
            current_coord = (sr, sc)
            max_row, max_col = num_rows-1, num_cols-1

            min_delta, max_delta, step = -1, 1, 2
            for i in range(min_delta, max_delta+1, step):
                r_combo, c_combo = (max(0, min(sr+i, max_row)),
                                    sc), (sr, max(0, min(sc+i, max_col)))
                # Looking for land neighbors
                if (grid[r_combo[0]][r_combo[1]] == 1 and r_combo != current_coord):
                    yield r_combo
                if (grid[c_combo[0]][c_combo[1]] == 1 and c_combo != current_coord):
                    yield c_combo

        # Compare explored island area
        max_area = 0
        seen = set()
        num_rows, num_cols = len(grid), len(grid[0])

        for i in range(num_rows):
            for j in range(num_cols):
                # Explore each land that is island
                is_island, is_new_land = (
                    grid[i][j] == 1), not ((i, j) in seen)
                if (is_island and is_new_land):
                    land_area = 0
                    start = (i, j)
                    exploring = [start]
                    while exploring:
                        land_area += 1
                        current = exploring.pop()

                        # Importantly, we have visited the current spot, so mark it as seen
                        seen.add(current)

                        current_row, current_col = current
                        neighbors = get_neighbors(current_row, current_col)

                        # Go through each land connected to this island
                        for neighbor in neighbors:
                            if neighbor not in seen:
                                # Exploring the entirety of the island which contains this current land
                                seen.add(neighbor)
                                exploring.append(neighbor)
                    # Update max area until all islands are explored
                    max_area = max(max_area, land_area)
        return max_area
