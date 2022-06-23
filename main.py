from algo_class import SortingAlgorithm
from tkinter import *
import random
import pygame


WIDTH, HEIGHT = 900, 500
# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms Visualizer")

sort_algo = SortingAlgorithm()
rand = list(range(WIDTH))
random.shuffle(rand)

algorithms_dict = {"BubbleSort": sort_algo.BubbleSort, 
    "SelectionSort": sort_algo.SelectionSort, 
    "InsertionSort": sort_algo.InsertionSort, 
    "CocktailShackerSort": sort_algo.CocktailShackerSort, 
    "OddEvenSort": sort_algo.OddEvenSort,
    "CombSort": sort_algo.CombSort}
algorithms_list = ["BubbleSort", "SelectionSort", "InsertionSort", 
        "CocktailShackerSort", "OddEvenSort", "CombSort"]

def sort():
    global rand
    rand = algorithms_dict[algorithms_list[choice.get()]].__call__(screen, rand)

def shuffle():
    global rand, screen
    random.shuffle(rand)

    sort_algo.draw(screen, rand)

# Window
window = Tk()
window.title("Choose Sorting Algorithms")

choice_frame = LabelFrame(window, text="Choose the Sorting Algorithm you want.", padx=5, pady=5)
choice_frame.pack(padx=10, pady=10)

choice = IntVar()
for i in range(2):
    for j in range(3):
        rb = Radiobutton(choice_frame, text=algorithms_list[j+i*3], variable=choice, value=j+i*3)
        rb.grid(row=j, column=i)

Button(window, text="Shuffle", command=shuffle).pack()
Button(window, text="Sort", command=sort).pack()

while True:
    window.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    sort_algo.draw(screen, rand)
