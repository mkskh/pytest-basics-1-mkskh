#!/usr/bin/env python


def squared(input: int) -> int:
    # Todo: add function to return the squre of the input int.
    if isinstance(input, int):
        return input ** 2
    else:
        raise TypeError


# print(callable(squared))  

if __name__ == "__main__":
    squared(100)
