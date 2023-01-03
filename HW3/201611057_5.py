import heapq 
import sys
from heapq import heappush
from heapq import heappop

def reverse_heap_sort(l):
    heap = []
    for i in range(len(l)):
        heappush(heap, (-l[i],i))

    sorted_l = []
    while heap:
        sorted_l.append(heappop(heap))
    return sorted_l


def greedy_choices (satisfy_list,num_of_list):
    choosen_list = [0]*num_of_list
    maximal_satisfy = 0
    heap_sorted = reverse_heap_sort(satisfy_list)
    n=0
    
    while n < num_of_list:
        index = heappop(heap_sorted)[1]
        n += 1
        if index == 0 :
            if not(choosen_list[1] + choosen_list[2] == 2):
                choosen_list[index] = 1
            continue
        if index == 1 :
            if not((choosen_list[0] + choosen_list[2] == 2) or (choosen_list[3] + choosen_list[2] == 2)):
                choosen_list[index] = 1
            continue
        if index == num_of_list-1: 
            if not(choosen_list[index-1] + choosen_list[index-2] == 2):
                choosen_list[index] = 1
            continue
        if index == num_of_list-2 :
            if not((choosen_list[index-1] + choosen_list[index+1] == 2) or (choosen_list[index-2] + choosen_list[index-1] == 2)):
                choosen_list[index] = 1   
            continue
            
            
        if choosen_list[index-1] == 1 and choosen_list[index+1] == 1:
            pass
        elif choosen_list[index-1] == 1 and choosen_list[index-2] == 1:
            pass
        elif choosen_list[index+1] == 1 and choosen_list[index+2] == 1:
            pass
        else :
            choosen_list[index] = 1
            
    for i in range(num_of_list):
        maximal_satisfy += choosen_list[i]*satisfy_list[i]
        
    return maximal_satisfy


def input_form():
    num_of_booth = int(sys.stdin.readline().strip())
    input_list = [int(sys.stdin.readline().strip()) for i in range(num_of_booth)]
    return num_of_booth, input_list

    

if __name__ == "__main__":
    num_of_booth, input_list = input_form()
    print(greedy_choices (input_list, num_of_booth))
 
    pass
