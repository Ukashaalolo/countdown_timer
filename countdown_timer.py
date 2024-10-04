import time
def countdown_timer():
    duration = int(input("Enter the duration in seconds: "))
    while duration:
        mins, secs = divmod(duration, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        print(f"Time left: {timer}")
        time.sleep(1)
        duration -= 1
    print("Time's up!")

countdown_timer()