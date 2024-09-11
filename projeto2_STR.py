# -*- coding: utf-8 -*-
"""
Código principal do projeto 02
"""

import json

#Load the tasks list
with open('tasks_list.json', 'r') as file:
  input_data = json.load(file)


#Numbers of tasks
n = len(input_data['tasks'])

#Utilization
U = 0

#Computing the usability and the viability
for i in range(n):
  task = input_data['tasks'][i]
  
  U += task['execution_time']/task['period']

certainly_viable = U <= n*(2**(1/n)-1)

#schedulability is certainly viable
if certainly_viable:
  output_data = {'schedulability': 'viable'}
    
  sorted_tasks = sorted(input_data['tasks'], key = lambda x: x['period'])
  suggested_schedule = []

  for i in range(n):
    suggested_schedule.append({'priority': i+1, 'id': sorted_tasks[i]['id']})

  output_data['suggested_schedule'] = suggested_schedule

#schedulability is unknown
elif U <= 1:
  output_data = {'schedulability': 'unknown'}

#schedulability is certainly not viable
else:
   output_data = {'schedulability': 'not viable'}


#Exporting the resut as a json file
with open('schedulability.json', 'w') as file:
  json.dump(output_data, file, indent=4)



''' Mostrando informações no LOG '''
#Show the tasks
print('#'*30)
print(f'{"TASKS":^30}')
print('#'*30)

#Computing the usability and the viability
for i in range(n):
  task = input_data['tasks'][i]

  #mostra as tasks
  print(f'ID = {task["id"]} \nPeriod = {task["period"]} \nExecutation Time = {task["execution_time"]}\n')


#Show the test
print()
print('#'*30)
print(f'{"TEST":^30}')
print('#'*30)
print(f'U = {U}')
print(f'Test  = {n*(2**(1/n)-1)}')


#Show the Schedule
print()
print('#'*30)
print(f'{"SCHEDULE":^30}')
print('#'*30)

print(f'schedulability = {output_data["schedulability"]}\n')

try:
    for task in output_data['suggested_schedule']:
        print(f'Priority = {task["priority"]} \nID = {task["id"]}\n')
except:
    pass
