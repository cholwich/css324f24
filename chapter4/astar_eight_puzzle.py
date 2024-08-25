import eight_puzzle
from informed import a_star_graph_search
from utils import print_solution


def h1(s):
    board, _, _ = s
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    h_value = 0
    for idx in range(8):
        if goal[idx] != board[idx]:
            h_value += 1
    return h_value


print(h1(eight_puzzle.initial_state()))


goal_node, n_visits = a_star_graph_search(eight_puzzle, h1)
if goal_node is not None:
    print("Solution")
    print_solution(goal_node)
    print(f"Cost = {goal_node[3]}")
    print(f"n_visits = {n_visits}")
else:
    print("No solution")
