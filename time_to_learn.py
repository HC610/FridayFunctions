import time
# UNIX TIME

# print(time.time())

# print(time.ctime())

# def calculateTime(num1,num2):
#    time1 = time.time()
#    result = num1 * num2
#    time2 = time.time()
#    print(f"the answer is {result} which took {time2 - time1} seconds")

# calculateTime(43,43)

# def sleep_function(sleeptime):
#     print("Going Sleep")
#     time.sleep(sleeptime)
#     print("Wake up")
    
# sleep_function(5)

# NAME INPUT 

# name = input("Whats your name? ")
# print("Hello", name)

# proceed = input("Do you want to Proceed  Y/N").upper()
# if proceed == "Y":
#     print("Proceeding")
# elif proceed == "N":
#     print("Stop")
# else:
#     print("Please only enter Y or N")

# PYTHON STOP WATCH

import time

start = input("Press Enter to start the stopwatch...")

if start == "":
    start_time = time.time()

    stop = input("Press Enter to stop the stopwatch...")
# If condition to ensure only enter is being passed in.
    if stop == "":
        end_time = time.time()
        # Rounded to clean up the time display
        elapsed = round(end_time - start_time, 2)
        print(f"Elapsed time: {elapsed} seconds")
    else:
        print("Invalid input. Only press Enter.")
else:
    print("Invalid input. Only press Enter.")


    





