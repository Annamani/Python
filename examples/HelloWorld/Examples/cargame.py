command=" "
started=False
stopped=True
while True:
    command=input(">").lower()
    if command=="start":
        if started:
            print("Car is already started")
        else:
            started=True
            print("Car is ready to go....")
    elif command=="stop":
        if not stopped:
            print("car is already stopped")
        else:
            stopped=False
            print("Car Stopped....")
    elif command=="help":
        print("""
        Please enter from below options
        start--to start the car
        stop--to stop the car
        quit--to quit
        """)
    elif command=="quit":
        break
    else:
        print("Sorry! I don't understand the command...")
