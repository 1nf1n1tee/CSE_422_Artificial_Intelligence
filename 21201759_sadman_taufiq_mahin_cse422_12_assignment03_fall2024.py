# -*- coding: utf-8 -*-
"""21201759_Sadman Taufiq Mahin_CSE422_12_Assignment03_Fall2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HJaiLw3n9HB2UIxhJjzFA3V_hecVhX_m

Task 1
"""

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def populate(self, d=0):
        if d == 5:
            self.data = random.choice([1, -1])
        else:
            self.left = Node(None)
            self.right = Node(None)
            self.left.populate(d + 1)
            self.right.populate(d + 1)

    def pruning(self, d, a, b, isMax):
      if self.left is None and self.right is None:
          return self.data

      if isMax:
          maxVal = float('-inf')
          if self.left:
              maxVal = max(maxVal, self.left.pruning(d + 1, a, b, False))
              a = max(a, maxVal)
          if b <= a:
              return maxVal
          if self.right:
              maxVal = max(maxVal, self.right.pruning(d + 1, a, b, False))
              a = max(a, maxVal)
          return maxVal
      else:
          minVal = float('inf')
          if self.left:
              minVal = min(minVal, self.left.pruning(d + 1, a, b, True))
              b = min(b, minVal)
          if b <= a:
              return minVal
          if self.right:
              minVal = min(minVal, self.right.pruning(d + 1, a, b, True))
              b = min(b, minVal)
          return minVal

game1 = Node(None)
game1.populate()

game2 = Node(None)
game2.populate()

game3 = Node(None)
game3.populate()

result1 = game1.pruning(0, float('-inf'), float('inf'), True)
result2 = game2.pruning(0, float('-inf'), float('inf'), True)
result3 = game3.pruning(0, float('-inf'), float('inf'), True)

inp = open('/content/input.txt','r')
out = open('/content/output.txt','w')

characters = ['Scorpion','Subzero']
results = [result1,result2,result3]
player = int(inp.readline())
if sum(results) > 0:
  out.write(f'Game Winner:{str(characters[player])}')
  out.write(f'\nTotal Rounds Played: 3')
  for i in range(3):
    if results[i] > 0:
      out.write(f'\nWinner of Round {i+1}: {str(characters[player])}')
    else:
      out.write(f'\nWinner of Round {i+1}: {str(characters[player-1])}')
else:
  out.write(f'Game Winner:{str(characters[player-1])}')
  out.write(f'\nTotal Rounds Played: 3')
  for i in range(3):
    if results[i] > 0:
      out.write(f'\nWinner of Round {i+1}: {str(characters[player])}')
    else:
      out.write(f'\nWinner of Round {i+1}: {str(characters[player-1])}')
out.close()
inp.close()

"""Task 2"""

class Node2:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def populate(self, d=0,arr=[3, 6, 2, 3, 7, 1, 2, 0]):
        if d == 3:
            self.data = arr.pop(0)
        else:
            self.left = Node2(None)
            self.right = Node2(None)
            self.left.populate(d + 1)
            self.right.populate(d + 1)

    def pruning(self, d, a, b, isMax):
      if self.left is None and self.right is None:
          return self.data

      if isMax:
          maxVal = float('-inf')
          if self.left:
              maxVal = max(maxVal, self.left.pruning(d + 1, a, b, False))
              a = max(a, maxVal)
          if b <= a:
              return maxVal
          if self.right:
              maxVal = max(maxVal, self.right.pruning(d + 1, a, b, False))
              a = max(a, maxVal)
          return maxVal
      else:
          minVal = float('inf')
          if self.left:
              minVal = min(minVal, self.left.pruning(d + 1, a, b, True))
              b = min(b, minVal)
          if b <= a:
              return minVal
          if self.right:
              minVal = min(minVal, self.right.pruning(d + 1, a, b, True))
              b = min(b, minVal)
          return minVal

    def dark_pruning(self, d, a, b):
        if self.left is None and self.right is None:
            return self.data

        maxVal = float('-inf')
        if self.left:
            maxVal = max(maxVal, self.left.dark_pruning(d + 1, a, b))
            a = max(a, maxVal)
        if b <= a:
            return maxVal
        if self.right:
            maxVal = max(maxVal, self.right.dark_pruning(d + 1, a, b))
            a = max(a, maxVal)
        return maxVal

pacman = Node2(None)
pacman.populate()

result = pacman.pruning(0, float('-inf'), float('inf'), True)
result_dark = pacman.dark_pruning(0, float('-inf'), float('inf'))

inp = open('/content/input2.txt','r')
out = open('/content/output2.txt','w')
magic = int(inp.readline())
if result_dark-magic>result:
  out.write(f'The new minimax value is {result_dark-magic}. Pacman goes right and uses dark magic')
else:
  out.write(f'The minimax value is {result}. Pacman does not use dark magic')
out.close()
inp.close()