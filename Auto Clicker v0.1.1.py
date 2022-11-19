import ctypes
import ctypes.wintypes
import pyautogui
from pyautogui import LEFT, MIDDLE, RIGHT
"""Required modules for auto clicker to work"""

clicks=0
"""Number of times the 'trackMouse' function has been called"""

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
    # TODO: ARG! For some reason, SendInput isn't working for mouse events. I'm switching to using the older mouse_event win32 function.
    #mouseStruct = MOUSEINPUT()
    #mouseStruct.dx = x
    #mouseStruct.dy = y
    #mouseStruct.mouseData = ev
    #mouseStruct.time = 0
    #mouseStruct.dwExtraInfo = ctypes.pointer(ctypes.c_ulong(0)) # according to https://stackoverflow.com/questions/13564851/generate-keyboard-events I can just set this. I don't really care about this value.
    #inputStruct = INPUT()
    #inputStruct.mi = mouseStruct
    #inputStruct.type = INPUT_MOUSE
    #ctypes.windll.user32.SendInput(1, ctypes.pointer(inputStruct), ctypes.sizeof(inputStruct))

    # TODO Note: We need to handle additional buttons, which I believe is documented here:
    # https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-mouse_event

    width, height = _size()
    convertedX = 65536 * x // width + 1
    convertedY = 65536 * y // height + 1
    ctypes.windll.user32.mouse_event(ev, ctypes.c_long(convertedX), ctypes.c_long(convertedY), dwData, 0)

    # TODO: Too many false positives with this code: See: https://github.com/asweigart/pyautogui/issues/108
    #if ctypes.windll.kernel32.GetLastError() != 0:
    #    raise ctypes.WinError()

    
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

"""________________________________Settings__________________________________"""

outputPos='true'
#Weather or not the autoclicker should output the mouse position in the console

clickFrequency="not implemented yet"
#how frequently to click (in ms)

button="left"
#Which mouse button to press ('left','middle','right')

clickAmount=100
#How many times you want the autoclclicker to click (any positive number)

infinite=-1
#Weather or not the autoclicker works infinitely (1 for true, -1 for false)

"""__________________________________Code____________________________________"""

def posOutput():
    print(currentMouseX,currentMouseY)    

def trackMouse():
    global currentMouseX, currentMouseY
    currentMouseX, currentMouseY=pyautogui.position()
    global clicks
    clicks=clicks-infinite
while clicks<clickAmount: 
    trackMouse()
    _click(currentMouseX, currentMouseY, button)
    if outputPos=='true':
            posOutput()
    else: pass
    
