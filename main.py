from algo_class import SortingAlgorithm 
import random, time
import test


rand = [random.randint(0, 200) for _ in range(20000)]

# rand = [72, 57, 9, 6, 94, 132, 0, 0]
# print(rand)

# rand = test.l
sort = SortingAlgorithm(0, 0)

t = time.time()
QuickSorted = sort.FixQuickSortReturn(sort.QuickSort(rand))
print("QuickSort: ", time.time()-t)

t = time.time()
BubbleSorted = sort.BubbleSort(rand)
print("BubbleSort: ", time.time()-t)

t = time.time()
SelectionSorted = sort.SelectionSort(rand)
print("SelectionSort: ", time.time()-t)

t = time.time()
InsertionSorted = sort.InsertionSort(rand)
print("InsertionSort: ", time.time()-t)

t = time.time()
Builtin = sorted(rand)
print("Built-in: ", time.time()-t)

print(SelectionSorted==QuickSorted==BubbleSorted==InsertionSorted==sorted(rand))
