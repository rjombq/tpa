a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if a >= sum - a or b >= sum - b or c >= sum - c:
    print('NO')
else:
    print('YES')
