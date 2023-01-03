import math
import random
import sys
import heapq


def min_memory(num_of_disk, before_disk, after_disk):
    diff_heap = []
    before_heap = []
    for i in range(num_of_disk):
        diff = after_disk[i] - before_disk[i]
        heapq.heappush(diff_heap, (-diff,[diff,i]))
        heapq.heappush(before_heap, (-before_disk[i],before_disk[i]))
    max_diff_list = heapq.heappop(diff_heap)[1]
    max_diff = max_diff_list[0]
    max_disk = heapq.heappop(before_heap)[1]
    
    if max_diff < max_disk:
        return max_disk
    else:
        return before_disk[max_diff_list[1]]


def input_form():
    disk_num = int(sys.stdin.readline().strip())
    
    before_disk = []
    after_disk = []
    
    for n in range(disk_num):
    	stt = list(map(int,sys.stdin.readline().strip().split()))
    	before_disk.append(stt[0])
    	after_disk.append(stt[1])

    return disk_num, before_disk, after_disk


if __name__ == "__main__":
    num_of_disk, b_disk, a_disk = input_form()

    print(min_memory(num_of_disk, b_disk, a_disk))

    pass
