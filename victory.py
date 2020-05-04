from playsound import playsound
import os

directory = os.path.dirname(os.path.realpath(__file__))

file = directory + '\\audio.wav'
file_ff = directory + '\\audioff.wav'
familyfriendly = True # Change this for a more familly appropriate audiofile


def victor():
    if familyfriendly:
        playsound(file_ff)
    else:
        playsound(file)
    return
#Why does setting the 2nd "block" argument to False cause the file to not play?

