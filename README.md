# 📽 moter: the 'motion picture terminal'
## bring your workstation to life!
!['demo-gif'](./assets/moter-480.gif)

### What is this? 
Moter is a motion picture terminal designed to enhance your workstation experience. For those that may spend many hours each day working in the terminal, staring at a black screen can be an isolating experience. I created motor for myself because I am one of those people and time lapse footage of outer space makes me happy. 

### Quickstart:
1. install: `brew cask install moter`  

2. setup: [permissions](#permissions) (**required** or will not work properly) 

3. run: `moter start ` / `moter stop`  



### How should I use this?  

#### Customization

Set a default background video: `export MOTER_DEFAULT=<path/url>` (this will play on `start`) 

Experiment with new videos: `moter start <path/url>`  

#### Formats
Motor uses VLC media player behind the scenes, so any [supported format](https://en.wikipedia.org/wiki/VLC_media_player#Input_formats) will work here too. You can even use a URL (youtube,etc). I also included a couple samples to get you started. 


#### <a name="permissions"></a>Permissions 

Moter requires accessibily access of the following:

- Terminal
- iTerm
- Spectacle
- System Events

<img src="./assets/instr-320.gif" alt="instr.gif" style="width:210px;height:160px"/> 

