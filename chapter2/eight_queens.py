from typing import Tuple, List, Iterable
from numbers import Number

type State = List
type StepCost = Number

def initial_state() -> State:
    return []

def is_goal(s: State) -> bool:
    return len(s) == 8

def successors(s: State) -> Iterable[Tuple[State, StepCost]]:
    for new_r in range(1, 9):
        if placable(s, new_r):
            t = s[:]
            t.append(new_r)
            yield t, 1

def attack(r1: int, c1: int, r2: int, c2: int) -> bool:
    return r1 == r2 or c1 == c2 or abs(c1-c2) == abs(r1-r2)

def placable(s: State, new_r: int) -> bool:
    new_c = len(s)
    for c in range(len(s)):
        r = s[c]
        if attack(r, c, new_r, new_c):
            return False
    return True
