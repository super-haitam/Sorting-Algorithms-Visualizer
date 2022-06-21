import pygame
import time


class SortingAlgorithm:
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
