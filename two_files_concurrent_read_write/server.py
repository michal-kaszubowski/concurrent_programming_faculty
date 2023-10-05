import os

os.environ["CLIENT_TO_DATA"] = "0"
os.environ["SERVER_TO_DATA"] = "0"
os.environ["NEXT_DATA"] = "1"

while True:
    # Dekker algorithm v
    os.environ["SERVER_TO_DATA"] = "1"

    while os.environ["CLIENT_TO_DATA"] == "1":
        if os.environ["NEXT_DATA"] != "2":
            os.environ["SERVER_TO_DATA"] = "0"
            
            while os.environ["NEXT_DATA"] != "2":
                pass

            os.environ["SERVER_TO_DATA"] = "1"
    
    # Critical stuff v
    
    # Here read data from data.txt

    # Critical stuff ^

    # Dekker algorith ^

