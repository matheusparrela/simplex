import Simplex
import BranchAndBound
import graphicalSolution
import json

# Opening JSON file
file = open('../problem\problem.json', )

# returns JSON object as a dictionary
data = json.load(file)
# Closing file
file.close()


print(data, '\n')
test = data.values()
print(test)
z = list(data['constraintsMethod'].values())
print(list(data['numberVariablesMethod']))









'''
t.start()
print(t.dict_result[0])

with open('../problem\result.json', 'w') as json_file:
    json.dump(t.dict_result, json_file, indent=4)
'''