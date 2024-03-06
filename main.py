import json
import numpy
import sys

from match import match

sequence = [1,2,3,4,5,6,7,8,9,0]
random_numbers = []
    
for i in range(int(sys.argv[1])):
    random_numbers.append(numpy.random.randint(10, size=10).tolist())    

file = open("./output.json", "w")
file.write(json.dumps(match(random_numbers, sequence)))
file.close()