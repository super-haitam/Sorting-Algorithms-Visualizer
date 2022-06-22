import random
import pygame
from algo_class import SortingAlgorithm 


WIDTH, HEIGHT = 900, 500
rand = [random.randint(0, 500) for _ in range(WIDTH)]
# rand = [0, 7, 2, 5, 3]

sort = SortingAlgorithm()

algorithms_dict = {"BubbleSort": sort.BubbleSort, 
    "SelectionSort": sort.SelectionSort, 
    "InsertionSort": sort.InsertionSort, 
    "CocktailShackerSort": sort.CocktailShackerSort, 
    "OddEvenSort": sort.OddEvenSort}
algorithms_list = ["BubbleSort", "SelectionSort", 
    "InsertionSort", "CocktailShackerSort", "OddEvenSort"]

print("Choose the sorting algorithm:")
for nb, algorithm in enumerate(algorithms_list):
    print("\t" + str(nb) + ". " + algorithm)
choice = int(input())

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualizer")

print(rand)
reversed_rand = list(sorted(rand, reverse=True))

sorted_rand = algorithms_dict[algorithms_list[choice]].__call__(screen, rand)
print(rand == sorted(rand))
print(sorted_rand == sorted(rand))
