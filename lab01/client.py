import os

while True:
    # Local stuff v
    user_input = input()
    # Local stuff ^

    # Dekker algorithm v
    os.environ["CLIENT_TO_DATA"] = "1"

    while os.environ["SERVER_TO_DATA"] == "1":
        if os.environ["NEXT_DATA"] != "1":
            os.environ["CLIENT_TO_DATA"] = "0"
            
            while os.environ["NEXT_DATA"] != "1":
                pass

            os.environ["CLIENT_TO_DATA"] = "1"
    
    # Critical stuff v
    data_file = open('data.txt', 'w')
    data_file.write(user_input)
    data_file.close()
    # Critical stuff ^

    os.environ["NEXT_DATA"] = "2"
    os.environ["CLIENT_TO_DATA"] = "0"

    # Dekker algorith ^

