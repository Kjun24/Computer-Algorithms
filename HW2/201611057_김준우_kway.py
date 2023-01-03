### K-Way Merge Sort
import sys
sys.setrecursionlimit(10**7)

def isSorted(InputArr, YourArr):
    if (YourArr == sorted(InputArr)): 
        print("Well Sorted!")
    else:
        print("Something is wrong...")
    return

def merge(L, R):
    result = []

    l, r = 0, 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            result.append(L[l])
            l += 1
        else:
            result.append(R[r])
            r += 1

    result.extend(L[l:])
    result.extend(R[r:])

    return result

def input_form_k():
    inp_ = sys.stdin.readline().strip()

    if inp_.count(' ') == 0 & inp_[inp_.find(' ')+1].isdigit():
        print("Something is wrong...")
        raise Exception("It needs two inputs. (1.Size of Array 2.k-way)")
    inp = inp_.split()
    input_num = int(inp[0])
    input_k = int(inp[1])
    
    if input_num < 1:
    	print("Something is wrong...")
    	raise Exception("There is no input.")
    if input_k < 2:
        print("Something is wrong...")
        raise Exception("Value k cannot be under 2.") 
    input_list = [sys.stdin.readline().strip() for i in range(input_num)]
    input_list_2 = [sys.stdin.readline().strip() for i in range(input_num)]
    if input_list_2[0] != '':
    	print("Something is wrong...")
    	raise Exception
    if input_list[-1] == '':
    	print("Something is wrong...")
    	raise Exception
    	
    return input_list, input_k
        

## Just modify below "pass" code blocks
def mergesortK(A, n, k):
    if n <= 1:
        return A
    A = A.copy()

    unit = n//k
    # part1. You need to handle additional edge cases
    if unit == 0:
        return mergesortK(A, n, k-1)

    # part2. reculsively do something
    i = k
    united_list = []
    while i > 1:
        united_list.append(mergesortK(A[:unit], unit, k))
        del A[:unit]
        i = i - 1
    united_list.append(mergesortK(A, len(A), k))

    # part3. merge something and return it
    m = len(united_list)-1
    while m > 0:
        united_list[m-1] = merge(united_list[m-1], united_list[m])
        m = m -1
    return united_list[0]


if __name__ == "__main__":
    Input_A, Input_k = input_form_k()
    #print("Input Array  : ", Input_A)
    sorted_A = mergesortK(Input_A, len(Input_A), Input_k)
    #print("Sorted Array : ", sorted_A)
    isSorted(Input_A, sorted_A)
    pass
