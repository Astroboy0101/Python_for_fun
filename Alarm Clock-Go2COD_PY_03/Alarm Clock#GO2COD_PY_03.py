#GO2COD_PY_03
# By Kena Fayera
import time
import datetime
from playsound import playsound
import threading
import sys

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}. Waiting...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            alarm_thread = threading.Thread(target=play_alarm)
            alarm_thread.start()

            while True:
                user_input = input('Enter "quit" to stop the alarm: ').strip().lower()
                if user_input == 'quit':
                    stop_alarm()
                    sys.exit() #I want it to exit the program completely, but it didn't work.So use the ur PCs' exit button.
            break
        time.sleep(30)

def play_alarm():
    playsound("alarm_sound.mp3")  # Change it to your own sound. I used a gospel song (Yet) 😇.

def stop_alarm():
    print("Alarm stopped.")

if __name__ == "__main__":
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    alarm_time = input(f"The current time is {current_time} \nEnter the alarm time (Hour[HH]:Minute[MM]): ")
    set_alarm(alarm_time)
