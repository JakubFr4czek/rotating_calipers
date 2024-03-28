import copy as cp
import functools as ft
from collections import deque

class Graham:

    def __det(a, b, c):
        return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])

    def __distance(P, A, B):
        
        #Wektor PA
        PA = (A[0] - P[0], A[1] - P[1])

        #Moduł wektora PA
        PA_mod = (PA[0] ** 2 + PA[1] ** 2)**(0.5)   

        #Wektor PB
        PB = (B[0] - P[0], B[1] - P[1])

        #Moduł wektora PB
        PB_mod = (PB[0] ** 2 + PB[1] ** 2)**(0.5)

        if PA_mod > PB_mod:
            return 1
        else:
            return -1

    @classmethod
    def __cmp(self, P, A, B, eps = 0):
        
        # -1 - B jest po lewej od PA
        # 1 - B jest po prawej od PA
        # 0 - B jest na PA

        calculatedOrientation = self.__orient(P, A, B)
        
        if calculatedOrientation != 0:
            return calculatedOrientation
        else:
            return self.__distance(P, A, B)

    @classmethod
    def __orient(self, P, A, B, eps = 0):
        
        # -1 - B jest po lewej od PA
        # 1 - B jest po prawej od PA
        # 0 - B jest na PA
        
        res = self.__det(P, A, B)
        
        if res < -eps: #B leży po prawej stronie od PA
            return 1
        elif res > eps: #B leży po lewej stronie od PA
            return -1
        else:
            return 0

    @classmethod
    def graham_algorithm(self, X):

        #Zbiór pusty
        if len(X) == 0:
            return []
        
        #Kopiuję tablicę, żeby nie zniszczyć oryginalnej, która potem jest używana do wyświetlania
        Q = cp.deepcopy(X) 

        #Punkt początkowy o najmiejszej współrzędnej y oraz x
        P = min(Q, key = lambda l: (l[1],l[0])) 

        #Pozbywam się P z listy
        Q.remove(P) 
        
        #Sortuje zbiór punktów po najmniejszym kącie między prostą P - Punkt względem OX
        Q = [P] + sorted(Q, key=ft.cmp_to_key(lambda A, B: self.__cmp(P, A, B)))
        
        #Tworze stos
        stack = deque()
        
        #Wrzucam 3 pierwsze punkty na stos (w tym P)
        
        if len(Q) > 0:
            stack.append(Q[0])
        else:
            return list(stack)
            
        if len(Q) > 1:
            stack.append(Q[1])
        else:
            return list(stack)
            
        if len(Q) > 2:    
            stack.append(Q[2])
        else:
            return list(stack)
        
        # Jeśli wsród 3 pierwszych punktów dwa są współliniowe to usuwam ten na szyczycie stosu (bo są posortowane rosnąco)
        if self.__orient(stack[-3], stack[-2], stack[-1]) == 0: 
            stack.pop()
            
        
        i = 3
        
        while i < len(Q):
            A = stack[-2]
            B = stack[-1]
            C = Q[i]

            if self.__orient(A, B, C) == 0: #B i C są współlinowe (Ale także posortowane rosnąco, więc usuwam ten pierwszy bo będzie mniejszy)

                stack.pop()
                stack.append(Q[i])
                i += 1
            elif self.__orient(A, B, C) == 1: 
                
                stack.pop()
            else:
                stack.append(Q[i])
                i += 1

        graham_points_a = list(stack)
        
        return graham_points_a