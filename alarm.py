import os
import subprocess
import playsound

questions = [
    ["A", "Chicago is a \n A: City \n B: State \n C: Country"]
]

# plays the sound
# subprocess.call(["mpg123", './alarm.mp3'])
#os.system("nohup mpg123 -q -o alsa ./alarm.mp3")

playsound("alarm.mp3", **0**)
NotDone = 1
while NotDone:
    for item in questions:
        print(item[1])
        tries = 0
        while tries < 3:
            user_ans = input("Answer : ")

            if item[0] == user_ans.upper():
                break

            tries += 1
    NotDone = 0


# stops the alarm
subprocess.call(["killall", "mpg123"])

