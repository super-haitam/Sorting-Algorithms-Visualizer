# Give up on QuickSort, and all algorithms requiring recursivity
import pygame


class SortingAlgorithm:
    def OddEvenSort(self, screen, lst):
        lst = lst[:]
        for _ in range(len(lst)//2):
            print(_)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return lst

            if len(lst)%2 == 0:
                # Even Sort
                even = [(i, lst[num*2+1]) for num, i in enumerate(lst[:: 2])]
                lst = self.SortOddEvenList(even)
                
                # Odd Sort
                first, last = lst[0], lst[-1]
                odd = [(i, lst[num*2+2]) for num, i in enumerate(lst[1: -1: 2])]
                lst = [first] + self.SortOddEvenList(odd) + [last]

            else:
                # Even Sort
                last = lst[-1]
                even = [(i, lst[num*2+1]) for num, i in enumerate(lst[: -1: 2])]
                lst = self.SortOddEvenList(even) + [last]
                
                # Odd Sort
                first = lst[0]
                odd = [(i, lst[num*2+2]) for num, i in enumerate(lst[1:: 2])]
                lst = [first] + self.SortOddEvenList(odd)     
            
            self.draw(screen, lst)

        return lst

    def SortOddEvenList(self, lst):
        lst = lst[:]
        for num, (a, b) in enumerate(lst):
            if b < a:
                # Swap them
                lst[num] = (b, a)
        
        l = []
        for tupl in lst:
            l.append(tupl[0])
            l.append(tupl[1])
        return l

    def CocktailShackerSort(self, screen, lst):
        lst = lst[:]
        num_viewed_integers = 0
        while lst != sorted(lst):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return lst

            # Left to Right
            for a in range(0, len(lst)-num_viewed_integers-1):
                if lst[a+1] < lst[a]:
                    temp = lst[a]
                    lst[a] = lst[a+1]
                    lst[a+1] = temp

            # Right to Left
            for a in range(len(lst)-1, num_viewed_integers, -1):
                if lst[a] < lst[a-1]:
                    temp = lst[a]
                    lst[a] = lst[a-1]
                    lst[a-1] = temp
            num_viewed_integers += 1

            self.draw(screen, lst)
        return lst

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
