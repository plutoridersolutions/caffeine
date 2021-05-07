import sys
import time
import win32api
from pynput.keyboard import Key, Controller

last = time.time()
keyboard = Controller()
print('Awake function will start in 10 seconds. To resume normal work press Q..')
time.sleep(10)

keyboard.press(Key.cmd)
keyboard.press('d')
keyboard.release('d')
keyboard.release(Key.cmd)

while(True):
    if win32api.GetAsyncKeyState(ord('Q')):
	    sys.exit()

    if (time.time() - last >= 59):
        last = time.time()
        keyboard.press(Key.esc)
        time.sleep(0.001)
        keyboard.release(Key.esc)
        time.sleep(0.001)