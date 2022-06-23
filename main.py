from algo_class import SortingAlgorithm
import random
import pygame


WIDTH, HEIGHT = 900, 500
rand = [random.randint(0, 500) for _ in range(WIDTH)]
# rand = [1, 8, 0, 7, 2, 5, 0, 3, 9]

sort = SortingAlgorithm()

algorithms_dict = {"BubbleSort": sort.BubbleSort, 
    "SelectionSort": sort.SelectionSort, 
    "InsertionSort": sort.InsertionSort, 
    "CocktailShackerSort": sort.CocktailShackerSort, 
    "OddEvenSort": sort.OddEvenSort,
    "CombSort": sort.CombSort,
    "CountingSort": sort.CountingSort}
algorithms_list = ["BubbleSort", "SelectionSort", "InsertionSort", 
        "CocktailShackerSort", "OddEvenSort", "CombSort", "CountingSort"]

print("Choose the sorting algorithm:")
for nb, algorithm in enumerate(algorithms_list):
    print("\t" + str(nb) + ". " + algorithm)
choice = int(input())

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualizer")

# print(rand)
reversed_rand = list(sorted(rand, reverse=True))
# print(sorted(rand))

sorted_list = algorithms_dict[algorithms_list[choice]].__call__(screen, rand)

