import subprocess
import time

#plays the sound
subprocess.call(["mpg123", "--loop", "10", "./alarm.mp3"])

print("deb1")

#stops the alarm
subprocess.call(["killall", "mpg123"])

print("deb2")


