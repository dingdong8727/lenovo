import time
from player import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALEAT!!!",
            message = "Take a break! It has been an hour!",
            timeout = 10

        )
        time.sleep(3600)