# Auto Clicker v2
The final feature update.

## Configurable Settings
`outputPos`: (bool) whether or not to print the coordinates of the mouse to the console.

`clickFrequency`: (int) the time between clicks in milliseconds

`mouseButton`: (str) the mouse button to press (left, middle, or right)

`clickAmount`: (int) How many times to click before stopping (must be positive, has no effect if `infinite` is true)

`infinite`: (bool) Whether or not to click indefinitely

`startKey`: (str) Key to start the autoclicker (must be name of a key on a keyboard ex. 'pageup','t','shift')

`stopKey`: (str) Key to stop the autoclicker (must be name of a key on a keyboard ex. 'pagedown','t','shift')

`winKey`: (str) Key to open the window while the autoclicker is running (must be name of a key on a keyboard ex. 'pagedown','t','shift')

`clickMode`: (str) How the auto clicker clicks (click or hold)

`clickHoldTime`: (int) How long to hold click (only has an effect is `clickMode` is hold

`mouseX`,`mouseY`:(int) Used to manually position mouse
