import subprocess
import time

#plays the sound
subprocess.Popen("mpg123 ~/alarm.mp3 --loop 10")

time.sleep(10)

#stops the alarm
subprocess.call(["killall", "mpg123"])


