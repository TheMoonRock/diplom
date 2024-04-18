n = 0
h = 0
k = 0
count = 0

def PrintSpaces(count):
    for i in range(count):
        print(' ',end='')

def PrintLineOfDiamond(k, n):
    PrintSpaces(n+1-k)
    print('*',end='')
    if k > 1:
        PrintSpaces(2*k-3)
        print('*', end='')
    print()

while h <= 2 or h % 2 != 1:
    print('Enter the diamond''s height (positive odd): ')
    h = int(input())

n = h // 2

for k in range(1, n + 2):
    PrintLineOfDiamond(k, n)
for k in range(n, 0, -1):
    PrintLineOfDiamond(k, n)
