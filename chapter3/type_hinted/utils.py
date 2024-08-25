from typing import Any, Tuple
from numbers import Number
from collections import deque

type State = Any
type Node = Tuple[State, "Node", str, Number, int]

# a node = a tuple of 5 members
def create_node(state, parent, action, path_cost, depth) -> Node:
    return (state, parent, action, path_cost, depth)

# Trace back from a goal node, n, to the initial node
# to generate a solution
def print_solution(n: Node) -> None:
    r = deque() # double-end queue
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for s in r:
        print(s)
