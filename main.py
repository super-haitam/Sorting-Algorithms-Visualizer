from algo_class import SortingAlgorithm 
import random, time
import test
import pygame

# Screen
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))


rand = [random.randint(0, 200) for _ in range(50)]

sort = SortingAlgorithm()
h = sort.InsertionSort(screen, rand)

print(h)
