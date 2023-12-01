#!/bin/sh
#
#       admin@kamenka.su
#
########################

curdir=$(dirname $0)
GRP= ps -xa | pgrep -f reverse_bot.py | grep -o "^\S\+"

if [ $? -eq 0 ]; then
	
	echo "ok"
else
	
	echo "Bot is dead. Restarting..."
	($curdir/../env/bin/python3 -u $curdir/reverse_bot.py)&
	
fi
