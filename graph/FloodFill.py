'''
Easy 733 - Flood fill
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        Return a modified image after flood fill
        Inputs:
            Image (list): a nested list representing pixel values
            Sr (int): row of the source element
            Sc (int): column of the source element
            newColor (int): the new color to update 
        Outputs:
            newImage (list): a modified version of the original image
        Approach:
            BFS
            Have to traverse the graph
            Need to get neighbors
        """
        # Keep track of v tiles
        seen = set()

        # Initialize basic information about the image
        newImage = image[:][:]
        baseColor = image[sr][sc]
        rowDim, colDim = len(image)-1, len(image[0])-1

        # Keep a queue to track of the coloring process
        coloring_queue = [(sr, sc, baseColor)]

        while coloring_queue:
            current_tile = coloring_queue.pop()
            currentRow, currentCol, color = current_tile
            # Check if current tile has same color as parent
            if color == baseColor:
                # Replace current tile color with new color
                newImage[currentRow][currentCol] = newColor
            neighbors = list(
                find(current_tile, image, rowDim, colDim, baseColor))
            print(neighbors)
            for neighbor in neighbors:
                # Explore new tiles
                if neighbor not in seen:
                    coloring_queue.append(neighbor)
                    # Mark tile as visited
                    seen.add(neighbor)
        return newImage


def find(tile, image, rowDim, colDim, baseColor):
    """
    Return a list of neighbors from the curren tile
    Inputs:
        tile (tuple): (row, column, color)
        image (list): a nested list representing pixel values
        rowDim (int): number of rows
        colDim (int): number of column
    Outputs:
    """
    # Get current dimension
    row, col, color = tile
    # Neighbors are 1 in difference of row or column number
    for i in range(-1, 2, 2):
        newRow, newCol = max(min(row+i, rowDim), 0), max(min(col+i, colDim), 0)
        if (newRow != row) or (newCol != col):
            if image[newRow][col] == baseColor:
                yield (newRow, col, image[newRow][col])
            if image[row][newCol] == baseColor:
                yield (row, newCol, image[row][newCol])
