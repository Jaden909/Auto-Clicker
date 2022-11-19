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
infiniteBool='false'

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
# v1.1.3 Added ability to change the mouse button (via UI)
# v1.2 Added ability to change click times, infinite mode, start key, and stop key (via UI), not changing all settings and attempting to update values no longer throws a error and works as expected, increased window size to accomodate new UI elements
# v1.2.1 Window can now be opened with a key seperate from the stop key, 1.2 bug fixes
# v1.2.2 Finally got the exit button to work somehow

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

winKey='esc'
#Hotkey to open the main window

clickMode='click'
#How the autoclicker clicks (click or hold)[NOT YET IMPLEMENTED]

clickHoldTIme='10'
#How long to hold click (hold mode only)[NOT YET IMPLEMENTED]

"""_________________________________________________________________________________UI________________________________________________________________________________"""

def mainWindow():
        mainWin = Tk()
        Tk.title(mainWin,'Auto Clicker v1.2.2.1')
        def start():
            global isRunning
            isRunning=1
            mainWin.destroy()
        def exitScript():
            exit()  
        def updateValue():
            if 'setOutputPos' in globals():
                global outputPos
                outputPos=setOutputPos
                oposValue.set('Current: '+ outputPos)
            if 'setClickFreq' in globals():
                global clickFrequency
                clickFrequency=setClickFreq
                clickFreqValue.set('Current: '+ clickFrequency +'ms')
            if 'setMouseButton' in globals():
                global mouseButton
                mouseButton=setMouseButton
                mouseButtonValue.set('Current: '+mouseButton)
            if 'setClickTimes' in globals():
                global clickAmount
                clickAmount=setClickTimes
                clickTimesValue.set('Current: '+clickAmount+ ' times')
            if 'setinfinite' in globals():
                global infiniteBool
                infiniteBool=setinfinite
                infiniteValue.set('Current: '+infiniteBool)
            if 'setstartKey' in globals():
                global startKey
                startKey=setstartKey
                startKeyValue.set('Current: '+startKey)
            if 'setstopKey' in globals():
                global stopKey
                stopKey=setstopKey
                stopKeyValue.set('Current: '+stopKey)
            
        #intial stuff
        title= Label(mainWin, text= 'Auto Clicker v1.2.2.1')
        title.config(font=(20))
        credit= Label(mainWin, text='By Jaden909')
        mainWin.geometry("600x700")
        startButton = Button(mainWin, text = 'Start Auto Clicker', command = start)
        updateValues=Button(mainWin, text='Update Values', command=updateValue)
        changelog=Label(mainWin, text= """Patch Notes:
         v1.2.2.1 Window has proper title now""", wraplength=520)
        NOTE=Label(mainWin, text="NOTE: Press ESC to bring this window back up after it is closed", wraplength=520)
        exitButton=Button(mainWin, text='Exit',command=exitScript)

        def create(Title:str,Setting):    
            
            Value=StringVar()
            Value.set(f'Current: {Setting}')
            _Button = Button(mainWin, text = Title, command = change)
            _Label=Label(mainWin, textvariable=Value)
            _Button.pack()
            _Label.pack()
            return Value
        def change(Title:str,Prompt:str):
            __=simpledialog.askstring(title=Title, prompt=Prompt)
            return __
        global outputPos,clickFrequency,mouseButton,clickTimes,infinite,startKey,stopKey    
        title.pack()
        credit.pack()
        startButton.pack()
        oposValue=create('Change Mouse Position Output',outputPos)
        setOutputPos=change('Change Mouse Position Output','Should the mouse position be outputted? (true or false)')   
        clickFreqValue=create('Change Click Frequency',clickFrequency)
        setClickFreq=change('Change Click Frequency','How fast should the autoclicker click? (ms)')
        mouseButtonValue=create('Change Mouse Button',mouseButton)
        setMouseButton=change('Change Mouse Button','Which button should the autoclicker click with? (left, middle, right)')
        clickTimesValue=create('Change Click Times',clickTimes)
        setClickTimes=change('Change Click Times','How many times should the autoclicker click?')
        infiniteValue=create('Infinite Mode',infinite)
        setinfinite=change('Infinite Mode','Should the autoclicker run infinitely? (MAY BE DANGEROUS)')
        startKeyValue=create('Change Start Key',startKey)
        setstartKey=change('Change Start Key','What key should start the autoclicker?')
        stopKeyValue=create('Change Stop Key',stopKey)
        setstopKey=change('Change Stop Key','What key should stop the autoclicker?')
        updateValues.pack()
        exitButton.pack()
        changelog.pack()
        NOTE.pack()
        mainWin.mainloop()

"""___________________________________________________________________________________Code_____________________________________________________________________________"""

mainWindow()

def trackMouse():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY=pyautogui.position()
    global clickTimes
    if infiniteBool=='true':
        infinite=1
    else:
        infinite=-1    
    clickTimes=clickTimes-infinite
clickTimes=int(clickTimes)
clickAmount=int(clickAmount)
while clickTimes<clickAmount+1: 
    clickFrequency=int(clickFrequency)
    if keyboard.is_pressed(startKey):
        isRunning=1
    if keyboard.is_pressed(stopKey):
        isRunning=0
        clickFrequency=int(clickFrequency)
    if keyboard.is_pressed(winKey):
        mainWindow()
    if clickTimes==clickAmount:
        clickTimes=0
        isRunning=0
        mainWindow()    
    if isRunning==1:
        trackMouse()
        currentMouseX=int(currentMouseX)
        currentMouseY=int(currentMouseY)
        clickFrequency=int(clickFrequency)
        pyautogui.click(currentMouseX,currentMouseY,button=mouseButton,interval=clickFrequency/1000)
        if outputPos=='true':
            print(currentMouseX,currentMouseY)  
        else: pass
#271 lines