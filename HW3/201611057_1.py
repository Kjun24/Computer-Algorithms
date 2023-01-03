import heapq 
import sys
from heapq import heappush
from heapq import heappop

def shortestpath(input_g, start, end):
    w = {}
    hq = []
    for vertex in input_g:
        w[vertex] = float('inf')
    w[start] = 0
    heappush(hq, [start, w[start]])
    while hq:
        now_vertex, now_w = heappop(hq)
        if w[now_vertex] >= now_w:
            for ver, weight in graph[now_vertex].items():
                if w[ver]>(now_w + weight):
                    w[ver]=(now_w + weight)
                    heappush(hq, [ver,w[ver]])
    result = w[end]
    if result == float('inf'):
        return float('inf')
    return w[end]
    
def shortpath_node (input_g, node1, node2, end):
    path_costs = []
    
    start_n1 = shortestpath(input_g,'1',node1)
    start_n2 = shortestpath(input_g,'1',node2)
    n1_n2 = shortestpath(input_g,node1,node2)
    n1_end = shortestpath(input_g,node1,end)
    n2_end = shortestpath(input_g,node2,end)
    start_end = shortestpath(input_g,'1',end)
    
    path_costs.append(start_n1*2 + start_n2*2 + start_end)
    path_costs.append(start_n1*2 + start_n2 + n2_end)
    path_costs.append(start_n2*2 + start_n1 + n1_end)
    path_costs.append(start_n2 + n1_n2 + n1_end)
    path_costs.append(start_n1 + n1_n2 + n2_end)
    if min(path_costs) == float('inf'):
    	return "NO WAY"
    return min(path_costs)    


def input_form():
    input_1 = sys.stdin.readline().strip().split()
    number_of_node = int(input_1[0])
    number_of_edge = int(input_1[1])
    
    input_2 = sys.stdin.readline().strip().split()
    node_1 = input_2[0]
    node_2 = input_2[1]
    
    graph = {}
    
    for n in range(number_of_node):
    	graph[str(n+1)]={}
    
    for i in range(number_of_edge):
    	input_3 = sys.stdin.readline().strip().split()
    	graph[input_3[0]][input_3[1]] = int(input_3[2])
    	graph[input_3[1]][input_3[0]] = int(input_3[2])
    
    return number_of_node, node_1, node_2, graph


if __name__ == "__main__":
    number_of_node, node_1, node_2, graph = input_form()
    print(shortpath_node(graph,node_1,node_2,str(number_of_node)))
    pass
