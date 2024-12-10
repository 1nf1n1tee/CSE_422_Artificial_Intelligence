# -*- coding: utf-8 -*-
"""21201759_Sadman Taufiq Mahin_CSE422_12_Assignment02_Fall2024.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bTCZ2Npz7C3yhqdFupT8GwS4dPhYiOeR
"""

import random
#generating population
def population(size,start=0,end=1):
    pop = [random.randint(start,end) for i in range(size)]
    return pop

# def fitness(arr,n,t):
def overlap(arr,n,t):
  count=0
  p = 0
  i = 0
  while True:
    # print(count,p)
    if arr[i] == 1:
      if count==0:
        count = 1
      else:
        p+=1
    i+=1
    if i%n==0 and i!=0:
      count=0
      # print('reset')
    if i == n*t:
      break
  return p

def consistency(arr,n,t):
  count=0
  for i in range(n):
    # print(abs(arr[i]+arr[i+n]+arr[i+n+n]-1))
    count += abs(arr[i]+arr[i+n]+arr[i+n+n]-1)
  return count

def fitness(arr,n,t):
  f = -(overlap(arr,n,t)+consistency(arr,n,t))
  return f

#cross over
def cross_over(sample):
  arr1 = sample[random.randint(0,len(sample)-1)]
  arr2 = sample[random.randint(0,len(sample)-1)]
  p = random.randint(0,len(arr1))
  # print(arr1,arr2)
  # print(p)
  arr1[p:],arr2[p:] = arr2[p:],arr1[p:]
  return arr1,arr2
#mutation
def mutation(arr):
  p = random.randint(0,len(arr)-1)
  if arr[p] == 1:
    arr[p] = 0
  else:
    arr[p] = 1
  return arr

inp = open('/content/input.txt','r')
out = open('/content/output.txt','w')

def genetic_algo(n,t):
  sample = []
  for i in range(10):
    sample.append(population(n*t))
  flag = True
  count = 0
  while flag:
    for i in range(5):
      cross_over(sample)
    for i in sample:
      mutation(i)
    for i in sample:
      if fitness(i,n,t) == 0:
        # print('solution',i)
        flag = False
        return i
    count+=1
cmd = inp.readline().split()
n = int(cmd[0])
t = int(cmd[1])
ans = genetic_algo(n,t)
out.write('Encoded Answer:')
out.write('\n')
for i in ans:
  out.write(str(i))
out.close()
inp.close()