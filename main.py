#!/usr/bin/env python

from src.scale import Scale
from src.chord import Chord

common_prompt = """
    Welcome to the Music Theory CLI!
    
    This tool allows you to review the various chords and scales present in the musical literature.
    Whether you need to remember your chords, or you want to understand the theory behind music 
    better, this tool can come in handy.
    
    First, we will ask you to choose a task. The task can be "scale", "chord", or "exit".
    Next, if you chose "scale", it allows you to enter the scale name, which should be of the format:
    
        <note> <type>
        
    Here, note can be anything in the range of [A, G] and type can "major" or "minor"
    
    Similarly,if you chose "chord", we allow the same format, but now the chord type can
    be "major7" and "minor7", in addition to "major" and "minor", to indicate whether you want to 
    include the seventh interval in your chord or not.
    
    Thank you for reading this lengthy demo. Have fun!
"""

task_prompt = "task"
prompt_term = "> "


def main():
    print(common_prompt)
    while True:
        _user_in = input(task_prompt + prompt_term).strip()
        if _user_in == "exit":
            break
        if _user_in == "scale":
            handle_scale_request()
        elif _user_in == "chord":
            handle_chord_request()
        else:
            raise Exception("Illegal action value provided")

    print("Thank you for using this humble Music Theory tool!")


def handle_chord_request():
    prompt_for_chord = task_prompt + " Chord" + prompt_term
    chord_input = input(prompt_for_chord)
    [note, type] = chord_input.strip().split(" ")
    includes_seventh_interval = False
    if type == "major7" or type == "minor7":
        type = "major" if (type == "major7") else "minor"
        includes_seventh_interval = True
    ch = Chord()
    print(ch.get_chord(note, type, includes_seventh_interval))


def handle_scale_request():
    prompt_for_scale = task_prompt + " Scale" + prompt_term
    scale_input = input(prompt_for_scale)
    [note, type] = scale_input.strip().split(" ")
    sc = Scale()
    print(sc.get_scale(note, type))


if __name__ == "__main__":
    main()
