# -*- coding: utf-8 -*-
"""
Código utilizado para gerar a lista de tarefas de forma aleatória
"""

from random import randint
import json

#Constants
MIN_TASK_NUM = 1
MAX_TASK_NUM = 5

MIN_PERIOD = 50
MAX_PERIOD = 200

MIN_EXC_TIME= 10
MAX_EXC_TIME = 50

#Numbers of tasks
n = randint(MIN_TASK_NUM, MAX_TASK_NUM)

#The list of tasks
output_data = {'tasks': []}

#Creating random tasks
for i in range(n):
  task = {
            'id': f'T{i+1}',
            'period': randint(MIN_PERIOD, MAX_PERIOD),
            'execution_time': randint(MIN_EXC_TIME, MAX_EXC_TIME)
           }

  output_data['tasks'].append(task)

#Exporting the tasks list as a json file
with open('tasks_list.json', 'w') as file:
  json.dump(output_data, file, indent=4)
  