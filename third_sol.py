def isPossible(n,k):
    if ((k*k) <= n and (n + k) % 2 == 0):
        print('Yes')
    else:
        print("NO")


if __name__=='__main__':

    t=int(input())
    for i in range(t):
        print('enter n and k value followed by space')
        t-=1
        n,k=map(int,input().split())
        isPossible(n,k)


'''
Dry run input output data is taken from Internet.
For Dry Run Purpose we can use these input and check our code output.
input
6
3 1
4 2
10 3
10 2
16 4
16 5
output
YES
YES
NO
YES
YES
NO
Note
'''