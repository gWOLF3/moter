import psutil
import applescript
import subprocess
import sys
import os
from os import path
import time

command = str(sys.argv[1])
if command != 'start' and command != 'stop':
  print('you must specify valid command')
  sys.exit() 

try:
  terminal = os.environ['TERM_PROGRAM']
  print('detected terminal '+terminal)  
except:
  print('something went wrong')

if len(sys.argv) >= 3:
  vod = str(sys.argv[2])
    
  if path.exists(vod) == False:
    print('issue with path. exiting.')
    exit

if command == 'start':
  
  print('starting moter background...')

  # fullscreen terminal (hasDep: spectacle) 
  applescript.tell.app("System Events",'keystroke "f" using {command down, option down}')
  
  subprocess.Popen(["vlc","--no-audio","--video-wallpaper","--loop","--no-video-title","-q",vod],stdout=None,stderr=None)

  time.sleep(0.5)
  window = True 
  while window:
    try: 
      subprocess.check_call(['osascript','-e','tell application "VLC" to set visible of front window to false'],stdout=None,stderr=None)
      window = False  
    except:
      pass
  
  if terminal == 'iTerm.app':
    applescript.tell.app("iTerm",'set the transparency of the current session of the current window to 0.3') 
    
    applescript.tell.app("System Events",'keystroke "t" using {command down}')
    applescript.tell.app("System Events",'keystroke "w" using {command down}')
    applescript.tell.app("iTerm",'tell current session of current window to write text "clear"')
    term = 'iTerm'

  else:
    term = 'Terminal'
    print('You must manually adjust your background transparency (opacity=60% is recommended). Auto adjust only supported on iTerm')


if command == 'stop':
  if terminal == 'iTerm.app':
    print('resetting background..')
    applescript.tell.app("iTerm",'set the transparency of the current session of the current window to 0')  
  print('stopping moter background...')
  if "VLC" in (p.name() for p in psutil.process_iter()): 
    subprocess.check_call(["osascript","-e",'tell application "VLC" to quit'])
