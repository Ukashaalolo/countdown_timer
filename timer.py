import time
def countdown_timer():
    duration = int(input("Enter the duration in seconds: "))
    while duration > 0:
        print(f"Time remaining: {duration} seconds")
        time.sleep(1)
        duration -= 1
    print("Time's up!")

countdown_timer()