
command = ""
started = False
stopped = True
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
    elif command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Vroom vroooom! 🚗")
    elif command == "stop":
        if stopped:
            print("Car is already stopped!")
        else:
            stopped = True
            print("Car stopped ✋🛑")
    elif command == "quit":
        break
    else:
        print("I don't understand 🤔")
