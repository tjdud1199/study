'''
ATM 1대. 1~N번까지의 번호가 매겨짐. i번 사람이 인출하는데 걸리는 시간은 Pi분
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하라!

< 아이디어 >
인출 시간이 적은 사람 순으로 돈을 인출한다.
기다린 시간을 따로 저장한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
wait = 0
result = 0
times = list(map(int, input().split()))
times.sort()

for time in times:
    result += time + wait
    wait += time

print(result)