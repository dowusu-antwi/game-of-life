#!/usr/bin/env python3

"""
This is a test, returns a generator
"""

def gen(n=1):
    yield n
    yield from gen(0 if n else 1)

if __name__ == "__main__":

    pass
