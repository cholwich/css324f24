edges = [
    ["oradea", "zerind", 71], ["oradea", "sibiu", 151], 
    ["zerind", "arad", 75], ["arad", "timisoara", 118], 
    ["arad", "sibiu", 140], ["timisoara", "lugoj", 111],
    ["lugoj", "mehadia", 70], ["mehadia", "dobreta", 75], 
    ["dobreta", "craiova", 120], ["craiova", "rimnicu vilcea", 146], 
    ["craiova", "pitesti", 138], ["pitesti", "rimnicu vilcea", 97],
    ["pitesti", "bucharest", 101], ["rimnicu vilcea", "sibiu", 80], 
    ["sibiu", "fagaras", 99], ["fagaras", "bucharest", 211], 
    ["bucharest", "giurgiu", 90], ["bucharest", "urziceni", 85],
    ["urziceni", "hirsova", 98], ["urziceni", "vaslui", 142], 
    ["hirsova", "eforie", 86], ["vaslui", "lasi", 92], 
    ["lasi", "neamt", 87]
]

def initial_state():
    return ("arad", "bucharest")

def is_goal(s):
    city1, city2 = s
    return city1 == city2

def neighbors(c):
    n = list()
    for e in edges:
        if e[0] == c:
            n.append((e[1], e[2]))
        elif e[1] == c:
            n.append((e[0], e[2]))
    return n

def successors(s):
    city1, city2 = s
    n1 = neighbors(city1)
    n2 = neighbors(city2)
    prod = [(x, y) for x in n1 for y in n2]
    for p in prod:                              # p = ((cityX, dX), (cityY, dY))
        step_cost = max(p[0][1], p[1][1])
        yield ((p[0][0], p[1][0]), step_cost)

if __name__ == "__main__":
    for succ, cost in successors(initial_state()):
        print(f"{succ}\t{cost}")


