import subprocess
import time

#plays the sound
subprocess.call(["/bin/mpg123", "--loop 10", "/home/pranav/alarm.mp3"])

time.sleep(10)

#stops the alarm
subprocess.call(["killall", "mpg123"])


