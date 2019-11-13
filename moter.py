import psutil
import applescript
import subprocess
import sys
import os
from os import path
import time

commands = ['start','stop','watch']

command = str(sys.argv[1])
if command not in commands:
  print('you must specify valid command')
  sys.exit() 

try:
  terminal = os.environ['TERM_PROGRAM']
except:
  print('something went wrong')


if len(sys.argv) >= 3:
  vod = str(sys.argv[2])
    
  if path.exists(vod) == False and "http" not in vod:
    print('issue with path. exiting.')
    sys.exit()

else:
    if "MOTER_DEFAULT" in os.environ:
        vod = os.environ["MOTER_DEFAULT"]
    else:
        if command == 'start':
            print('MOTER_DEFAULT not found.')
        vod = 'https://github.com/gWOLF3/moter/blob/master/samples/mother-earth.mp4?raw=true'


def watch():
    print('''
MOTER WATCH PROCESS. WILL EXIT AUTOMATICALLY.
''')
    while "VLC" in (p.name() for p in psutil.process_iter()):
        if "iTerm2" not in (p.name() for p in psutil.process_iter()):
            subprocess.check_call(["osascript","-e",'tell application "VLC" to quit'])
            sys.exit()
            break
        else:
            pass


def welcome():
    print('''

    
                          WELCOME TO  
       .___  ___.   ______   .___________. _______ .______      
       |   \/   |  /  __  \  |           ||   ____||   _  \     
       |  \  /  | |  |  |  | `---|  |----`|  |__   |  |_)  |    
       |  |\/|  | |  |  |  |     |  |     |   __|  |      /     
       |  |  |  | |  `--'  |     |  |     |  |____ |  |\  \----.
       |__|  |__|  \______/      |__|     |_______|| _| `._____|

                   THE MOTION PICTURE TERMINAL


''')

def vlc():
  subprocess.Popen(["vlc","--no-audio","--video-wallpaper","--loop","--no-video-title","-q",vod],stdout=None,stderr=None)

  time.sleep(1)
  window = True 
  while window:
    try: 
      subprocess.Popen(['osascript','-e','tell application "VLC" to set visible of front window to false'],stdout=None,stderr=None)
      window = False  
    except:
      pass

def start():
    applescript.tell.app("System Events",'keystroke "h" using {command down, option down}')
    applescript.tell.app("System Events",'keystroke "f" using {command down, option down}')
    vlc()
    time.sleep(1.5)
    applescript.tell.app("iTerm",'set the transparency of the current session of the current window to 0.3') 
    applescript.tell.app("System Events",'keystroke "t" using {command down}')
    applescript.tell.app("System Events",'keystroke "w" using {command down}')
    applescript.tell.app("System Events",'keystroke "k" using {command down}')
    welcome()

if command == 'start':
  if terminal == 'iTerm.app':
    applescript.tell.app("Terminal",'do script ""')
    applescript.tell.app("Terminal",'activate')
    applescript.tell.app("Terminal",'set size of window 1 to {590,140}')
    while not "Terminal" in (p.name() for p in psutil.process_iter()):
        pass
    applescript.tell.app("Terminal",'do script "exec moter watch" in window 1')
    applescript.tell.app("Terminal",'set size of window 1 to {590,140}')
    applescript.tell.app("Terminal",'set custom title of tab 1 of window 1 to "watcher"')
    applescript.tell.app("Spectacle",'activate')
    applescript.tell.app("iTerm",'activate')
    term = 'iTerm'
    start()
  else:
    term = 'Terminal'
    applescript.tell.app("iTerm",'activate')
    applescript.tell.app("iTerm",'tell current session of current window to write text ""')
    applescript.tell.app("iTerm",'tell current session of current window to write text "moter start"')


if command == 'stop':
  if terminal == 'iTerm.app':
    applescript.tell.app("iTerm",'set the transparency of the current session of the current window to 0')  
  if "VLC" in (p.name() for p in psutil.process_iter()): 
    subprocess.check_call(["osascript","-e",'tell application "VLC" to quit'])
  time.sleep(0.5)
  applescript.tell.app("Terminal",'close every window whose name contains "watcher"')


if command == 'watch':
    time.sleep(4)
    watch()
