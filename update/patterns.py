#!/usr/bin/env python3

LIVING = 1
DEAD = 0


def make_arrow():
    seed = [DEAD]*5
    seed = [seed[:] for c in range(7)]
    for i in [0,6]:
        seed[i][4] = LIVING
    for i in [1,5]:
        seed[i][2], seed[i][4] = (LIVING, LIVING)
    for i in range(2,5):
        seed[i][0], seed[i][1] = (LIVING, LIVING)
    return seed


PATTERNS = {"block": [[LIVING, LIVING],
                      [LIVING, LIVING]],
            "anti-sym": [[DEAD, LIVING],
                         [LIVING, LIVING]],
            "glider": [[LIVING, DEAD, LIVING],
                       [DEAD, LIVING, LIVING],
                       [DEAD, LIVING, DEAD]],
            "toad": [[DEAD, LIVING, LIVING, LIVING],
                     [LIVING, LIVING, LIVING, DEAD]],
            "blinker": [[DEAD, DEAD, DEAD],
                        [LIVING, LIVING, LIVING],
                        [DEAD, DEAD, DEAD]],
            "beacon": [[LIVING, LIVING, DEAD, DEAD],
                       [LIVING, DEAD, DEAD, DEAD],
                       [DEAD, DEAD, DEAD, LIVING],
                       [DEAD, DEAD, LIVING, LIVING]],
            "arrow": make_arrow()}

if __name__ == "__main__":
    pass
