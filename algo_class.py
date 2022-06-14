import random
import pygame
import time


class List:
    def __init__(self, lst):
        self.lst = lst
        self.id_lst = []


class Int:
    def __init__(self, value):
        pass


class SortingAlgorithm:
    def QuickSort(self, screen, lst):
        self.ProcessQuickSort(screen, lst)

    def ProcessQuickSort(self, screen, lst):
        if lst:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Pick random pivot
            rand_ind = random.randrange(len(lst))
            pivot = lst[rand_ind]
            lst = [lst[:rand_ind] if 0 <= rand_ind-1 else [], pivot, lst[rand_ind+1:]]
            
            # Nums that will be moved
            smaller_nums = [i for i in lst[0]+lst[2] if i < pivot]  # From Right to Left
            bigger_nums = [i for i in lst[0]+lst[2] if pivot <= i]  # From Left to Right

            lst[0] = smaller_nums[:]
            lst[2] = bigger_nums[:]
            
            # Remove all empty lists
            quick_sorted = [self.ProcessQuickSort(screen, lst[0]), pivot, self.ProcessQuickSort(screen, lst[2])]
            
            self.draw(screen, self.FixQuickSortReturn(quick_sorted))

            return quick_sorted
        else:
            return []
    
    def FixQuickSortReturn(self, temp):  # Make the self.QuickSort return 1d array
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
        return temp

    def BubbleSort(self, screen, lst):
        lst = lst[:]
        num_viewed_integers = 0
        for _ in range(len(lst)-1):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            for a in range(0, len(lst)-num_viewed_integers-1):
                if lst[a+1] < lst[a]:
                    temp = lst[a]
                    lst[a] = lst[a+1]
                    lst[a+1] = temp
            num_viewed_integers += 1

            self.draw(screen, lst)
        return lst

    def SelectionSort(self,screen, lst):
        lst = lst[:]
        for num in range(len(lst)):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Index it in the rest of the list, not in all of it, cuz it could select a sorted num
            index_minimun = lst[num:].index(min(lst[num:])) + num

            temp = lst[num]
            lst[num] = lst[index_minimun]
            lst[index_minimun] = temp

            self.draw(screen, lst)
        return lst

    def InsertionSort(self, screen, lst):
        lst = lst[:]
        for num in range(len(lst[:-1])):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()

            next_num = lst[num+1]
            
            if next_num <= lst[num]:
                for n, j in enumerate(lst[:num+1]):
                    if next_num < j:
                        lst.pop(num+1)
                        lst.insert(n, next_num)
                        break
            self.draw(screen, lst)
        return lst

    def draw(self, screen, lst):
        screen.fill((0, 0, 0))

        w = screen.get_width() / len(lst)
        for num, el in enumerate(lst):
            h = screen.get_height()/(max(lst)+1) * el
            rect = pygame.Rect([num*w, screen.get_height()-h, w, h])
            pygame.draw.rect(screen, (255, 255, 255), rect)

        pygame.display.flip()
