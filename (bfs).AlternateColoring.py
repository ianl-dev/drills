"""
Given a graph (dictionary), decide if you can color it with only 2 colors
Such that each node is alternating in color

If possible, return any valid coloring mapping
Else if not possible, return {}

Graph is given as:
# Can color with 2 colors
{'A': ['B'], 'B': ['A', 'C'],
'C':['B', 'D'], 'D': ['C', 'E', 'F'],
'E': ['D'], 'F': ['D', 'G', 'H', 'I'], 'G': ['F'], 'H': ['F'],
'I': ['F']}

# CANNOT color with 2 colors
{'A': ['B'], 'B': ['A', 'C'],
'C':['B', 'D'], 'D': ['C', 'E', 'F'],
'E': ['D'], 'F': ['D', 'G', 'H', 'I'], 'G': ['F', 'H'], 'H': ['F', 'G'],
'I': ['F']}

adjancency list = neighbors of the node

Define a function (graph, start)
"""
def alternating_colors(graph, start):
    """
    My approach: develop a closure so that we can keep track of 
    the current mapping

    Since red and blue are symmetric, doesn't matter which color we start with
    """
    # Closure so that we can recurse more easily
    coloring = {}

    def color_node(node, color):
        if node in coloring:
            # A node has been colored before and now we try to overwrite it -> cannot do it with 2 colors
            return False
        
        coloring[node] = color

        other_color = 'blue' if color == 'red' else 'red'

        # Color each neighbor immediate to this node
        for neighbor in graph[node]:
            if neighbor in coloring and coloring[neighbor] == other_color:
                continue
            # Color it with the opposite color
            is_two_color = color_node(neighbor, other_color)
            if not is_two_color:
                return False
            # Result is false, then return false
            # Update mapping
            coloring[neighbor] = other_color
        
        return True

    return coloring if color_node(start, 'red') else {}

# TEST
case = {'A': ['B'], 'B': ['A', 'C'],
'C':['B', 'D'], 'D': ['C', 'E', 'F'],
'E': ['D'], 'F': ['D', 'G', 'H', 'I'], 'G': ['F'], 'H': ['F'],
'I': ['F']}

case2 = {'A': ['B'], 'B': ['A', 'C'],
'C':['B', 'D'], 'D': ['C', 'E', 'F'],
'E': ['D'], 'F': ['D', 'G', 'H', 'I'], 'G': ['F', 'H'], 'H': ['F', 'G'],
'I': ['F']}

print(alternating_colors(case, 'A'))