import os, sys, signal, sysv_ipc


def handle_terminate(signum, frame):
    print('\nTerminating...')
    server_queue.remove()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_terminate)

known_server_ipc_key = 11
my_pid = os.getpid()

user_input = input('<< ')

try:
    client_queue = sysv_ipc.MessageQueue(my_pid, sysv_ipc.IPC_CREAT)
    server_queue = sysv_ipc.MessageQueue(known_server_ipc_key)
except sysv_ipc.ExistentialError:
    print('Error occured during creating message queues! Use ipcs for debug!')
    sys.exit(1)

server_queue.send(user_input.encode(), True, my_pid)

response, _ = client_queue.receive(True, known_server_ipc_key)
print('>>', response.decode())

client_queue.remove()

