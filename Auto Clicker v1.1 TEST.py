import ctypes
import ctypes.wintypes
import pyautogui
from pyautogui import LEFT, MIDDLE, RIGHT
import time
import keyboard
#Required modules for auto clicker to work
global isRunning
isRunning=0
#Weather or not the autoclicker is running
clicks=0
#Number of times the 'trackMouse' function has been called
from tkinter import *
from tkinter import simpledialog

"""_______________________________Changelog__________________________________"""

# v0.1.1 Added setting to turn mouse position output on or off
# v0.2 Added ability to change click frequency
# v1.0 Added hotkey for turning the autoclclicker on or off
# v1.0.1 Auto clicker automatically resets clicks when click amount is reached so it can be run again without rerunning the program
# v1.0.2 Added ability to change hotkey for starting/stopping 
# v1.0.2.1 Made slightly more user friendly

# Planned feature: Ability to manually select coordinates for autoclicker

# Potential feature: Basic UI

"""______________________________Mouse_Events________________________________"""

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_LEFTCLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_RIGHTCLICK = MOUSEEVENTF_RIGHTDOWN + MOUSEEVENTF_RIGHTUP
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_MIDDLECLICK = MOUSEEVENTF_MIDDLEDOWN + MOUSEEVENTF_MIDDLEUP

def _size():
        return (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))


"""________________________Send_Mouse_Event_function_________________________"""

def _sendMouseEvent(ev, x, y, dwData=0):
    assert x != None and y != None, 'x and y cannot be set to None'
    width, height = _size()
    convertedX = 65536 * x // width + 1
    convertedY = 65536 * y // height + 1
    ctypes.windll.user32.mouse_event(ev, ctypes.c_long(convertedX), ctypes.c_long(convertedY), dwData, 0)
    

"""_____________________________Click_Function_______________________________"""

def _click(x, y, button):
    """Send the mouse click event to Windows by calling the mouse_event() win32
    function.

    Args:
      button (str): The mouse button, either 'left', 'middle', or 'right'
      x (int): The x position of the mouse event.
      y (int): The y position of the mouse event.

    Returns:
      None
    """
    if button not in (LEFT, MIDDLE, RIGHT):
        raise ValueError('button arg to _click() must be one of "left", "middle", or "right", not %s' % button)

    if button == LEFT:
        EV = MOUSEEVENTF_LEFTCLICK
    elif button == MIDDLE:
        EV = MOUSEEVENTF_MIDDLECLICK
    elif button ==RIGHT:
        EV = MOUSEEVENTF_RIGHTCLICK

    try:
        _sendMouseEvent(EV, x, y)
    except (PermissionError, OSError):
       
        pass

"""_______________________________Settings___________________________________"""

outputPos='true'
#Weather or not the autoclicker should output the mouse position in the console

clickFrequency=500
#How frequently to click (in ms)

mouseButton="left"
#Which mouse button to press ('left','middle','right')

clickAmount=100
#How many times you want the autoclclicker to click (any positive number)

infinite=-1
#Weather or not the autoclicker works infinitely (1 for true, -1 for false)

startKey='pageup'
#Hotkey to start the autoclicker

stopKey='pagedown'
#Hotkey to stop the autoclcliker

"""__________________________________UI______________________________________"""

mainWin = Tk()

def start():
    global isRunning
    isRunning=1
    mainWin.destroy()
    OPos.destroy()
    clickFreq.destroy()
def updateValue():
    global outputPos
    outputPos=setOutputPos
    oposValue.set('Current: '+ outputPos)
    global clickFrequency
    clickFrequency=setClickFreq
    clickFreqValue.set('Current: '+ clickFrequency +'ms')

#intial stuff
title= Label(mainWin, text= 'Auto Clicker v1.1')
title.config(font=(20))
credit= Label(mainWin, text='By Jaden909')
mainWin.geometry("600x600")
startButton = Button(mainWin, text = 'Start Auto Clicker', command = start)
updateValues=Button(mainWin, text='Update Values', command=updateValue)

#OPos Stuff
def changeOutputPos():
    OPos=Tk()
    global setOutputPos
    setOutputPos=simpledialog.askstring(title="Change Mouse Position Output", prompt="Should the mouse position be outputted? (true or false)")
    OPos.destroy()
    OPos.mainloop()
oposValue=StringVar()
oposValue.set('Current:')
changeOPosButton = Button(mainWin, text = 'Change mouse position output', command = changeOutputPos)
outputPosValue=Label(mainWin, textvariable=oposValue)

#clickFreq Stuff
def changeClickFreq():
    clickFreq=Tk()
    global setClickFreq
    setClickFreq=simpledialog.askstring(title="Change Click Frequency", prompt="How fast should the autoclicker click? (ms)")
    clickFreq.destroy()
    clickFreq.mainloop()
clickFreqValue=StringVar()
clickFreqValue.set('Current:')
changeClickFreqButton = Button(mainWin, text = 'Change Click Frequency', command = changeClickFreq)
clickFreqValueLabel=Label(mainWin, textvariable=clickFreqValue)

title.pack()
credit.pack()
startButton.pack()
changeOPosButton.pack()                             
outputPosValue.pack()
changeClickFreqButton.pack()
clickFreqValueLabel.pack()
updateValues.pack()
mainWin.mainloop()

"""__________________________________Code____________________________________"""

def trackMouse():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY=pyautogui.position()
    global clicks
    clicks=clicks-infinite

print('Auto Clicker v1.0.2.1 By Jaden909')
print('Press pageup to start the autoclicker and pagedown to stop it')
print('The EXE version uses the default settings. You need the python version to change the settings')

clickFrequency=int(clickFrequency)

while clicks<clickAmount+1: 
    if keyboard.is_pressed(startKey):
        isRunning=1
    if keyboard.is_pressed(stopKey):
        isRunning=0
    if clicks==clickAmount:
            clicks=0
            isRunning=0
    if isRunning==1:
        trackMouse()
        _click(currentMouseX,currentMouseY,mouseButton)
        if outputPos=='true':
                print(currentMouseX,currentMouseY)  
        else: pass
        time.sleep (clickFrequency/1000)

        
