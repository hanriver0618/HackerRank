#!/bin/python3

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(max([sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3]) for j in range(4) for i in range(4)]))
		
