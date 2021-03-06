'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n.

Constraints
1<=n<=100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.
'''

n=int(input())

if n>=1 and n<=100:
    if n%2==0 and (n in range(2,6) or n>20):
        print("Not Weird")
            
    elif n%2==0 and n in range(6,21):
            print("Weird")
            
    else:
        print("Weird")
        