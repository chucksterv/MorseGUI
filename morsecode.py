## Toggle LEDs when the GUI buttons are pressed ##

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led_white=LED(14)
blinkRate=0.25


### GUI DEFINITIONS ###
win = Tk()
win.title("MorseCode")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


### Event Functions ###
def morse_dash():
    led_white.on()
    time.sleep(blinkRate*4)
    led_white.off()
    time.sleep(blinkRate)
    
def morse_pause():
    time.sleep(blinkRate)

def morse_dot():
    led_white.on()
    time.sleep(blinkRate)
    led_white.off()
    time.sleep(blinkRate)
    
CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}


def blink(character):
    character = character.upper()
    encodedCharacter = CODE[character] + " "
    
    for i in encodedCharacter:
        if i == ".":
            morse_dot()
        elif i == "-":
            morse_dash()
        else:
            morse_pause()

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    return inputValue
    
def callBothFuncs():
    inputValue = retrieve_input()
    blink(inputValue)
    
def close():
    RPi.GPIO.cleanup()
    win.destroy()



### WIDGETS ###

# Button, triggers the connected command when it is pressed

textBox = Text(win, font=myFont, height=1, width=24)
textBox.grid(row=0, column=1)

blinkButton=Button(win, font=myFont, height=1, width=6, text="Blink", command=callBothFuncs)
blinkButton.grid(row=1, column=1)
                        
exitButton = Button(win, text='Exit', font=myFont, command=close, height=1, width=6)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever