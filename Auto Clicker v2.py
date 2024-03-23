import pyautogui,keyboard,time,json
from customtkinter import *
import tkinter
#Required modules for auto clicker to work
isRunning=False
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
# v1.3 Rewrote UI to be way better
# v1.3.1 I forgot, probably added the hold function or something

# Planned feature: Ability to manually select coordinates for autoclicker
# Planned feature: Ability to hold down click

#file=tkinter.filedialog.askopenfile(mode='r',initialdir='.')
#print(file.read())
"""______________________________________________________________________________Settings______________________________________________________________________________"""

outputPos=True
#Weather or not the autoclicker should output the mouse position in the console (Main Settings Menu)

clickFrequency=100
#How frequently to click (in ms) (Main Settings Menu)

mouseButton='left'
#Which mouse button to press ('left','middle','right') (Advanced Setting) 4 X

clickAmount=1000
#How many times you want the autoclclicker to click (any positive number) (Main Settings Menu)

infinite=False
#Weather or not the autoclicker works infinitely (Main Settings Menu)

startKey='pageup'
#Hotkey to start the autoclicker (Main Settings Menu)

stopKey='pagedown'
#Hotkey to stop the autoclcliker (Main Settings Menu)

winKey='esc'
#Hotkey to open the main window (Advanced Setting) 2 X

clickMode='Click'
#How the autoclicker clicks (click or hold) (Advanced Setting) X 1

clickHoldTime=1000
#How long to hold click (hold mode only) (Advanced Setting) X 1

mouseX,mouseY=0,0
#Used to manually position mouse (Advanced Setting) 3

config={'outputPos':outputPos,'clickFrequency':clickFrequency,'mouseButton':mouseButton,'clickAmount':clickAmount,'infinite':infinite,'startKey':startKey,'stopKey':stopKey,'winKey':winKey,'clickMode':clickMode,'clickHoldTime':clickHoldTime,'mouseX':mouseX,'mouseY':mouseY}
#Used to save and load settings
"""_________________________________________________________________________________UI________________________________________________________________________________"""

def mainWindow():
        mainWin = CTk()
        mainWin.config(cursor='tcross')
        CTk.title(mainWin,'Auto Clicker v2')
        def start():
            global isRunning
            isRunning=1
            mainWin.destroy()
        def exitScript():
            exit() 
        
        


        def openSettings():
            settingsWin=CTk()
            settingsWin.title('Settings')
            settingsWin.config(cursor='tcross')
            settingsWin.geometry('630x450')
            def settingsExit():
                updateValue()
                settingsWin.destroy()
            
            def updateValue():
                global clickFrequency,clickAmount,startKey,stopKey,clickMode,cm,clickHoldTime,ct,infinite,winKey,mouseButton,manual,mouseY,mouseX
                if setClickFreq.get()!='':
                    clickFrequency=setClickFreq.get()
                    clickFreqValue.set('Current: '+ clickFrequency +'ms')
                    clickFreqValueLabel.configure(text=f'Current: {clickFrequency}ms')
                #if setMouseButton.get()!='':
                #    global mouseButton
                #    mouseButton=setMouseButton.get()
                #    mouseButtonValue.set('Current: '+mouseButton)
                #    mouseButtonValueLabel.configure(text=f'Current: {mouseButton}')
                if setClickTimes.get()!='':
                    clickAmount=setClickTimes.get()
                    #print(clickAmount)
                    clickTimesValue.set(f'Current: {clickAmount} times')
                    clickTimesValueLabel.configure(text=f'Current: {clickAmount} times')
                if setstartKey.get()!='':
                    startKey=setstartKey.get()
                    startKeyValue.set(f'Current: {startKey}')
                    startKeyValueLabel.configure(text=f'Current: {startKey}')
                
                if setstopKey.get()!='':
                    stopKey=setstopKey.get()
                    stopKeyValue.set(f'Current: {stopKey}')
                    stopKeyValueLabel.configure(text=f'Current: {stopKey}')
                outputPos=True if outputPosv.get() else False
                infinite=True if infinitev.get() else False
                inf.configure(text=f'{infinite}')
                ops.configure(text=f'{outputPos}')
                #Gave up on making this not error
                try:
                    if setwinKey.get()!='':
                        winKey=setwinKey.get()
                        winKeyValue.set(f'Current: {winKey}')
                        winKeyValueLabel.configure(text=f'Current: {winKey}')
                    clickMode=clickModeVar.get()
                    cm.configure(text=f'Current: {str(clickMode)}')
                    if ct.get()!='':
                        clickHoldTime=int(ct.get())
                    if mbValue.get() in ['left','middle','right']:
                        mouseButton=mbValue.get()
                    if mpX.get()!='' and mpY.get()!='' :
                        #manual=True
                        mouseX=int(mpX.get())
                        mouseY=int(mpY.get())

                    else:
                        #manual=False
                        mouseX,mouseY=0
                    
                except:
                    pass
                #outputPosValue.configure(text=f'Current: {str(outputPos)}')
                #infiniteValueLabel.configure(text=f'Current: {str(infinite)}')
            def saveConfig():
                updateValue()
                config={'outputPos':outputPos,'clickFrequency':clickFrequency,'mouseButton':mouseButton,'clickAmount':clickAmount,'infinite':infinite,'startKey':startKey,'stopKey':stopKey,'winKey':winKey,'clickMode':clickMode,'clickHoldTime':clickHoldTime,'mouseX':mouseX,'mouseY':mouseY}
                print(config)
                with open(tkinter.filedialog.asksaveasfilename(initialdir='.',defaultextension='.json',filetypes=[('json','.json')]),'w') as f:
                    json.dump(config,f)
            def advSettings():
                def advSettingsExit():
                    updateValue()
                    advSettingsWin.destroy()
                #def cmClick():
                #    global clickMode
                #    clickMode='Click'
                #    cmValue.set(clickMode)
                #    cmValueLab.configure(text=f'Current: {str(clickMode)}')
                #def cmHold():
                #    global clickMode
                #    clickMode='Hold'
                #    cmValue.set(clickMode)
                #    cmValueLab.configure(text=f'Current: {str(clickMode)}')
                advSettingsWin=CTk()
                advSettingsWin.title('Advanced Settings')
                advSettingsWin.geometry('420x450')
                aframe=CTkFrame(master=advSettingsWin)
                aframe.grid(padx=5,pady=5,row=0,column=0)
                aframe1=CTkFrame(master=advSettingsWin)
                aframe1.grid(padx=5,pady=5,row=1,column=0)
                aframe2=CTkFrame(master=advSettingsWin)
                aframe2.grid(padx=5,pady=5,row=0,column=1)
                aframe3=CTkFrame(master=advSettingsWin)
                aframe3.grid(padx=5,pady=5,row=1,column=1)
                aframe3.grid_propagate(False)
                aframe2.grid_propagate(False)
                aframe1.grid_propagate(False)
                aframe.grid_propagate(False)

                advSettingsExitButton=CTkButton(advSettingsWin,text='Exit',command=advSettingsExit,border_color=colorNegOutline,fg_color=colorNeg,border_width=1,hover_color=colorNegHover)
                settingsSaveButton=CTkButton(advSettingsWin,text='Save Config',command=saveConfig,border_color=colorPosOutline,fg_color=colorPos,border_width=1,hover_color=colorPosHover)

                global clickMode,clickModeVar,cm,ct,setwinKey,winKeyValue,winKeyLabel,winKeyValueLabel,mbValue,mpY,mpX
                clickModeVar=StringVar(value=clickMode)
                #clickTimeVar=StringVar(value=clickHoldTime)
                cm=CTkSwitch(aframe,text=f'Current: {str(clickMode)}',variable=clickModeVar,command=updateValue,offvalue='click',onvalue='hold')
                ct=CTkEntry(aframe,placeholder_text='Click Hold Time...')

                mbValue=StringVar()
                mbLabel=CTkLabel(aframe3,text='Mouse Button')
                mbButt=CTkSegmentedButton(aframe3,values=['left','middle','right'],variable=mbValue)

                mpLabel=CTkLabel(aframe1,text='Manually Set Mouse Position')
                mpX=CTkEntry(aframe1,placeholder_text='Mouse position X...')
                mpY=CTkEntry(aframe1,placeholder_text='Mouse position Y...')
                #cmTrue=CTkButton(aframe,text='Hold',command=cmHold,fg_color=colorMain)
                #cmFalse=CTkButton(aframe,text='Click',command=cmClick,fg_color=colorMain)    
                #cmValue=StringVar()
                #cmValue.set('Current: Click')
                #cmValueLab=CTkLabel(aframe, text=f'Current: {str(clickMode)}',font=('roboto',15))
                cmLabel=CTkLabel(aframe,text='Click Mode',font=('roboto',15))
                
                cmLabel.grid(row=0,column=0,padx=30,pady=10)
                setwinKey=CTkEntry(aframe2,width=150,placeholder_text='Window Key...') 
                winKeyValue=StringVar()
                winKeyValue.set(f'Current: {winKey}')
                winKeyValueLabel=CTkLabel(aframe2, text=winKeyValue.get(),font=('roboto',15))
                winKeyLabel=CTkLabel(aframe2,text='Window Hotkey',font=('roboto',15))
                #cmValueLab.grid(row=1,column=0,padx=30,pady=10)
                #cmTrue.grid(row=2,column=0,padx=30,pady=10)
                #cmFalse.grid(row=3,column=0,padx=30,pady=10)
                cm.grid(row=1,column=0,padx=30,pady=10)
                ct.grid(row=2,column=0,padx=30,pady=10)

                winKeyLabel.grid(row=1,column=0,padx=30,pady=10)
                winKeyValueLabel.grid(row=2,column=0,padx=30,pady=10)
                setwinKey.grid(row=3,column=0,padx=30,pady=10)

                mpLabel.grid(row=1,column=0,padx=20,pady=10)
                mpX.grid(row=2,column=0,padx=30,pady=10)
                mpY.grid(row=3,column=0,padx=30,pady=10)
                
                mbLabel.grid(row=1,column=0,padx=30,pady=10)
                mbButt.grid(row=2,column=0,padx=30,pady=10)

                advSettingsExitButton.grid(row=3,column=0)
                settingsSaveButton.grid(row=3,column=1)
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
           
            #oposValue=StringVar()
            #oposValue.set(f'Current: True')
            global outputPos   
            outputPosv=IntVar(value=outputPos)
            ops=CTkSwitch(frame,text=f'{outputPos}',variable=outputPosv,command=updateValue)
            print(outputPosv.get())
            #opsTrue=CTkButton(frame,text='True',command=lambda: setTrue(oposValue,'outputPos'),fg_color=colorMain)
            #opsFalse=CTkButton(frame,text='False',command=lambda: setFalse(oposValue,'outputPos'),fg_color=colorMain)    
            
            
            #outputPosValue=CTkLabel(frame, text=f'Current: {str(outputPos)}',font=('roboto',15))
            oposLabel=CTkLabel(frame,text='Output Position',font=('roboto',15))
            
            #clickFreq Stuff
            setClickFreq=CTkEntry(frame1,width=150,placeholder_text='Click Frequency...') 
            clickFreqValue=StringVar()
            clickFreqValue.set(f'Current: {clickFrequency}ms')
            clickFreqValueLabel=CTkLabel(frame1, text=clickFreqValue.get(),font=('roboto',15))
            clickFreqLabel=CTkLabel(frame1,text='Click Frequency',font=('roboto',15))

            #mouseButton stuff
            #setMouseButton=CTkEntry(frame,width=150,placeholder_text='') 
            #mouseButtonValue=StringVar()
            #mouseButtonValue.set('Current: ' + mouseButton)
            #mouseButtonValueLabel=CTkLabel(frame, text=mouseButtonValue.get(),font=('roboto',15))

            #clickTimes Stuff
            setClickTimes=CTkEntry(frame2,width=150,placeholder_text='Click Times...') 
            clickTimesValue=StringVar()
            clickTimesValue.set(f'Current: {clickAmount} times')
            clickTimesValueLabel=CTkLabel(frame2, text=clickTimesValue.get(),font=('roboto',15))
            clickTimesLabel=CTkLabel(frame2,text='Click Times',font=('roboto',15))

            #infinite Stuff (grid 0)
            global infinite   
            infinitev=IntVar(value=infinite)
            inf=CTkSwitch(frame3,text=f'{infinite}',variable=infinitev,command=updateValue)
            #infTrue=CTkButton(frame3,text='True',command=lambda: setTrue(infiniteValue,'infinite'),fg_color=colorMain)
            #infFalse=CTkButton(frame3,text='False',command=lambda: setFalse(infiniteValue,'infinite'),fg_color=colorMain) 
            #infiniteValue=StringVar()
            #infiniteValue.set('Current: False')
            #infiniteValueLabel=CTkLabel(frame3, text=f'Current: {str(infinite)}',font=('roboto',15))
            infiniteLabel=CTkLabel(frame3,text='Infinite',font=('roboto',15))
            
            #startKey Stuff
            setstartKey=CTkEntry(frame4,width=150,placeholder_text='Start Key...') 
            startKeyValue=StringVar()
            startKeyValue.set('Current: ' + startKey)
            startKeyValueLabel=CTkLabel(frame4, text=startKeyValue.get(),font=('roboto',15))
            startKeyLabel=CTkLabel(frame4,text='Start Hotkey',font=('roboto',15))

            #stopKey Stuff
            setstopKey=CTkEntry(frame5,width=150,placeholder_text='Stop Key...') 
            stopKeyValue=StringVar()
            stopKeyValue.set('Current: ' + stopKey)
            stopKeyValueLabel=CTkLabel(frame5, text=stopKeyValue.get(),font=('roboto',15))
            stopKeyLabel=CTkLabel(frame5,text='Stop Hotkey',font=('roboto',15))

            updateValues=CTkButton(settingsWin, text='Update Values', command=updateValue,border_color=colorPosOutline,fg_color=colorPos,border_width=1,hover_color=colorPosHover)
            settingsExitButton=CTkButton(settingsWin,text='Exit',command=settingsExit,border_color=colorNegOutline,fg_color=colorNeg,border_width=1,hover_color=colorNegHover)
            advSettingsButton=CTkButton(settingsWin,text='Advanced Settings',command=advSettings)

            oposLabel.grid(row=0,column=0,padx=30,pady=10)
            #outputPosValue.grid(row=1,column=0,padx=30,pady=10)
            ops.grid(row=2,column=0,padx=30,pady=10)
            #opsFalse.grid(row=3,column=0,padx=30,pady=10)
            clickFreqLabel.grid(row=1,column=0,padx=30,pady=10)
            clickFreqValueLabel.grid(row=2,column=0,padx=30,pady=10)
            setClickFreq.grid(row=3,column=0,padx=30,pady=10)
            #mouseButtonValueLabel.grid(row=2,column=1)
            clickTimesLabel.grid(row=3,column=0,padx=30,pady=10)
            clickTimesValueLabel.grid(row=4,column=0,padx=10,pady=10)
            setClickTimes.grid(row=5,column=0,padx=15,pady=10)
            infiniteLabel.grid(row=0,column=0,padx=30,pady=10)
            inf.grid(row=1,column=0,padx=30,pady=10)
            #infTrue.grid(row=2,column=0,padx=30,pady=10)
            #infFalse.grid(row=3,column=0,pady=10)
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
        def loadConfig():
            global config,outputPos,clickFrequency,mouseButton,clickAmount,infinite,startKey,stopKey,winKey,clickMode,clickHoldTime,mouseX,mouseY
            
            try:
                config=json.load(tkinter.filedialog.askopenfile(initialdir='.',filetypes=[('json','.json')]))
                outputPos=config['outputPos']
                clickFrequency=config['clickFrequency']
                mouseButton=config['mouseButton']
                clickAmount=config['clickAmount']
                infinite=config['infinite']
                startKey=config['startKey']
                stopKey=config['stopKey']
                winKey=config['winKey'] 
                clickMode=config['clickMode'] 
                clickHoldTime=config['clickHoldTime'] 
                mouseX=config['mouseX'] 
                mouseY=config['mouseY']
                print(config)
            except IndexError:
                print('Loading config failed due to improper data structure.')
            except AttributeError:
                print('Loading config failed due to invalid file.')
            except:
                print('Unknown error occurred while loading config.')
        mainFrame=CTkFrame(master=mainWin,bg_color="gray")
        mainFrame.pack(fill='both',padx=20,pady=15)
        title= CTkLabel(master=mainFrame, text= 'Auto Clicker v2',font=('roboto',30))
        credit= CTkLabel(master=mainFrame, text='By Jaden909',font=('roboto',18))
        mainWin.geometry("550x310")
        startButton = CTkButton(master=mainFrame, text = 'Start Auto Clicker', command = start,fg_color=colorPos,hover_color=colorPosHover)
        changelog=CTkLabel(master=mainFrame, text= """Patch Notes:
         v2 Final Feature Update: Added all settings and ability to save/load config""", wraplength=520)
        global clickFrequency
        clickFrequency=str(clickFrequency)
        global clickAmount
        clickAmount=str(clickAmount)
        NOTE=CTkLabel(master=mainFrame, text="NOTE: Press ESC to bring this window back up after it is closed", wraplength=520)
        exitButton=CTkButton(master=mainFrame, text='Exit',command=exitScript,fg_color=colorNeg,hover_color=colorNegHover)
        settingsButton=CTkButton(master=mainFrame,text='Settings',command=openSettings,fg_color=colorMain)
        configButton=CTkButton(master=mainFrame,text='Load Config',command=loadConfig,fg_color=colorMain)
        title.pack()
        credit.pack()
        startButton.pack(pady=5)  
        settingsButton.pack(pady=5)
        configButton.pack(pady=5)
        exitButton.pack(pady=5)
        changelog.pack(pady=5)
        NOTE.pack()
        mainWin.mainloop()

"""___________________________________________________________________________________Code_____________________________________________________________________________"""

mainWindow()
if mouseX==0 and mouseY==0:
    manual=False
else:
    manual=True
def trackMouse():
    global currentMouseX, currentMouseY, clickTimes
    currentMouseX, currentMouseY=pyautogui.position()
    clickTimes+=0 if infinite else 1
if isRunning:    
    if clickMode=='Hold':
        time.sleep(1)
        trackMouse()
        pyautogui.mouseDown(button=mouseButton)
        time.sleep(clickHoldTime)
        pyautogui.mouseUp(button=mouseButton)
        if not infinite:
            mainWindow()
    else:    
        while int(clickTimes)<int(clickAmount)+1: 
            clickFrequency=int(clickFrequency)
            isRunning=True if keyboard.is_pressed(startKey) else isRunning
            isRunning=False if keyboard.is_pressed(stopKey) else isRunning
            if keyboard.is_pressed(winKey):
                mainWindow()
            if clickTimes==clickAmount:
                clickTimes=0
                isRunning=False
                mainWindow()    
            if isRunning:
                if not manual:
                    trackMouse()
                else:
                    currentMouseX,currentMouseY=mouseX,mouseY
                pyautogui.click(currentMouseX,currentMouseY,button=mouseButton,interval=int(clickFrequency)/1000)
                if outputPos:
                    print(currentMouseX,currentMouseY)