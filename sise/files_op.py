import numpy as np

def parse_array_from_file(file_name):
  file = open(file_name, 'r')
  parsed_data = [t.split(' ') for t in file.read().split('\n')]
  file.close()
  parsed_data.pop(0)
  return np.asarray(parsed_data).astype(int)

def write_to_solution_file(filename, moves):
  file = open(filename, 'w')
  if moves is None:
    file.write(str(-1))
  else:
    output = ' '.join(map(str, moves))
    file.write(str(len(moves)) + '\n')
    file.write(output)
  file.close()

def write_info_to_file(filename, moves, time):
  file = open(filename, 'w')
  if moves is None:
    file.write(str(-1) + '\n')
  else:
    file.write(str(len(moves)) + '\n')
  file.write(str(time) + '\n')
  file.close()