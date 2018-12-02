import pygame

questions = [
    ["A", "Chicago is a \n A: City \n B: State \n C: Country"]
]

# plays the sound

pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")
pygame.mixer.music.play(loops=-1)

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
