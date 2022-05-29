"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints
"""

arr= [
[1,2,3],
[4,5,6],
[9,8,3]
]

def diagonalDifference(array):
#Validate it is a square matrix
    matrixRows=len(array)
    matrixCol=[]
    leftDiagonal=0
    rightDiagonal=0
    for col in array:
        matrixCol.append(len(col))
    if  matrixCol.count(matrixRows)==len(matrixCol):
#Diagonal difference logic
        for i in range(len(array)):
           leftDiagonal+=array[i][i]
           rightDiagonal+=array[i][-(i+1)]
    else:
        return("Please introduce a square matrix")
    
    return (abs(leftDiagonal - rightDiagonal)) 

print(diagonalDifference (arr))