import os
import errno
import time
import signal, sys

def handle_pass(signum, frame):
    pass

def handle_terminate(signum, frame):
    sys.exit(0)


signal.signal(signal.SIGHUP, handle_pass)
signal.signal(signal.SIGINT, handle_pass)
signal.signal(signal.SIGUSR1, handle_terminate)

server_queue = 'server_queue'
data_base = {
    0: 'Zbigniew JSON',
    1: 'Stanislaw Grad',
    2: 'Kornel Oberza',
    3: 'Szymon Chacina',
    4: 'Konrad Wol',
    5: 'Halina Stonoga'
}

try:
    os.mkfifo(server_queue)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

input_queue = os.open(server_queue, os.O_RDONLY) # open to read | waits for sbd to write???

_ = os.open(server_queue, os.O_WRONLY|os.O_NDELAY) # do not end queue on no one writing

while True:
    try:
        _ = os.read(input_queue, 5)
        length = int(os.read(input_queue, 2).decode())
        message = os.read(input_queue, length).decode()
        message_array = message.split(':')
        
        req_id = int(message_array[0])
        if not req_id in data_base:
            print('Cannot find data')
            continue
        
        output_data = '$msg?' + str(len(data_base[req_id])) + data_base[req_id]
        output_queue = os.open(message_array[1], os.O_WRONLY)
        os.write(output_queue, output_data.encode())
        continue

    except Exception:
        print(">! Cannot parse queue")
        break

