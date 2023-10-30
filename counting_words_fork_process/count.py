import os
import sys
import time

def count(file_name, keyword):
  print('Starting process:', os.getpid(), 'with arguments', file_name, keyword)

  children = []
  counter = 0

  file = open(file_name, 'r')

  for line in file:
    print(os.getpid(), ':', 'Reading line:', line)

    if '\input' in line:
      pid = os.fork()
      print(os.getpid(), ':', 'PID:', pid)

      if pid > 0:
        children.append(pid)
        continue
      else:
        print(os.getpid(), ':', 'Starting subprocess...')
        sys.exit(count(line[7:-2], keyword))
    elif keyword in line:
      counter += 1
      print(os.getpid(), ':', 'Counter:', counter)
      continue
    else:
      pass
  file.close()

  for each in children:
    print(os.getpid(), ':', 'Waiting for subprocess', each, 'to finish...')
    _, status = os.waitpid(each, 0)
    subprocess_returned_value = status >> 8
    print(os.getpid(), ': Subprocess', each, 'returned:', subprocess_returned_value)
    counter += subprocess_returned_value
  
  print(os.getpid(), ':', 'Ended process with counter:', counter)
  return counter


# count(sys.argv[1], sys.argv[2])
count('plikA.txt', 'Stoi')
