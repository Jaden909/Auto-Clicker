import ctypes
import ctypes.wintypes
import pyautogui
from pyautogui import LEFT, MIDDLE, RIGHT
import keyboard
from tkinter import *
from tkinter import simpledialog
#Required modules for auto clicker to work
global isRunning
isRunning=0
#Weather or not the autoclicker is running
clickTimes=0
#Number of times the 'trackMouse' function has been called

"""______________________________________________________________________________Changelog_____________________________________________________________________________"""

# v0.1.1 Added setting to turn mouse position output on or off
# v0.2 Added ability to change click frequency
# v1.0 Added hotkey for turning the autoclclicker on or off
# v1.0.1 Auto clicker automatically resets clicks when click amount is reached so it can be run again without rerunning the program
# v1.0.2 Added ability to change hotkey for starting/stopping 
# v1.0.2.1 Made slightly more user friendly
# v1.1 Added basic UI
# v1.1.0.1 Minor bug fixes
# v1.1.1 Improved UI and window now returns when the autoclicker is stopped
# v1.1.1.1 Minor code optimizations (I actually use pyautogui's functions now)
# v1.1.2 clickFrequency now only affects click function instead of entire code preventing code from slowing code down if there is a slow click frequency
# v1.1.2.1 Changed from IDLE code editor to Visual Studio Code
# v1.1.2.2 Removed useless line of code causing an error

# Planned feature: Ability to manually select coordinates for autoclicker
# Planned feature: Ability to hold down click

"""______________________________________________________________________________Settings______________________________________________________________________________"""

outputPos='true'
#Weather or not the autoclicker should output the mouse position in the console

clickFrequency=100
#How frequently to click (in ms)

mouseButton="left"
#Which mouse button to press ('left','middle','right')

clickAmount=1000
#How many times you want the autoclclicker to click (any positive number)

infinite=-1
#Weather or not the autoclicker works infinitely (1 for true, -1 for false)

startKey='pageup'
#Hotkey to start the autoclicker

stopKey='pagedown'
#Hotkey to stop the autoclcliker

"""_________________________________________________________________________________UI________________________________________________________________________________"""

def mainWindow():
        mainWin = Tk()

        def start():
            global isRunning
            isRunning=1
            mainWin.destroy()
            
        def updateValue():
            global outputPos
            outputPos=setOutputPos
            oposValue.set('Current: '+ outputPos)
            global clickFrequency
            clickFrequency=setClickFreq
            clickFreqValue.set('Current: '+ clickFrequency +'ms')
       

        #intial stuff
        title= Label(mainWin, text= 'Auto Clicker v1.1.2.2')
        title.config(font=(20))
        credit= Label(mainWin, text='By Jaden909')
        mainWin.geometry("600x600")
        startButton = Button(mainWin, text = 'Start Auto Clicker', command = start)
        updateValues=Button(mainWin, text='Update Values', command=updateValue)
        changelog=Label(mainWin, text= """Changelog:
         v1.1.2.2 Removed useless line of code causing an error""", wraplength=520)
        hotkeys=Label(mainWin, text= 'Press pageup to start the autoclicker and pagedown to stop it')
        global clickFrequency
        clickFrequency=str(clickFrequency)
        NOTE=Label(mainWin, text="NOTE: There are more options that can be changed, I just haven't added them to the ui yet", wraplength=520)
        

        #OPos Stuff
        def changeOutputPos():
            OPos=Tk()
            global setOutputPos
            setOutputPos=simpledialog.askstring(title="Change Mouse Position Output", prompt="Should the mouse position be outputted? (true or false)")
            OPos.destroy()
            OPos.mainloop()
        oposValue=StringVar()
        global outputPos
        oposValue.set('Current: '+ outputPos)
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
        clickFreqValue.set('Current: ' + clickFrequency +'ms')
        changeClickFreqButton = Button(mainWin, text = 'Change Click Frequency', command = changeClickFreq)
        clickFreqValueLabel=Label(mainWin, textvariable=clickFreqValue)

        title.pack()
        credit.pack()
        hotkeys.pack()
        startButton.pack()
        changeOPosButton.pack()                             
        outputPosValue.pack()
        changeClickFreqButton.pack()
        clickFreqValueLabel.pack()
        updateValues.pack()
        changelog.pack()
        NOTE.pack()
        mainWin.mainloop()

"""___________________________________________________________________________________Code_____________________________________________________________________________"""

mainWindow()

def trackMouse():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY=pyautogui.position()
    global clickTimes
    clickTimes=clickTimes-infinite

while clickTimes<clickAmount+1: 
    clickFrequency=int(clickFrequency)
    if keyboard.is_pressed(startKey):
        isRunning=1
    if keyboard.is_pressed(stopKey):
        isRunning=0
        clickFrequency=int(clickFrequency)
    if clickTimes==clickAmount:
        clickTimes=0
        isRunning=0
    if isRunning ==0:
        mainWindow()    
    if isRunning==1:
        trackMouse()
        currentMouseX=int(currentMouseX)
        currentMouseY=int(currentMouseY)
        pyautogui.click(currentMouseX,currentMouseY,button=mouseButton,interval=clickFrequency/1000)
        if outputPos=='true':
                print(currentMouseX,currentMouseY)  
        else: pass
        

