import os
import sys
import time

def count(file_name, keyword):
  children = []
  counter = 0

  file = open(file_name, 'r')

  for line in file:
    if '\input' in line:
      pid = os.fork()

      if pid > 0:
        children.append(pid)
      else:
        sys.exit(count(line[7:-2], keyword))
    else:
      counter += line.lower().count(keyword.lower())
  file.close()

  for each in children:
    _, status = os.waitpid(each, 0)
    subprocess_returned_value = status >> 8
    counter += subprocess_returned_value
  
  return counter


print(count(sys.argv[1], sys.argv[2]))
