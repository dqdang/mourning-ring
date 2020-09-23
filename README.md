# mourning-ring
Keylogger for Windows

## Install requirements from here:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32
<br/>
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywinhook

## Notes

Download the wheel for your version of Python and 32/64 bit CPU. You can check if you open a Python interpreter and check the output of the header:
```
$ python
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
ex. `pywin32‑228‑cp39‑cp39‑win_amd64.whl` for a 64 bit Python 3.9.x

Install the downloaded wheel with\
`python -m pip install WHL_FILE.whl`
