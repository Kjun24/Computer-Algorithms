
import sys

def can_reach(num_nation, input_list, num_visit, want_visit_list):
    stack = [want_visit_list[0]]
    visited = []
    for n in range(num_nation):
        current_index = stack.pop()-1
        current_node = input_list[current_index]
        visited.append(current_index+1)
        for i in range(num_nation):
            if current_node[i]==1 and (i+1) not in visited and (i+1) not in stack:
                stack.append(i+1)
        if len(stack) == 0:
            break
    for nation in want_visit_list:
        if nation not in visited:
            print('NO')
            return
    print('YES')
    return


def input_form():
    nations = int(sys.stdin.readline().strip())
    graph = []
    
    for n in range(nations):
    	small_g =[]
    	a = sys.stdin.readline()
    	for i in range(nations):
    	    small_g.append(int(a[i]))
    	graph.append(small_g)
    	
    num_visit_nations = int(sys.stdin.readline().strip())
    visit_nations = list(map(int, sys.stdin.readline().strip().split()))
    
    return nations, graph, num_visit_nations, visit_nations

    

if __name__ == "__main__":
    nations, graph, num_visit_nations, visit_nations = input_form()
    can_reach(nations, graph, num_visit_nations, visit_nations)
    pass
