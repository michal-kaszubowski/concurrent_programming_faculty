import socket, struct

connections_data = {}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5001))
print(">$ Server is up & running!")

while True:
    print(">$ New Round!")
    client0_data, client0_address = server.recvfrom(1024)
    print(">$ Player One -", client0_address)
    client1_data, client1_address = server.recvfrom(1024)
    print(">$ Player Two -", client1_address)
    
    if client0_address not in connections_data:
        connections_data[client0_address] = 0
    if client1_address not in connections_data:
        connections_data[client1_address] = 0

    guess0 = struct.unpack('!i', client0_data)[0]
    guess1 = struct.unpack('!i', client1_data)[0]

    winner = ()

    # 1=rock, 2=paper, 3=scissors, 0=end
    if (guess0 == 1 and guess1 == 1):
        pass
    if (guess0 == 1 and guess1 == 2):
        winner = client1_address
    if (guess0 == 1 and guess1 == 3):
        winner = client0_address
    
    if (guess0 == 2 and guess1 == 1):
        winner = client0_address
    if (guess0 == 2 and guess1 == 2):
        pass
    if (guess0 == 2 and guess1 == 3):
        winner = client1_address

    if (guess0 == 3 and guess1 == 1):
        winner = client1_address
    if (guess0 == 3 and guess1 == 2):
        winner = client0_address
    if (guess0 == 3 and guess1 == 3):
        pass


    if (guess0 == 0 or guess1 == 0):
        server.sendto(struct.pack('!i', 0), client1_address)
        server.sendto(struct.pack('!i', 0), client0_address)
        
        if connections_data[client0_address] > connections_data[client1_address]:
            print(">$ Player One Won The Game!")
        elif (connections_data[client1_address] > connections_data[client0_address]):
            print(">$ Player Two Won The Game!")
        else:
            print(">$ Game Tie!")

        print(">$ Game Over!\nFinal Score:", connections_data[client0_address], ":", connections_data[client1_address])
        connections_data = {}
        continue


    if (winner == client0_address):
        loser = client1_address
        print(">$ Player One Won!")
    else:
        loser = client0_address
        print(">$ Player Two Won!")


    if winner != ():
        connections_data[winner] += 1

        server.sendto(struct.pack('!i', 1), winner)
        server.sendto(struct.pack('!i', 2), loser)
    else:
        server.sendto(struct.pack('!i', 3), client0_address)
        server.sendto(struct.pack('!i', 3), client1_address)
        print(">$ Tie!")

