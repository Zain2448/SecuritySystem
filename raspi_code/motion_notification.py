from gpiozero import MotionSensor
from time import sleep
from datetime import datetime

pir = MotionSensor(4)

with open("/home/zain/TeamProject/motion_status.txt", 'w') as file:
    file.truncate(0)  # Clears the file content


def write_motion_event():
    with open("/home/zain/TeamProject/motion_status.txt", 'a') as file:
        file.write(
            f"Intruder!!! {datetime.now().strftime('Date: %d_%m_%Y and Time: %H_%M_%S')}" + '\n')  # Adding a newline for readability


print("Running")
while True:
    pir.when_motion = write_motion_event
    sleep(5)

