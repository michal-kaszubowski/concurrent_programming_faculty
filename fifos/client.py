import os
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return (''.join(random.choice(letters) for i in range(length)))

my_queue = get_random_string(4)
server_queue = 'server_queue'

try:
    os.mkfifo(my_queue)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

output_queue = os.open(server_queue, os.O_WRONLY)

user_input = input('<< ')
user_input_len = len(user_input)

if user_input_len > 2 or user_input_len == 0:
    raise Exception('Wrong id format!')
elif user_input_len == 1:
    user_input = ' ' + user_input

output_data = '$msg?' + str(len(user_input) + len(my_queue) + 1) + user_input + ':' + my_queue
os.write(output_queue, output_data.encode())

try:
    input_queue = os.open(my_queue, os.O_RDONLY)
    _ = os.read(input_queue, 5)
    length = int(os.read(input_queue, 2).decode())
    message = os.read(input_queue, length).decode()

    print('>> Received:', message)
except Exception:
    print(">! Cannot parse queue")
