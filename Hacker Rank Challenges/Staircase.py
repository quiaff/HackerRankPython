def staircase(n):
    for i in range (1,n+1):

        hashnumber="#"*i
        spacesnumber=" "*(n-i)
        print(spacesnumber+hashnumber)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
