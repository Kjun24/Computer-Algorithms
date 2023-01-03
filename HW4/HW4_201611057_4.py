import math
import random
import sys
import copy
import gc

def find_min_score_to_win(graph, score_list, nodes, edges):
    score_range = []
    a_can_get_score = sum(graph['0'].values())
    for i in range(a_can_get_score+1):
        score_range.append(score_list[0]+i)
    
    graph_score_sum = 0
    connected_edge = [0]*nodes ##각 node에 연결된 edge의 weight 합

    for a in list(graph.keys()):
        for b in list(graph[a].keys()):
            graph_score_sum += graph[a][b]
            connected_edge[int(a)] += graph[a][b]
            connected_edge[int(b)] += graph[a][b]
    mini_graph_score_sum = graph_score_sum - a_can_get_score #0노드를 뺀 그래프에서 남은 경기의 수
    
    ##print(sum(score_list))
    
    for a_score in score_range:
        ##print("a score is ",a_score)
        a_s = copy.deepcopy(a_score)
        mini_g = copy.deepcopy(graph)
        scores = copy.deepcopy(score_list)

        if (sum(scores)+graph_score_sum-a_score)/(nodes-1) > a_score-1:
            ##print ("It's impossible for ",(sum(scores)+graph_score_sum-a_score)/(nodes-1))
            continue
        
        ## 0노드의 edge부터 처리 // 0이 이기는 경우를 max score probabilty node에 배정
        c_edge = copy.deepcopy(connected_edge)
        while a_score > scores[0]:
            max_score_node = float('-inf')
            max_score = float('-inf')
            
            for node in list(mini_g['0'].keys()):
                if scores[int(node)] + c_edge[int(node)] >= max_score:
                    max_score = scores[int(node)] + c_edge[int(node)]
                    max_score_node = node
            mini_g['0'][max_score_node] -= 1
            a_score -= 1
            c_edge[int(max_score_node)] -= 1
            if (mini_g['0'][max_score_node] == 0): ## 승부가 다 종료된 엣지는 제거
                del mini_g['0'][max_score_node]
            
        scores[0] = a_s
        
        for node in list(mini_g['0'].keys()): ## 0에 연결된 나머지 노드 분배 및 제거
            scores[int(node)] += mini_g['0'][node]
            del mini_g['0'][node]
        del mini_g['0']    
        ##print("#####Done" , scores)
        
        boolean = True
        
        ## 0을 제외한 나머지 그래프에서 edge 분배 // 랜덤하게 선택 
        for n in range(edges*pow(nodes,2)):
            mini_graph = copy.deepcopy(mini_g)
            rest_graph_edge_sum = copy.deepcopy(mini_graph_score_sum)
            while (rest_graph_edge_sum > 0):
                random_node = random.choice(list(mini_graph.keys()))
                if len(mini_graph[random_node]) == 0:
                    del mini_graph[random_node]
                    continue

                random_edge = random.choice(list(mini_graph[random_node].keys()))
                if mini_graph[random_node][random_edge] == 0:
                    del mini_graph[random_node][random_edge]
                    continue

                if (scores[int(random_node)]>scores[int(random_edge)]):
                    scores[int(random_edge)] += 1
                    if scores[int(random_edge)] > scores[0]:
                        break
                    mini_graph[random_node][random_edge] -= 1
                else :
                    scores[int(random_node)] += 1
                    if scores[int(random_node)] > scores[0]:
                        break
                    mini_graph[random_node][random_edge] -= 1

                rest_graph_edge_sum -= 1
            
            for i in scores[1:]:
                if scores[0] <= i:
                    boolean = False
                    break
                    
            if boolean:
                return scores[0]
        gc.collect()

    return -1
    
    
    
def input_form():
    num_student, num_games = map(int,sys.stdin.readline().strip().split())
    scores = list(map(int,sys.stdin.readline().strip().split()))
    graph = {}
    games_list = []
    
    for i in range(num_student):
    	graph[str(i)] = {}
    	games_list.append([0]*num_student)
    
    for m in range(num_games):
    	stt = list(map(int,sys.stdin.readline().strip().split()))
    	if (stt[0]<stt[1]):
    	    games_list[stt[0]][stt[1]] += 1
    	else:
    	    games_list[stt[1]][stt[0]] += 1
    	    
    for n in range(num_student):
        for o in range(num_student):
            if games_list[n][o] == 0:
            	continue
            else :
            	graph[str(n)].update({str(o):games_list[n][o]})

    return num_student, num_games, graph, scores
    
    
    
def monte_carlo(graph, score_list, nodes, edges):
    a =[]
    for i in range(10):
        a.append(find_min_score_to_win(graph, score_list, nodes, edges))

    return(min(a))


if __name__ == "__main__":
    n_student, n_games, input_graph, score_l = input_form()

    print(monte_carlo(input_graph, score_l, n_student, n_games))

    pass
