import os
import subprocess

def check(application):
    """
    Run External Command Line Programs
    Only run .exe file types
    """
    res = False
    for i in os.getenv('PATH').split(';'):
        res = os.path.exists(i + "\\"+f"{application}.exe")
        if res:
            return i + f"\\{application}.exe"
    else:
        return False

def run_external(*args):
    cmd = list(args[0])
    x = check(cmd[0])
    if x == False:
        print('=> Not such command found.')
    else:
        subprocess.call(cmd)