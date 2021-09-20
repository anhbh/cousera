
import os

prompt_prefix="> "
result_prefix=""
error_prefix="%"
debug_prefix="!"

def func_pwd(cmd):
    print(result_prefix + os.getcwd())
    
def func_ls(cmd):
    #print(os.listdir())
    entries=os.listdir()
    for entry in entries:
        print(result_prefix + entry)
        
def func_cd(cmd):
    target_dir=cmd[1]
    try:
        os.chdir(target_dir)
    except:
        print(error_prefix, "Invalid directory:", target_dir) 
    
def func_cat(cmd):
    filename=cmd[1]
    try:
        fh=open(filename)
        print(fh.read())
    except:
        print(error_prefix, "failed to open file", filename)

def prompt():
    return(os.getcwd()+prompt_prefix)

while True:
    # Command   Argument
    # pwd
    # cd 
    # cat
    # done

    try:
        cmdstr=input(str(prompt()))
        cmdstr=cmdstr.lstrip()                 # remove space in left
        if (cmdstr == ""):
            continue

        command=cmdstr.split()         # split into list of command 
        
        # debug
        # print(debug_prefix, command)
        
        if (command[0] == "pwd"):
            func_pwd(command)
        elif (command[0] == "cd"):
            func_cd(command)
        elif (command[0] == "ls"):
            func_ls(command)
        elif (command[0] == "cat"):
            func_cat(command)
        elif (command[0] == "done"):
            print(result_prefix + "Bye!")
            break;
        else:
            continue
    except:
        print(error_prefix, "Error")

SystemExit()
    