from algo_class import SortingAlgorithm 
import random, time
import test
import pygame

WIDTH, HEIGHT = 900, 500
rand = [random.randint(0, 200) for _ in range(100)]

sort = SortingAlgorithm()

algorithms_dict = {"QuickSort": sort.QuickSort, "BubbleSort": sort.BubbleSort,
 "SelectionSort": sort.SelectionSort, "InsertionSort": sort.InsertionSort}
algorithms_list = ["QuickSort", "BubbleSort", "SelectionSort", "InsertionSort"]

print("Choose the sorting algorithm:")
for nb, algorithm in enumerate(algorithms_list):
    print("\t" + str(nb) + ". " + algorithm)
choice = int(input())

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

print(rand)
g = algorithms_dict[algorithms_list[choice]](screen, rand)
print(g)
