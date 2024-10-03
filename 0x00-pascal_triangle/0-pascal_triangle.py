#!/usr/bin/python3
"""
This script generates Pascal's Triangle up to n rows
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing the Pascal’s triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing the Pascal’s triangle.
    """
    if n <= 0:
        return []
    
    # Initialize the first row of the Pascal's triangle
    triangle = []

    # Iterate through each row index from 0 to n-1
    for i in range(n):
        row = [1] * (i + 1)  # Each row has i+1 elements
        # Update the values for the middle elements of the row
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle
