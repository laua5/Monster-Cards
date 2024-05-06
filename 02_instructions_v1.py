"""This function will be used to display instructions to user"""
import easygui


def instructions():
    easygui.msgbox("Instructions will go here")


instructions_ = easygui.buttonbox("Display instructions or exit",
                                  choices=["View Instructions", "Exit"])

if instructions_ == "View Instructions":
    instructions()
else:
    easygui.msgbox("Program continues otherwise")
