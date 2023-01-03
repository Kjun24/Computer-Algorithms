import math
import random
import sys

def make_dictionary (task_list,task_number):
    dic = {}
    for task in task_list:
        if (task in dic):
            dic[task] += 1
        else :
            dic[task] = 1
    return dic

def cpu_schedule(task_list, task_dic, rest_time):
    if rest_time == 0:
        return len(task_list)
    list_all_task = sorted(list(task_dic.values()),reverse = True)
    
    task_line = []
    n=0
    m=rest_time
    
    while sum(list_all_task) > 0:
        i = 0
        ##print(list_all_task)
        ##print(task_line) 
        if len(task_line) < m :
            while i in task_line or list_all_task[i]==0:
                i += 1
                if  i == len(list_all_task)-1:
                    break
            if i in task_line[n-m:n] or i > len(list_all_task) or list_all_task[i]==0:
                task_line.append(float('inf'))
                n += 1
                continue   
            task_line.append(i)
            list_all_task[i] -= 1
        else :
            while i in task_line[n-m:n] or list_all_task[i]==0:
                i += 1
                if  i == len(list_all_task)-1:
                    break
            if i in task_line[n-m:n] or i > len(list_all_task) or list_all_task[i]==0:
                ##print(i)
                task_line.append(float('inf'))
                n += 1
                continue
            task_line.append(i)
            list_all_task[i] -= 1
           
        n += 1
    ##print(list_all_task)
    ##print(task_line)
    return n
            

def input_form():
    input_1 = sys.stdin.readline().strip().split()
    number_of_task = int(input_1[0])
    m_time = int(input_1[1])
    
    input_list = sys.stdin.readline().strip()
    task_list = []
    for n in range(number_of_task):
    	task_list.append(input_list[n])

    return number_of_task, m_time, task_list


if __name__ == "__main__":
    num_of_task, m, tasks = input_form()
    dic = make_dictionary(tasks, num_of_task)
    print(cpu_schedule (tasks, dic, m))
    
    pass
