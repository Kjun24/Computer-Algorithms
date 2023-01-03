
import sys

global way
way = []

def all_the_way(graph, st, des, visit=[]):
    visit = visit + [st]
    if st == des:
        way.append(visit)
    for n in graph[st]:
        if n not in visit:
            all_the_way(graph, n, des, visit)
            
def make_dictionary(x,y,chart):
    g = dict()
    for m in range(x):
        for n in range(y):
            l=[]
            if n+1<y and chart[m][n] > chart[m][n+1]:
                l.append(str((y*m)+(n+1)))
            if n-1>0 and chart[m][n] > chart[m][n-1]:
                l.append(str((y*m)+(n-1)))
            if m+1<x and chart[m][n] > chart[m+1][n]:
                l.append(str((y*(m+1))+n))
            if m-1>0 and chart[m][n] > chart[m-1][n]:
                l.append(str((y*(m-1))+n))
            g[str((y*m)+n)] = l
    return g


def input_form():
    input_1 = sys.stdin.readline().strip().split()
    x_axis = int(input_1[0])
    y_axis = int(input_1[1])
    
    height_list = []
    
    for n in range(x_axis):
    	a = list(map(int,sys.stdin.readline().strip().split()))
    	height_list.append(a)
    	
    return x_axis, y_axis, height_list


if __name__ == "__main__":
    x_axis, y_axis, height_list = input_form()
    dic = make_dictionary(x_axis, y_axis, height_list)
    all_the_way(dic, '0', str(x_axis*y_axis - 1))
    print(len(way))
    way.clear()
    pass
