#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's Triangle of size n."""
    if n <= 0:
        return []
    
    # Create the triangle starting with the first row [1]
    triangle = [[1]]
    
    # Generate the rows from 1 to n-1
    for i in range(1, n):
        # Create new row with 1 at the start
        row = [1]
        # Use list comprehension to compute the values in between
        row.extend([triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)])
        # End the row with 1
        row.append(1)
        # Append the new row to the triangle
        triangle.append(row)
    
    return triangle
