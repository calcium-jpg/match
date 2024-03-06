import json
import sys
import numpy as np

from match import match

sequence = [2,4,3,1,0,5,8,7,9,6]
random_numbers = []
amount = 0

for i in range(int(sys.argv[1])):
    random_numbers.append(np.random.choice(range(10), size=10, replace=False).tolist())
  
f = match(random_numbers, sequence)

for (i,j) in enumerate(f):
  if j['right'] >= 1:
    #print(j)
    amount += 1
  
print(f"Amount right: {amount}")