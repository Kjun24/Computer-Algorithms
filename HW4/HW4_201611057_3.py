import math
import random
import sys
import copy

def random_choice(graph_map):
    while True :
        random_node1 = random.choice(list(graph_map.keys()))
        if len(graph_map[random_node1]) > 0:
            return random_node1
            

def Min_Cut (graph_map, start, target):
    left=start
    right=target
    
    min_cuts = []
    
    while len(graph_map.values()) > 2:
        random_node1 = random_choice(graph_map)
        random_node2 = random.choice(list(graph_map[random_node1]))
        random_edge = graph_map[random_node1][random_node2]
        #find random edge
        
        if random_node1 == left or random_node2 == left:
            left = min(random_node1, random_node2)
        if random_node1 == right or random_node2 == right:
            right = min(random_node1, random_node2)
        #random node가 타겟 노드인 경우, 합쳐진 노드 정보 저장 (번호가 최소인 노드로 합쳐짐)
        
        super_node = min(random_node1, random_node2)
        merge_node = max(random_node1, random_node2)
        
        if super_node in graph_map[merge_node]:
            del graph_map[merge_node][super_node]
        
        if len(graph_map[merge_node]) > 0:
            for n in list(graph_map[merge_node].keys()):
                if n in graph_map[super_node]:
                    graph_map[super_node][n] += graph_map[merge_node][n]
                else :
                    graph_map[super_node][n] = graph_map[merge_node][n]
        del graph_map[merge_node]
        
        if merge_node in graph_map[super_node]:
            del graph_map[super_node][merge_node]
            
        for node in list(graph_map.keys()):
            if merge_node in graph_map[node]:
                if super_node in graph_map[node]:
                    change_value = copy.deepcopy(graph_map[node][merge_node])
                    del graph_map[node][merge_node]
                    graph_map[node][super_node] += change_value
                else:
                    change_value = copy.deepcopy(graph_map[node][merge_node])
                    del graph_map[node][merge_node]
                    graph_map[node][super_node] = change_value
    return graph_map,left, right
    

def karger_mincut(graph_map, start, target, num_of_edge, num_of_vertex):
    min_cuts = float("inf")
    for i in range(2*pow(num_of_edge,3)):
        graph = copy.deepcopy(graph_map)
        a, b ,c = Min_Cut (graph, start, target)
        if (b != c):
            index_1 = list(a.keys())[0]
            index_2 = list(a.keys())[1]
            value_1 = list(a[index_1].values())[0]
            value_2 = 0
            if len(a[index_2]) > 0:
                value_2 = list(a[index_2].values())[0]
            cuts = value_1 + value_2
            min_cuts = min(min_cuts, cuts)
    return min_cuts
    
    
    
def input_form():
    num_node, num_edge = map(int,sys.stdin.readline().strip().split())
    
    graph = {}
    
    for i in range(num_node):
    	graph[str(i+1)] = {}
    
    for m in range(num_edge):
    	stt = list(map(str,sys.stdin.readline().strip().split()))
    	if (int(stt[0])<int(stt[1])):
    	    graph[stt[0]].update({stt[1] : int(stt[2])})
    	else:
    	    graph[stt[1]].update({stt[0] : int(stt[2])})
    ##print(graph)
    start_node, target_node = map(str,sys.stdin.readline().strip().split())


    return num_node, num_edge, graph, start_node, target_node
    
    


if __name__ == "__main__":
    n_node, n_edge, input_graph, s_node, t_node = input_form()

    print(karger_mincut(input_graph, s_node, t_node, n_edge, n_node))

    pass
