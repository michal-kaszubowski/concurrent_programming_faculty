import sysv_ipc


def parse_to_int(string):
    try:
        return int(string)
    except:
        return -1

def write(memory, string):
    string += '\0'
    memory.write(string.encode())

def read(memory):
    string = memory.read().decode()
    i = string.find('\0')
    if i != -1:
        string = string[:i]
    return string


master_semaphore_key = 11
client_semaphore_key = 12

master_memory_key = 11
client_memory_key = 12

master_points = 0
client_points = 0


try:
    master_semaphore = sysv_ipc.Semaphore(master_semaphore_key, sysv_ipc.IPC_CREX, 0o700, 0)
    client_semaphore = sysv_ipc.Semaphore(client_semaphore_key, sysv_ipc.IPC_CREX, 0o700, 0)
    master_memory = sysv_ipc.SharedMemory(master_memory_key, sysv_ipc.IPC_CREX)
    client_memory = sysv_ipc.SharedMemory(client_memory_key, sysv_ipc.IPC_CREX)
    
    master = True
    print('I am a master.')
    
    master_semaphore.release() # Master setup ready! | M1
except sysv_ipc.ExistentialError:
    master_semaphore = sysv_ipc.Semaphore(master_semaphore_key)

    master_semaphore.acquire() # Wait for the master setup | M0
    
    client_semaphore = sysv_ipc.Semaphore(client_semaphore_key)
    master_memory = sysv_ipc.SharedMemory(master_memory_key)
    client_memory = sysv_ipc.SharedMemory(client_memory_key)
    
    master = False
    print('I am a client.')

    client_semaphore.release() # Client setup ready! | C1


if master:
        client_semaphore.acquire() # Wait for the client setup | C0

round_counter = 1
while round_counter < 4:
    print('>$ Round:', round_counter)
    if master:
        master_input = input('<< Please chose a position of the winnig card in range [1,3]: ')

        if 0 < parse_to_int(master_input) < 4:
            write(master_memory, master_input)
            master_semaphore.release() # Master choice ready! M1
        else:
            print('>! Invalid input!')
            continue
        
        client_semaphore.acquire() # Wait for the client choice | C0

        client_input = read(client_memory)

        if master_input == client_input:
            client_points += 1
            print('Round lost.')
        else:
            master_points += 1
            print('You won!')

        round_counter += 1
    else:
        client_input = input('<< Please chose a position of the winnig card in range [1,3]: ')

        if 0 < parse_to_int(client_input) < 4:
            write(client_memory, client_input)
            client_semaphore.release() # Client choice ready! | C1
        else:
            print('>! Invalid input!')
            continue
        
        master_semaphore.acquire() # Wait for the master choice | M0

        master_input = read(master_memory)

        if master_input == client_input:
            client_points += 1
            print('You won the round!')
        else:
            master_points += 1
            print('Round lost.')
        
        round_counter += 1


print('>$ End of the game. Thank You for playing!\nFinall score:', master_points, '[master] :', client_points, '[client]')
if master:
    if master_points > client_points:
        print('You won the game!')
    else:
        print('Game lost.')
    
    client_memory.detach()
    
    master_semaphore.release() # Detached from client_memory
    
    client_semaphore.acquire() # Wait for the client to detach from master_memory

    master_memory.remove()

    sysv_ipc.remove_semaphore(master_semaphore.id)
else:
    if client_points > master_points:
        print('You won the game!')
    else:
        print('Game lost.')
    
    master_memory.detach()

    client_semaphore.release() # Detached from master_memory

    master_semaphore.acquire() # Wait for the master to detach from client_memory

    client_memory.remove()

    sysv_ipc.remove_semaphore(client_semaphore.id)

