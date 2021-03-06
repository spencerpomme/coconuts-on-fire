def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    longest = []
    increasing = None
    # main for loop
    for i in range(len(L) - 1):
        # this for loop decides if current run is increasing
        for j in range(i+1, len(L)):
            if L[j] == L[j-1]:
                continue
            elif L[j] > L[j-1]:
                increasing = True
                increase = [L[i]]
                break
            else:
                increasing = False
                decrease = [L[i]]
                break
        if increasing == None:
            if len(L[i:]) > len(longest):
                return sum(L[i:])
        # this for loop actually adds items in respective list
        for j in range(i+1, len(L)):
            if L[j] >= L[j-1] and increasing:
                increase.append(L[j])
                if j == len(L) - 1 and len(increase) > len(longest):
                    return sum(increase)
            elif L[j] <= L[j-1] and not increasing:
                decrease.append(L[j])
                if j == len(L) - 1 and len(decrease) > len(longest):
                    return sum(decrease)
            else:
                if increasing and len(increase) > len(longest):
                    longest = increase[:]
                    increase = []
                elif not increasing and len(decrease) > len(longest):
                    longest = decrease[:]
                    decrease = []
                i = j - 1
                break
    # print(L, len(L), longest, j)
    return sum(longest)

l1 = [3, 3, 3, 3, 3]
l2 = [3, 2, -1, 2, 7]
l3 = [100, 200, 300, -100, -200, -1500, -5000]
l4 = [3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]

print(longest_run(l1))
print(longest_run(l2))
print(longest_run(l3))
print(longest_run(l4))
