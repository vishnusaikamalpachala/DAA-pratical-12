ties = ["A", "B", "C", "D"]

dist = [
    #  A   B   C   D
    [0, 10, 15, 20],   # A
    [10, 0, 35, 25],   # B
    [15, 35, 0, 30],   # C
    [20, 25, 30, 0],   # D
]


def route_cost(route):
    """Total distance of a route that returns to the starting city."""
    total = 0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]
    total += dist[route[-1]][route[0]]  # go back home
    return total


def route_name(route):
    return " -> ".join(cities[i] for i in route) + " -> " + cities[route[0]]
