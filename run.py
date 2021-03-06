"""This is a bad hack, or an alternative as
I'd like to put it, to a cron job shutting
down faqbot and restarting it every so often.

The reason for this is because IDLE is finicky
and our current system doesn't know how to catch
disconnects, so we just restart before stuff
stop working.
"""

import subprocess
import time
import psutil
import signal
import sys

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

VERBOSE = True
DELAY = 1200 # seconds, or 20 minutes

lastproc = None

# Loop infinitely.
while True:
    # Start the app.
	p = subprocess.Popen(["python", "app.py"])
	lasproc = p.pid
	print '[Runner] Started at', p.pid

	time.sleep(DELAY) # Wait a minute.

	if VERBOSE:
		print "Killing {}".format(p.pid)

	kill(p.pid) # KILL.