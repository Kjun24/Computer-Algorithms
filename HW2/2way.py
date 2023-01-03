### 2-Way Merge Sort
## From 2022 DGIST CSE301 Lecture 03
# This is an example code of basic 2-way merge sort.

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

    # part1. handling edge cases
    if n <= 1:
        return A

    # part2. reculsively do something
    unit = n//2
    L = mergesort2(A[:unit],unit)
    R = mergesort2(A[unit:n],n-unit)

    # part3. merge something and return it
    return merge(L, R)

if __name__ == "__main__":
    A = [36, 12, 54, 97, 94, 56, 86, 8, 42, 13, 37, 86, 55, 44, 17, 57, 19, 68, 37, 75]
    print("Input Array  : ", A)
    sortedA = mergesort2(A, len(A)) 
    print("Sorted Array : ", sortedA)
    isSorted(A,sortedA)
