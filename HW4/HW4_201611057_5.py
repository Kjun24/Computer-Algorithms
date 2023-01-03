import numpy as np
import math
import sys

def traveling_salesman(x,visited_node,check_node,dp_matrix,costs_matrix,num_city):
    total = float('inf')
    if visited_node > check_node:
        return 
    elif visited_node == check_node:
        return costs_matrix[x][0]
    
    for j in range(1,check_node):
        if x!=j and dp_matrix[j] == float('-inf'):
            visited_node += 1
            dp_matrix[j] = 1
            total = min(total,costs_matrix[x][j]
                        +traveling_salesman(j, visited_node, check_node, dp_matrix, costs_matrix,num_city))
            dp_matrix[j] = float('-inf')
            visited_node -= 1
    return total



def manhatan_distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
    
def input_form():
    num_of_city = int(sys.stdin.readline().strip())+2
    
    matrix = []
    input_list = list(map(int,sys.stdin.readline().strip().split()))
    ranged_list =[]
    ##print(input_list)
    
    for i in range(num_of_city):
    	ranged_list.append(input_list[2*i:2*i+2])
    	matrix.append([])
    	
    copy_ = ranged_list[1]
    del ranged_list[1]
    ranged_list.append(copy_)
    
    for n in range(num_of_city):
        for m in range(num_of_city):
            if n == m:
            	matrix[n].append(0)
            else:
            	matrix[n].append(manhatan_distance(ranged_list[n],ranged_list[m]))

    return matrix, num_of_city, ranged_list
    
    


if __name__ == "__main__":
    costs_matrix, num_city, ranged_list = input_form()
    if len(costs_matrix) == 1:
        print(costs_matrix[0][0])
    dp_matrix = [float('-inf')] * (num_city+1)
    x = traveling_salesman(0, 1, len(costs_matrix), dp_matrix, costs_matrix, num_city)
    y = manhatan_distance(ranged_list[0],ranged_list[num_city-1])
    print(x-y)


    pass
