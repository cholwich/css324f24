from typing import Any, Tuple, List, Set, Callable
from types import ModuleType
from numbers import Number
from heapq import heappop, heappush, heapify
from utils import create_node

type State = Any
type Node = Tuple[State, "Node", str, float, int]
type PathCost = Number

# Search for a state in the frontier
# if found, return the index of the state
# otherwise, return -1
def index(f: List[Tuple[Number, Node]], s: State) -> int:
    return next((i for i, x in enumerate(f) if x[1][0] == s), -1)


def greedy_best_first_graph_search(problem: ModuleType, h: Callable[[State], Number]) -> Tuple[Node, int]:
    initial_state = problem.initial_state()
    initial_node = create_node(initial_state, None, "", 0, 0)
    # use the heuristic value as the key of the minheap
    frontier: List[Tuple[Number, Node]] = [(h(initial_state), initial_node)]
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
                    child = create_node(succ, node, "", \
                        child_cost, depth + 1)
                    new_h = h(succ)
                    if succ not in explored:
                        idx = index(frontier, succ)
                        if idx < 0:
                            heappush(frontier, (new_h, child))
                        else:
                            existing_h, existing = frontier[idx]
                            # compare the existing and the new
                            # heuristic values of the same state
                            if existing_h > new_h:
                                frontier[idx] = (new_h, child)
                                heapify(frontier)


def a_star_graph_search(problem: ModuleType, h: Callable[[State], Number]) -> Tuple[Node, int]:
    initial_state = problem.initial_state()
    initial_node = create_node(initial_state, None, "", 0, 0)
    # use f(n) = g(n) + h(n) as the key of the minheap
    frontier: List[Tuple[Number, Node]] = [(0 + h(initial_state), initial_node)]
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
                    child = create_node(succ, node, "", \
                        child_cost, depth + 1)
                    h_value = h(succ)
                    if succ not in explored:
                        idx = index(frontier, succ)
                        f_value = child_cost + h_value
                        if idx < 0:
                            heappush(frontier, (f_value, child))
                        else:
                            existing_f, existing = frontier[idx]
                            if existing_f > f_value:
                                frontier[idx] = (f_value, child)
                                heapify(frontier)
