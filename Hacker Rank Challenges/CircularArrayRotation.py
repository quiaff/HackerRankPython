"""
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.

Example
a=[3,4,5]
k=2
queries=[1,2]


Here k  is the number of rotations on a , and queries  holds the list of indices to report. First we perform the two rotations: [3,4,5]----> [5,3,4]--->[4,5,3]

Now return the values from the zero-based indices 1 and 2 as indicated in the queries array.

a[1]=5
a[2]=3

Function Description

Complete the circularArrayRotation function in the editor below.

circularArrayRotation has the following parameter(s):

int a[n]: the array to rotate
int k: the rotation count
int queries[1]: the indices to report
Returns

int[q]: the values in the rotated  as requested in 
Input Format

The first line contains  space-separated integers, , , and , the number of elements in the integer array, the rotation count and the number of queries.
The second line contains  space-separated integers, where each integer  describes array element  (where ).
Each of the  subsequent lines contains a single integer, , an index of an element in  to return.

Constraints

Sample Input 0

3 2 3
1 2 3
0
1
2
Sample Output 0

2
3
1
  c=list(a)
    for i in range (k):
    
        last_element = c.pop()
        c=c.insert(0,last_element)

"""

# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries

from typing import final


def circularArrayRotation(a, k,q):
    final_array=[]   
    for i in range (k):
        last_element=a.pop()
        a.insert(0,last_element)
    for i in q:
        final_array.append (a[i])l
    return final_array

print (circularArrayRotation([1,2,3],2,[1,2]))



