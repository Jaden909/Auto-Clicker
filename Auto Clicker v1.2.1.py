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
        title= Label(mainWin, text= 'Auto Clicker v1.2.1')
        title.config(font=(20))
        credit= Label(mainWin, text='By Jaden909')
        mainWin.geometry("600x700")
        startButton = Button(mainWin, text = 'Start Auto Clicker', command = start)
        updateValues=Button(mainWin, text='Update Values', command=updateValue)
        changelog=Label(mainWin, text= """Patch Notes:
         v1.2.1 Window can now be opened with a key seperate from the stop key, 1.2 bug fixes""", wraplength=520)
        global clickFrequency
        clickFrequency=str(clickFrequency)
        global clickAmount
        clickAmount=str(clickAmount)
        NOTE=Label(mainWin, text="NOTE: Press ESC to bring this window back up after it is closed", wraplength=520)
        

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

        #mouseButton stuff
        def changeMouseButton():
            mouseButtonWin=Tk()
            global setMouseButton
            setMouseButton=simpledialog.askstring(title="Change Mouse Button", prompt="Which button should the autoclicker click with? (left, middle, right)")
            mouseButtonWin.destroy()
            mouseButtonWin.mainloop()
        mouseButtonValue=StringVar()
        mouseButtonValue.set('Current: ' + mouseButton)
        changeMouseButtonButton = Button(mainWin, text = 'Change Mouse Button', command = changeMouseButton)
        mouseButtonValueLabel=Label(mainWin, textvariable=mouseButtonValue)

        #clickTimes Stuff
        def changeClickTimes():
            clickTimesWin=Tk()
            global setClickTimes
            setClickTimes=simpledialog.askstring(title="Change Click Times", prompt="How many times should the autoclicker click?")
            clickTimesWin.destroy()
            clickTimesWin.mainloop()
        clickTimesValue=StringVar()
        clickTimesValue.set('Current: ' + clickAmount+' times')
        changeClickTimesButton = Button(mainWin, text = 'Change Click Times', command = changeClickTimes)
        clickTimesValueLabel=Label(mainWin, textvariable=clickTimesValue)

        #infinite Stuff
        def changeinfinite():
            infiniteWin=Tk()
            global setinfinite
            setinfinite=simpledialog.askstring(title="Infinite Mode", prompt="Should the autoclicker run infinitely? (MAY BE DANGEROUS)")
            infiniteWin.destroy()
            infiniteWin.mainloop()
        infiniteValue=StringVar()
        infiniteValue.set('Current: ' + infiniteBool)
        changeinfiniteButton = Button(mainWin, text = 'Infinite Mode', command = changeinfinite)
        infiniteValueLabel=Label(mainWin, textvariable=infiniteValue)
        
        #startKey Stuff
        def changestartKey():
            startKeyWin=Tk()
            global setstartKey
            setstartKey=simpledialog.askstring(title="Change Start Key", prompt="What key should start the autoclicker?")
            startKeyWin.destroy()
            startKeyWin.mainloop()
        startKeyValue=StringVar()
        startKeyValue.set('Current: ' + startKey)
        changestartKeyButton = Button(mainWin, text = 'Change Start Key', command = changestartKey)
        startKeyValueLabel=Label(mainWin, textvariable=startKeyValue)

        #stopKey Stuff
        def changestopKey():
            stopKeyWin=Tk()
            global setstopKey
            setstopKey=simpledialog.askstring(title="Change Stop Key", prompt="What key should stop the autoclicker?")
            stopKeyWin.destroy()
            stopKeyWin.mainloop()
        stopKeyValue=StringVar()
        stopKeyValue.set('Current: ' + stopKey)
        changestopKeyButton = Button(mainWin, text = 'Change Stop Key', command = changestopKey)
        stopKeyValueLabel=Label(mainWin, textvariable=stopKeyValue)

        title.pack()
        credit.pack()
        startButton.pack()
        changeOPosButton.pack()                             
        outputPosValue.pack()
        changeClickFreqButton.pack()
        clickFreqValueLabel.pack()
        changeMouseButtonButton.pack()
        mouseButtonValueLabel.pack()
        changeClickTimesButton.pack()
        clickTimesValueLabel.pack()
        changeinfiniteButton.pack()
        infiniteValueLabel.pack()
        changestartKeyButton.pack()
        startKeyValueLabel.pack()
        changestopKeyButton.pack()
        stopKeyValueLabel.pack()
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