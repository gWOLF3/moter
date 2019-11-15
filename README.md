# 📽 moter: the 'motion picture terminal'
## bring your workstation to life!
!['demo-gif'](./assets/moter-480.gif)

### What is this? 
Moter is a motion picture terminal designed to enhance your workstation experience. For those that may spend many hours each day working in the terminal, staring at a black screen can be an isolating experience. I created motor for myself because I am one of those people and time lapse footage of outer space makes me happy. 

### Quickstart:
1. install: `brew tap gwolf3/craft` & `brew cask install moter`  

2. setup: [permissions](#permissions) (**required** or will not work properly) 

3. run: `moter start ` / `moter stop`  


### How should I use this?  

#### Additional Commands

Get help: `moter --help` /  `moter <command> --help`

Get version: `moter --version`


#### Customization

Set a new default background video: `export MOTER_DEFAULT=<path/url>` (this will play on `start`) 

Experiment with new videos: `moter start -v <path/url>`  

***(Hint: please be sure to use absolute paths & include 'http/https' scheme for urls)***

Run in desktop mode (disable terminal): `moter start --desktop-only`

Desktop mode can also be enabled by default: `export MOTER_DESKTOP_ONLY=True`

#### Formats
Motor uses VLC media player behind the scenes, so any [supported format](https://en.wikipedia.org/wiki/VLC_media_player#Input_formats) will work here too. You can even use a URL (youtube,etc). I also included a couple samples to get you started. 


#### <a name="permissions"></a>Permissions 

Moter requires accessibily access of the following:

- Terminal _(/Application/Terminal.app)_
- iTerm _(/Application/iTerm.app)_
- Spectacle _(/Applications/Spectacle.app)_
- System Events _(/System/Library/CoreServices/System\ Events.app)_

<img src="./assets/instr-320.gif" alt="instr.gif" style="width:210px;height:160px"/> 

***(Hint: if you cannot find any items here, you may need to search and add them with the `+` button)***
