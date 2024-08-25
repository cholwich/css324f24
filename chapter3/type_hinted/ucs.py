from typing import Any, Tuple, List, Set
from types import ModuleType
from numbers import Number
from heapq import heappush, heappop, heapify
from utils import create_node

type State = Any
type Node = Tuple[State, "Node", str, float, int]
type PathCost = Number

def uniform_cost_tree_search(problem: ModuleType) -> Tuple[Node, int]:
    initial_node = create_node(problem.initial_state(), None, "", 0, 0)
    frontier: List[Tuple[PathCost, Node]] = [(0, initial_node)]
    n_visits = 0
    while True:
        if not frontier:
            return (None, n_visits)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, _, _, path_cost, depth = node
            if problem.is_goal(state):
                return (node, n_visits)
            else:
                for succ, cost in problem.successors(state):
                    child_cost = path_cost + cost
                    child = create_node(succ, node, "", child_cost, depth + 1)
                    heappush(frontier, (child_cost, child))


# Search for a state in the frontier
# if found, return the index of the state
# otherwise, return -1
def index(f: List[Tuple[Number, Node]], s: State) -> int:
    return next((i for i, x in enumerate(f) if x[1][0] == s), -1)


def uniform_cost_graph_search(problem: ModuleType) -> Tuple[Node, int]:
    initial_node = create_node(problem.initial_state(), None, "", 0, 0)
    frontier: List[Tuple[PathCost, Node]] = [(0, initial_node)]
    explored: Set[State] = set()
    n_visits = 0
    while True:
        if not frontier:
            return (None, n_visits)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, _, _, path_cost, depth = node
            explored.add(state)
            if problem.is_goal(state):
                return (node, n_visits)
            else:
                for succ, cost in problem.successors(state):
                    child_cost = path_cost + cost
                    child = create_node(succ, node, "", child_cost, depth + 1)
                    if succ not in explored:
                        idx = index(frontier, succ)
                        if idx < 0:
                            heappush(frontier, (child_cost, child))
                        else:
                            _, existing = frontier[idx]
                            if existing[3] > child_cost:
                                frontier[idx] = (child_cost, child)
                                heapify(frontier)
