### K-Way Merge Sort

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

## Just modify below "pass" code blocks
def mergesortK(A, n, k):
    if n <= 1:
        return A

    unit = n//k
    # part1. You need to handle additional edge cases
    if unit == 0:
        pass

    # part2. reculsively do something
    pass

    # part3. merge something and return it
    pass


if __name__ == "__main__":
    pass
