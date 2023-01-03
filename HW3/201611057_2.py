import heapq 
import sys
from heapq import heappush
from heapq import heappop

def bestcost(cost_list,time_list,day_limit):
    
    cost_per_time = []
    choosen_task_cost=[]
    days = [0]*day_limit

    for n in range(len(cost_list)):
        heapq.heappush(cost_per_time, (-cost_list[n]/time_list[n],n))
        
    while cost_per_time:
        check_task = heapq.heappop(cost_per_time)[1]
        if time_list[check_task]+check_task > day_limit:
            continue
        occupy = False
        for i in range(time_list[check_task]):
            if days[i+check_task] > 0:
                occupy = True
                
        if occupy == False:
            for i in range(time_list[check_task]):
                days[i+check_task]=1
            choosen_task_cost.append(cost_list[check_task])
    return sum(choosen_task_cost)


def input_form():
    day_limit = int(sys.stdin.readline().strip())
    time_table = []
    cost_table = []
    
    for n in range(day_limit):
    	nums = sys.stdin.readline().strip().split()
    	time_table.append(int(nums[0]))
    	cost_table.append(int(nums[1]))
    	
    return day_limit, time_table, cost_table


if __name__ == "__main__":
    day_limit, time_table, cost_table = input_form()
    print(bestcost(cost_table, time_table, day_limit))
    pass
