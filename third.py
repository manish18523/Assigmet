for i in range(int(input())):
    n, k = map(int, input().split())
    print('YES' if k * k <= n and n % 2 == k % 2 else 'NO')


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