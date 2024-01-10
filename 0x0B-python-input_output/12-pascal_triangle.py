#!/usr/bin/python3
"""Defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent size n Pascal's Triangle.

    Returns a list of lists of integers that represents the triangle.
    """
    if n <= 0:
        return []

    pasTriangles = [[1]]
    while len(pasTriangles) != n:
        Triangle = pasTriangles[-1]
        tempo = [1]
        for i in range(len(Triangle) - 1):
            tempo.append(Triangle[i] + Triangle[i + 1])
        tempo.append(1)
        pasTriangles.append(tempo)
    return pasTriangles
