import pyautogui
import keyboard
from customtkinter import *
#Required modules for auto clicker to work
global isRunning
isRunning=0
#Weather or not the autoclicker is running
clickTimes=0
#Number of times the 'trackMouse' function has been called
infiniteBool='false'
colorMain,colorMainOutline,colorMainHover='#1F6AA5','',''
colorNeg,colorNegOutline,colorNegHover='#c44c43','','#61221e'
colorPos,colorPosOutline,colorPosHover='#1c9e39','#0a3814','#136926'

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

outputPos=True
#Weather or not the autoclicker should output the mouse position in the console

clickFrequency=100
#How frequently to click (in ms)

mouseButton="left"
#Which mouse button to press ('left','middle','right')

clickAmount=1000
#How many times you want the autoclclicker to click (any positive number)

infinite=False
#Weather or not the autoclicker works infinitely

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
        mainWin = CTk()
        mainWin.config(cursor='tcross')
        CTk.title(mainWin,'Auto Clicker v1.3')
        def start():
            global isRunning
            isRunning=1
            mainWin.destroy()
        def exitScript():
            exit()  
        
        def setTrue(strvar:StringVar,settingVar):
            
            
            global outputPos,infinite
            if settingVar=='outputPos':
                outputPos=True
            if settingVar=='infinite':
                infinite=True
            
        def setFalse(strvar:StringVar,settingVar):
            
            global outputPos,infinite
            if settingVar=='outputPos':
                outputPos=False
            if settingVar=='infinite':
                infinite=False
        def openSettings():
            settingsWin=CTk()
            settingsWin.config(cursor='tcross')
            settingsWin.geometry('630x450')
            def settingsExit():
                updateValue()
                settingsWin.destroy()
            def updateValue():
                if setClickFreq.get()!='':
                    global clickFrequency
                    clickFrequency=setClickFreq.get()
                    clickFreqValue.set('Current: '+ clickFrequency +'ms')
                    clickFreqValueLabel.configure(text=f'Current: {clickFrequency}ms')
                #if setMouseButton.get()!='':
                #    global mouseButton
                #    mouseButton=setMouseButton.get()
                #    mouseButtonValue.set('Current: '+mouseButton)
                #    mouseButtonValueLabel.configure(text=f'Current: {mouseButton}')
                if setClickTimes.get()!='':
                    global clickAmount
                    clickAmount=setClickTimes.get()
                    print(clickAmount)
                    clickTimesValue.set(f'Current: {clickAmount} times')
                    clickTimesValueLabel.configure(text=f'Current: {clickAmount} times')
                if setstartKey.get()!='':
                    global startKey
                    startKey=setstartKey.get()
                    startKeyValue.set(f'Current: {startKey}')
                    startKeyValueLabel.configure(text=f'Current: {startKey}')
                if setstopKey.get()!='':
                    global stopKey
                    stopKey=setstopKey.get()
                    stopKeyValue.set(f'Current: {stopKey}')
                    stopKeyValueLabel.configure(text=f'Current: {stopKey}')
                outputPosValue.configure(text=f'Current: {str(outputPos)}')
                infiniteValueLabel.configure(text=f'Current: {str(infinite)}')
            def advSettings():
                advSettingsWin=CTk()
                tempLabel=CTkLabel(master=advSettingsWin,text='Coming Soon',text_font=('roboto',30))
                tempLabel.pack()
                advSettingsWin.mainloop()
            frame=CTkFrame(master=settingsWin)
            frame.grid(padx=5,pady=5,row=0,column=0)
            frame1=CTkFrame(master=settingsWin)
            frame1.grid(padx=5,pady=5,row=1,column=0)
            frame2=CTkFrame(master=settingsWin)
            frame2.grid(padx=5,pady=5,row=0,column=1)
            frame3=CTkFrame(master=settingsWin)
            frame3.grid(padx=5,pady=5,row=1,column=1)
            frame4=CTkFrame(master=settingsWin)
            frame4.grid(padx=5,pady=5,row=0,column=2)
            frame5=CTkFrame(master=settingsWin)
            frame5.grid(padx=5,pady=5,row=1,column=2)
            frame5.grid_propagate(False)
            frame4.grid_propagate(False)
            frame3.grid_propagate(False)
            frame2.grid_propagate(False)
            frame1.grid_propagate(False)
            frame.grid_propagate(False)

            
            #OPos Stuff (grid 0)   
            global setOutputPos,outputPos    
            opsTrue=CTkButton(frame,text='True',command=lambda: setTrue(oposValue,'outputPos'),fg_color=colorMain)
            opsFalse=CTkButton(frame,text='False',command=lambda: setFalse(oposValue,'outputPos'),fg_color=colorMain)    
            oposValue=StringVar()
            oposValue.set('Current: True')
            outputPosValue=CTkLabel(frame, text=f'Current: {str(outputPos)}',text_font=('roboto',15))
            oposLabel=CTkLabel(frame,text='Output Position',text_font=('roboto',15))
            print(opsTrue.fg_color)
            #clickFreq Stuff
            setClickFreq=CTkEntry(frame1,width=150,placeholder_text='Click Frequency...') 
            clickFreqValue=StringVar()
            clickFreqValue.set(f'Current: {clickFrequency}ms')
            clickFreqValueLabel=CTkLabel(frame1, text=clickFreqValue.get(),text_font=('roboto',15))
            clickFreqLabel=CTkLabel(frame1,text='Click Frequency',text_font=('roboto',15))

            #mouseButton stuff
            #setMouseButton=CTkEntry(frame,width=150,placeholder_text='') 
            #mouseButtonValue=StringVar()
            #mouseButtonValue.set('Current: ' + mouseButton)
            #mouseButtonValueLabel=CTkLabel(frame, text=mouseButtonValue.get(),text_font=('roboto',15))

            #clickTimes Stuff
            setClickTimes=CTkEntry(frame2,width=150,placeholder_text='Click Times...') 
            clickTimesValue=StringVar()
            clickTimesValue.set(f'Current: {clickAmount} times')
            clickTimesValueLabel=CTkLabel(frame2, text=clickTimesValue.get(),text_font=('roboto',15))
            clickTimesLabel=CTkLabel(frame2,text='Click Times',text_font=('roboto',15))

            #infinite Stuff (grid 0)
            infTrue=CTkButton(frame3,text='True',command=lambda: setTrue(infiniteValue,'infinite'),fg_color=colorMain)
            infFalse=CTkButton(frame3,text='False',command=lambda: setFalse(infiniteValue,'infinite'),fg_color=colorMain) 
            infiniteValue=StringVar()
            infiniteValue.set('Current: False')
            infiniteValueLabel=CTkLabel(frame3, text=f'Current: {str(infinite)}',text_font=('roboto',15))
            infiniteLabel=CTkLabel(frame3,text='Infinite',text_font=('roboto',15))
            
            #startKey Stuff
            setstartKey=CTkEntry(frame4,width=150,placeholder_text='Start Key...') 
            startKeyValue=StringVar()
            startKeyValue.set('Current: ' + startKey)
            startKeyValueLabel=CTkLabel(frame4, text=startKeyValue.get(),text_font=('roboto',15))
            startKeyLabel=CTkLabel(frame4,text='Start Hotkey',text_font=('roboto',15))

            #stopKey Stuff
            setstopKey=CTkEntry(frame5,width=150,placeholder_text='Stop Key...') 
            stopKeyValue=StringVar()
            stopKeyValue.set('Current: ' + stopKey)
            stopKeyValueLabel=CTkLabel(frame5, text=stopKeyValue.get(),text_font=('roboto',15))
            stopKeyLabel=CTkLabel(frame5,text='Stop Hotkey',text_font=('roboto',15))

            updateValues=CTkButton(settingsWin, text='Update Values', command=updateValue,border_color=colorPosOutline,fg_color=colorPos,border_width=1,hover_color=colorPosHover)
            settingsExitButton=CTkButton(settingsWin,text='Exit',command=settingsExit,border_color=colorNegOutline,fg_color=colorNeg,border_width=1,hover_color=colorNegHover)
            advSettingsButton=CTkButton(settingsWin,text='Advanced Settings',command=advSettings)

            oposLabel.grid(row=0,column=0,padx=30,pady=10)
            outputPosValue.grid(row=1,column=0,padx=30,pady=10)
            opsTrue.grid(row=2,column=0,padx=30,pady=10)
            opsFalse.grid(row=3,column=0,padx=30,pady=10)
            clickFreqLabel.grid(row=1,column=0,padx=30,pady=10)
            clickFreqValueLabel.grid(row=2,column=0,padx=30,pady=10)
            setClickFreq.grid(row=3,column=0,padx=30,pady=10)
            #mouseButtonValueLabel.grid(row=2,column=1)
            clickTimesLabel.grid(row=3,column=0,padx=30,pady=10)
            clickTimesValueLabel.grid(row=4,column=0,padx=10,pady=10)
            setClickTimes.grid(row=5,column=0,padx=15,pady=10)
            infiniteLabel.grid(row=0,column=0,padx=30,pady=10)
            infiniteValueLabel.grid(row=1,column=0,padx=30,pady=10)
            infTrue.grid(row=2,column=0,padx=30,pady=10)
            infFalse.grid(row=3,column=0,pady=10)
            startKeyLabel.grid(row=7,column=0,padx=30,pady=10)
            startKeyValueLabel.grid(row=8,column=0,padx=30,pady=10)
            setstartKey.grid(row=9,column=0,padx=30,pady=10)
            stopKeyLabel.grid(row=9,column=0,padx=30,pady=10)
            stopKeyValueLabel.grid(row=10,column=0,padx=20,pady=10)
            setstopKey.grid(row=11,column=0,padx=30,pady=10)
            
            updateValues.grid(row=4,column=2)
            settingsExitButton.grid(row=4,column=0)
            advSettingsButton.grid(row=4,column=1)
            settingsWin.mainloop()
        #intial stuff
        mainFrame=CTkFrame(master=mainWin,bg_color="gray")
        mainFrame.pack(fill='both',padx=20,pady=15)
        title= CTkLabel(master=mainFrame, text= 'Auto Clicker v1.3',text_font=('roboto',30))
        credit= CTkLabel(master=mainFrame, text='By Jaden909',text_font=('roboto',18))
        mainWin.geometry("550x300")
        startButton = CTkButton(master=mainFrame, text = 'Start Auto Clicker', command = start,fg_color=colorPos,hover_color=colorPosHover)
        changelog=CTkLabel(master=mainFrame, text= """Patch Notes:
         v1.3 Rewrote UI to be WAY better""", wraplength=520)
        global clickFrequency
        clickFrequency=str(clickFrequency)
        global clickAmount
        clickAmount=str(clickAmount)
        NOTE=CTkLabel(master=mainFrame, text="NOTE: Press ESC to bring this window back up after it is closed", wraplength=520)
        exitButton=CTkButton(master=mainFrame, text='Exit',command=exitScript,fg_color=colorNeg,hover_color=colorNegHover)
        settingsButton=CTkButton(master=mainFrame,text='Settings',command=openSettings,fg_color=colorMain)
        setinfinite=None
        title.pack()
        credit.pack()
        startButton.pack(pady=5)  
        settingsButton.pack(pady=5)
        exitButton.pack(pady=5)
        changelog.pack(pady=5)
        NOTE.pack()
        mainWin.mainloop()

"""___________________________________________________________________________________Code_____________________________________________________________________________"""

mainWindow()

def trackMouse():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY=pyautogui.position()
    global clickTimes
    if infinite:
        clickTimes=clickTimes+1
    else:  
        clickTimes=clickTimes-1
while int(clickTimes)<int(clickAmount)+1: 
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
        pyautogui.click(currentMouseX,currentMouseY,button=mouseButton,interval=int(clickFrequency)/1000)
        if outputPos==True:
            print(currentMouseX,currentMouseY)  
        else: pass
