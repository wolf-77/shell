# shell code would be here
import os
import commands
import signal
import external

welcome_msg = '''
██     ██  ██████  ██      ███████     ███████ ██   ██ ███████ ██      ██      
██     ██ ██    ██ ██      ██          ██      ██   ██ ██      ██      ██      
██  █  ██ ██    ██ ██      █████       ███████ ███████ █████   ██      ██      
██ ███ ██ ██    ██ ██      ██               ██ ██   ██ ██      ██      ██      
 ███ ███   ██████  ███████ ██          ███████ ██   ██ ███████ ███████ ███████
'''


built_in_commands = {
    'cls': commands.cls,
    'cd': commands.cd,
    'pwd': commands.pwd,
    'ls': commands.ls,
    'cat': commands.cat,
    'mfile': commands.mfile,
    'mkdir': commands.mkdir,
    'btc': commands.btc,
    'hash': commands.hash,
    'env': commands.env
}

def ctrl_c(*args):
    exit(0)

signal.signal(signal.SIGINT, ctrl_c)

def shell():
    print(welcome_msg)
    print(f'{os.getcwd()}')
    command = ''

    while command != 'exit':
        command = input(':: ')
        # execute command
        cmd = command.split()
        
        for k in built_in_commands.keys():
            if k == cmd[0]:
                # print(cmd[1:])
                built_in_commands[k](cmd[1:])
                break
        else:
            external.run_external(cmd)