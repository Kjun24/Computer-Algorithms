### 3-Way Merge Sort
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


def mergesort2(A, n):
    if n <= 1:
        return A

    unit = n//2

    L = mergesort2(A[:unit],unit)
    R = mergesort2(A[unit:n],n-unit)

    return merge(L, R)


def input_form():
    input_num = int(sys.stdin.readline().strip())
    input_list = [sys.stdin.readline().strip() for i in range(input_num)]
    input_list_2 = [sys.stdin.readline().strip() for i in range(input_num)]
    if input_num < 1:
    	print("Something is wrong...")
    	raise Exception("There is no input.")
    if input_list_2[0] != '':
    	print("Something is wrong...")
    	raise Exception
    if input_list[-1] == '':
    	print("Something is wrong...")
    	raise Exception1
    in_list=[]
    for a in input_list:
    	in_list.append(int(a))
    return in_list


## Just modify below "pass" code blocks

def mergesort3(A, n):
    if n <= 1:
        return A

    unit = n//3

    # part1. You need to handle additional edge cases (Hint: see above)
    if unit == 0:
        if A[0]> A[1]:
            a = A[0]
            A[0] = A[1]
            A[1] = a
        return A


    # part2. reculsively do something
    L = mergesort3(A[:unit],unit)
    M = mergesort3(A[unit:unit*2],unit)
    R = mergesort3(A[unit*2:],n-(unit*2))


    # part3. merge something and return it
    L_M = merge(L,M)
    return merge(L_M,R)



if __name__ == "__main__":
    input_A = input_form()
    #print("Input Array  : ", input_A)
    sorted_A = mergesort3(input_A, len(input_A))
    #print("Sorted Array : ", sorted_A)
    isSorted(input_A, sorted_A)

    pass

