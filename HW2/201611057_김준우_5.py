
import sys
sys.setrecursionlimit(10**7)

def Counting_Money(Num_b,Num_c,b,c):
    i,m,typ = 0,0,0
    if Num_b >= Num_c: ## 지폐가 더 많은 경우
        i = Num_b
        m = Num_c
    else: ## 동전이 더 많은 경우
        i = Num_c
        m = Num_b
        typ = 1
        
    counts = [0,0,0,0,0,0] ##counts의 0~3 index는 지폐의 수, 4~5는 동전의 수
        
    for i_ in range(m):
        if (b[i_]==1):
            counts[0] += 1
        elif (b[i_]==2):
            counts[1] += 1
        elif (b[i_]==3):
            counts[2] += 1
        elif (b[i_]==4):
            counts[3] += 1
        if (c[i_]==1):
            counts[4] += 1
        elif (c[i_]==2):
            counts[5] += 1
            
    for i_ in range(i-m):
        if (typ == 1):
            if (c[i_+m]==1):
                counts[4] += 1
            elif (c[i_+m]==2):
                counts[5] += 1
        elif (typ == 0):
            if (b[i_+m]==1):
                counts[0] += 1
            elif (b[i_+m]==2):
                counts[1] += 1
            elif (b[i_+m]==3):
                counts[2] += 1
            elif i(b[i_+m]==4):
                counts[3] += 1
                
    return counts

def output_func(c):
    s = 1000*c[0]+5000*c[1]+10000*c[2]+50000*c[3]+100*c[4]+500*c[5]
    print ("(￦50000, "+str(c[3])+"), (￦10000, "+str(c[2])+"), (￦5000, "+str(c[1])+"), (￦1000, "+str(c[0])+"), (￦500, "+str(c[5])+"), (￦100, " +str(c[4])+")")
    print ("(Sum, ￦"+str(s)+")")
    
def input_form():
    input_num_1 = int(sys.stdin.readline().strip())
    input_num_2 = int(sys.stdin.readline().strip())
    input_list_1 = list(map(int,sys.stdin.readline().strip().split()))
    input_list_2 = list(map(int,sys.stdin.readline().strip().split()))
    return input_num_1, input_num_2, input_list_1, input_list_2

if __name__ == "__main__":
    i1, i2, i3, i4 = input_form()
    output_func(Counting_Money(i1,i2,i3,i4))
    pass

