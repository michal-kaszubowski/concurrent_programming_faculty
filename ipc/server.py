import signal, sys, time, sysv_ipc


def handle_terminate(signum, frame):
    print('\nTerminating...')
    server_queue.remove()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_terminate)

dictionary = {
    'pies': 'dog',
    'kot': 'cat',
    'krowa': 'cow',
    'kruk': 'crow'
}

known_server_ipc_key = 11

try:
    server_queue = sysv_ipc.MessageQueue(known_server_ipc_key, sysv_ipc.IPC_CREAT)
except _:
    print('Cannot create message queue. It might already exist!')
    sys.exit(1)
print('Server started!')

while True:
    message, messageType = server_queue.receive()
    message = message.decode()

    try:
        client_queue = sysv_ipc.MessageQueue(messageType)

        if message not in dictionary:
            client_queue.send('No entry with the passed value!'.encode(), True, known_server_ipc_key)
            continue
        
        client_queue.send(dictionary[message].encode(), True, known_server_ipc_key)
    except sysv_ipc.ExistentialError:
        print(f"Error! Cannot send data to client with key {messageType}. Invalid key!")
        continue

    time.sleep(5) # For testing only!

