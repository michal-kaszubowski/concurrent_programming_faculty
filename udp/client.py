import socket, struct

server_address = ("127.0.0.1", 5001)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(">$ Welcome to the RPS Tournament!\nType your choice carefully otherwise it's Game Over!\nReady? FIGHT!\n")

wins = 0

while True:
    user_input = input("<< ")
    match user_input:
        case 'rock':
            packed_data = struct.pack('!i', 1)
        case 'paper':
            packed_data = struct.pack('!i', 2)
        case 'scissors':
            packed_data = struct.pack('!i', 3)
        case _:
            packed_data = struct.pack('!i', 0)
    udp_socket.sendto(packed_data, server_address)
    print("...")
    server_response = udp_socket.recvfrom(1024)
    unpacked_response = struct.unpack('!i', server_response[0])[0]
    
    if (unpacked_response == 1):
        wins += 1
        print(">$ It's a win!")
        continue
    if (unpacked_response == 2):
        print(">$ Round lost.")
        continue
    if (unpacked_response == 3):
        print(">$ It's a tie!")
        continue
    if (unpacked_response == 0):
        print(">> Game finished.\nYou have won", wins, "times!")
        break

