"""
Given a list of points, construct a graph that includes all of those points and the position (0, 0).
Points will be dictionaries like so: {"x": 1, "y": -1}.
A graph should be represented as a 2d array.
"""

def construct_graph(p):
    points = [(0, 0), *[(d['x'], d['y']) for d in p]]
    
    min_x, min_y = map(min, zip(*points))
    max_x, max_y = map(max, zip(*points))
    points.pop(0)
    
    graph = [[' ']*(max_x - min_x + 1) for _ in range(min_y, max_y + 1)]
    graph[max_y] = ['-']*len(graph[0])
    for i in range(len(graph)): graph[i][abs(min_x)] = '|'
    graph[max_y][abs(min_x)] = '+'
    
    for x, y in points:
        graph[max_y - y][x - min_x] = '*'
    
    return graph