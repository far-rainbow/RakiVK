#!/bin/sh
#
#	admin@kamenka.su
#
########################

SCRIPT_NAME="reverse_bot.py"

# get PID of SCRIPT_NAME
PROC_ID=$(ps -xa | pgrep -f $SCRIPT_NAME)

# If runnig - kill it
if [ -n "${PROC_ID}" ]; then
	kill -9 $PROC_ID
	echo "Script ${SCRIPT_NAME} with PID ${PROC_ID} stoped."
else
	echo "No running procces is found!"
	exit 1
fi