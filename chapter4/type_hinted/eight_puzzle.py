from typing import Tuple, List, Iterable
from numbers import Number
import copy

type State = Tuple[Tuple, int, int]
type StepCost = Number

def initial_state() -> State:
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)

def is_goal(s: State) -> bool:
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)

def successors(s: State) -> Iterable[Tuple[State, StepCost]]:
    _, r, c = s
    for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if is_valid(new_r, new_c):
            yield move_blank(s, new_r, new_c), 1

def is_valid(r: int, c: int) -> bool:
    return 0 <= r <= 2 and 0 <= c <= 2

def to_index(r: int, c: int) -> int:
    return r*3 + c

def move_blank(s: State, new_r: int, new_c: int) -> State:
    board, r, c = s
    new_board = list(copy.deepcopy(board))
    new_board[to_index(r, c)] = new_board[to_index(new_r, new_c)]
    new_board[to_index(new_r, new_c)] = 0
    return (tuple(new_board), new_r, new_c)
