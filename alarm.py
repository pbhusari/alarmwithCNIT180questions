import os
import subprocess

questions = [
    ["A", "Chicago is a \n A: City \n B: State \n C: Country"]
]

# plays the sound
# subprocess.call(["mpg123", './alarm.mp3'])

os.system("mpg123 ./alarm.mp3")

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

# stops the alarm
subprocess.call(["killall", "mpg123"])

print("deb2")
