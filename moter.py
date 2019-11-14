import click
import psutil
import applescript
import subprocess
import sys
import os
from os import path
import time


@click.version_option(version=subprocess.getoutput("brew cask list --versions moter"))
@click.group()
def cli():
    pass


def validate_video(ctx, param, value):
    try:
        if path.exists(value):
            return value
        elif "http" in value:
            return value
    except ValueError:
        raise click.BadParameter("video needs to be a valid file path or url. please use absolute paths.")


def watcher():
    print("""
MOTER WATCH PROCESS. WILL EXIT AUTOMATICALLY.
""")
    while "VLC" in (p.name() for p in psutil.process_iter()):
        if "iTerm2" not in (p.name() for p in psutil.process_iter()):
            subprocess.check_call([
                "osascript",
                "-e",
                'tell application "VLC" to quit'
            ])
            sys.exit()
            break
        else:
            pass


def welcome():
    print("""

    
                          WELCOME TO  
       .___  ___.   ______   .___________. _______ .______      
       |   \/   |  /  __  \  |           ||   ____||   _  \     
       |  \  /  | |  |  |  | `---|  |----`|  |__   |  |_)  |    
       |  |\/|  | |  |  |  |     |  |     |   __|  |      /     
       |  |  |  | |  `--'  |     |  |     |  |____ |  |\  \----.
       |__|  |__|  \______/      |__|     |_______|| _| `._____|

                   THE MOTION PICTURE TERMINAL


""")


def vlc(video):
    subprocess.Popen([
        "vlc",
        "--no-audio",
        "--video-wallpaper",
        "--loop",
        "--no-video-title",
        "-q",
        video
    ], stdout=None, stderr=None)

    time.sleep(1)
    window = True
    while window:
        try:
            subprocess.Popen([
                "osascript",
                "-e",
                'tell application "VLC" to set visible of front window to false'
            ], stdout=None, stderr=None)
            window = False
        except:
            pass


def run(video):
    applescript.tell.app("System Events", 'keystroke "h" using {command down, option down}')
    applescript.tell.app("System Events", 'keystroke "f" using {command down, option down}')
    vlc(video)
    time.sleep(1.5)
    applescript.tell.app("iTerm", "set the transparency of the current session of the current window to 0.3")
    applescript.tell.app("System Events", 'keystroke "t" using {command down}')
    applescript.tell.app("System Events", 'keystroke "w" using {command down}')
    applescript.tell.app("System Events", 'keystroke "k" using {command down}')
    welcome()


@cli.command()
@click.option("-v", "--video", default="https://github.com/gWOLF3/moter/blob/master/samples/mother-earth.mp4?raw=true", type=str, envvar="MOTER_DEFAULT", show_default=True, show_envvar=True, required=False, callback=validate_video)
@click.option("-d", "--desktop-only", "desktop_only", is_flag=True, envvar="MOTER_DESKTOP_ONLY", default=False, show_envvar=True, show_default=True)
def start(video, desktop_only):
    if desktop_only:
        vlc(video)
        sys.exit()
    if os.environ["TERM_PROGRAM"] == "iTerm.app":
        applescript.tell.app("Terminal", 'do script ""')
        applescript.tell.app("Terminal", "activate")
        applescript.tell.app("Terminal", "set size of window 1 to {590,140}")
        while not "Terminal" in (p.name() for p in psutil.process_iter()):
            pass
        applescript.tell.app("Terminal", 'do script "exec moter watch" in window 1')
        applescript.tell.app("Terminal", "set size of window 1 to {590,140}")
        applescript.tell.app("Terminal", 'set custom title of tab 1 of window 1 to "watcher"')
        applescript.tell.app("Spectacle", "activate")
        applescript.tell.app("iTerm", "activate")
        run(video)
    else:
        if "iTerm2" in (p.name() for p in psutil.process_iter()):
            applescript.tell.app("iTerm",'create window with default profile')
        else:
            applescript.tell.app("iTerm", "activate")
        applescript.tell.app("iTerm", 'tell current session of current window to write text ""')
        applescript.tell.app("iTerm", f'tell current session of current window to write text "moter start -v {video}"')


@cli.command()
def stop():
    if os.environ["TERM_PROGRAM"] == "iTerm.app":
        applescript.tell.app("iTerm", "set the transparency of the current session of the current window to 0")
    if "VLC" in (p.name() for p in psutil.process_iter()):
        subprocess.check_call([
            "osascript",
            "-e",
            'tell application "VLC" to quit'
        ])
    time.sleep(0.5)
    applescript.tell.app("Terminal", 'close every window whose name contains "watcher"')


@cli.command()
def watch():
    time.sleep(4)
    watcher()


if __name__ == "__main__":
    cli()
