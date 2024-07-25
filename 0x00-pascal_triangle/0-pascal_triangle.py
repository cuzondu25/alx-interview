#!/usr/bin/python3
""" compute  pascal triangle"""

def pascal_triangle(n):
    """ A function to compute the value of pascal triangle up to nth row
    params:
        n (int): number of rows to compute
    return: a list of lists of pascal triangle rows
    """

    if n <= 0:
        return []
    elif n == 1:
        mylist = [[1,],]
        return mylist
    x = 1
    mylist = [[1,], [1, 1]]
    while x < n-1:
        row_list = [1]
        a = 0
        while a < len(mylist) - 1:
            b = mylist[x][a] + mylist[x][a+1]
            row_list.append(b)
            a += 1
        row_list.append(1)
        mylist.append(row_list)
        x += 1
    return mylist
