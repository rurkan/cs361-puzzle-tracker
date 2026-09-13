import os
import subprocess

# Code for clearing screen across OS from stackoverflow:
# Source - https://stackoverflow.com/a/5369197
# Posted by Acorn, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-13, License - CC BY-SA 4.0

if os.name == 'nt':
    def clearscreen():
        subprocess.call("cls", shell=True)
        return
else:
    def clearscreen():
        subprocess.call("clear", shell=True)
        return

# End stackoverflow post
