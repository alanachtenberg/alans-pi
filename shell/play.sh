#bash for playing videos in omxplayer
setterm -blank off -powerdown off > /dev/tty0

clear > /dev/tty0

setterm -cursor off > /dev/tty0

omxplayer -d "$1" > /dev/tty0 

clear > /dev/tty0

# turn the cursor back on when done with omxplayer
setterm -cursor on > /dev/tty0
