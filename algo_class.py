import random


class SortingAlgorithm:
    def __init__(self, x, y):
        pass

    def QuickSort(self, lst):
        if lst:
            # Pick random pivot
            rand_ind = random.randrange(len(lst))
            pivot = lst[rand_ind]
            lst = [lst[:rand_ind] if 0 <= rand_ind-1 else [], pivot, lst[rand_ind+1:]]
            
            # Nums that will be moved
            smaller_nums = [i for i in lst[0]+lst[2] if i < pivot]  # From Right to Left
            bigger_nums = [i for i in lst[0]+lst[2] if pivot <= i]  # From Left to Right

            lst[0] = smaller_nums[:]
            lst[2] = bigger_nums[:]
            
            quick_sorted = [self.QuickSort(lst[0]), pivot, self.QuickSort(lst[2])]
            for n in range(len(quick_sorted)):
                if quick_sorted[n] == []:
                    quick_sorted[n] = None
                elif isinstance(quick_sorted[n], list):
                    if len(quick_sorted[n]) == 1:
                        quick_sorted[n] = quick_sorted[n][0]
            return [i for i in quick_sorted if i is not None]
        else:
            return []
    
    def FixQuickSortReturn(self, temp):
        # Count is the number of lists in l
        count = len([i for i in temp if isinstance(i, list)])
        
        while count:
            l = []
            for i in temp:
                if isinstance(i, int):
                    l.append(i)
                elif isinstance(i, list):
                    l.extend(i)

            temp = l[:]
            count = len([i for i in l if isinstance(i, list)])
        return l

    def BubbleSort(self, lst):
        num_viewed_integers = 0
        for a in range(len(lst)):
            for b in range(a+1, len(lst)-num_viewed_integers):
                if lst[b] < lst[a]:
                    temp = lst[a]
                    lst[a] = lst[b]
                    lst[b] = temp
            num_viewed_integers += 1
        return lst

    def SelectionSort(self, lst):
        lst = lst[:]
        for num in range(len(lst)):
            # Index it in the rest of the list, not in all of it, cuz it could select a sorted num
            index_minimun = lst[num:].index(min(lst[num:])) + num

            temp = lst[num]
            lst[num] = lst[index_minimun]
            lst[index_minimun] = temp
        return lst

    def InsertionSort(self, lst):
        for num, i in enumerate(lst[:-1]):
            next_num = lst[num+1]
            
            if next_num < i:
                for n, j in enumerate(lst[:num+1]):
                    if j < next_num:
                        lst[num+1] = j
                        lst.insert(next_num, n)
        return lst      
