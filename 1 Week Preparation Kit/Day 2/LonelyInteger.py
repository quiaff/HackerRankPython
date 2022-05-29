"""

Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, , the number of integers in the array.
The second line contains  space-separated integers that describe the values in .

"""

from numpy import number


h=[1,2,3,4,3,2,1]
def lonelyinteger(a):
    for lonlynumber in a:
        temporalArray=a.copy()
        temporalArray.remove(lonlynumber)
        if lonlynumber in temporalArray:
            continue
        else:
            return lonlynumber


print (lonelyinteger(h))





    