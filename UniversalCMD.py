import os
import re
de = "0"
v = "0.0.1 PRE-ALPHA 04/Jan/2026"
c = "CHANGELOG\n0.0.1 PRE-ALPHA 03/Jan/2026\n\nFEATURES\n\n- Commands\n- The help list\n- The changelog"
help = "help - Displays this menu\nexit - What do you think this does?\nchange or changelog - Displays the changelog\ncd [path] - Changes the working directory to the specified path\ndebug [on/off] - Enables/disables viewing of extra debug info (intended for dev use, but it's viewable to anyone at the moment)\ndir ([path])- Without any arguments, displays the contents of the current directory, if a valid argument is provided, the contents of the argument will be provided"
temp0 = None
def take():
    global de    
    print("", end="\n")
    print(os.getcwd() + ">", end="")
    cmd = input()
    cmd0 = cmd.split(" ")[0]
    if len(cmd.split(" "))>=2 :
        cmd1 = cmd.split(" ")[1]
    else:
        cmd1 = None
    if de=="1":
        print(f"Command breakdown\nTrigger : '{cmd0}'\nArguments:'{cmd.split(" ")[1:]}'")
    if f"{cmd}"=="help":
        print(help)
        take()
    if f"{cmd}"=="exit":
        return
    if f"{cmd}"=="change" or f"{cmd}"=="changelog":
        print(c)
        take()
    if f"{cmd0}"=="cd":
        if not cmd1:
            print(f"cd takes 1 argument, can't execute command!")
            take()
        if os.path.exists(cmd1):
            os.chdir(cmd1)
        else:
            print(f"The directory provided, '{cmd1}', wasn't found!")
        take()
    if f"{cmd0}"=="debug":
        if not cmd1:
            print(f"debug takes 1 argument, can't execute command!")
            take()
        if f"{cmd1}"=="on":
            de="1"
        else:
            de="0"
        print(de)
        take()
    if f"{cmd0}"=="dir":
        fileList = list()
        folderList = list()
        print("[Folder]  File\n")
        if not cmd1:
            target = os.getcwd()
            for i in range(0, len(os.listdir(target))):
                if not os.listdir(target)[i].find(".")==-1:
                    fileList += [os.listdir(target)[i]]
                else:
                    folderList += [os.listdir(target)[i]]
                
        elif os.path.exists(cmd1):
            target = cmd1
            for i in range(0, len(os.listdir(target))):
                if not os.listdir(target)[i].find(".")==-1:
                    fileList += [os.listdir(target)[i]]
                else:
                    folderList += [os.listdir(target)[i]]
        elif not os.path.exists(cmd1):
            target = os.getcwd()
            print(f"The directory provided, '{cmd1}', wasn't found, displaying current directory instead.")
            for i in range(0, len(os.listdir(target))):
                if not os.listdir(target)[i].find(".")==-1:
                    fileList += [os.listdir(target)[i]]
                else:
                    folderList += [os.listdir(target)[i]]
        for i in range(0, len(folderList)):
            if i%10==1:
                print(f"[{folderList[i]}]")
            print(f"[{folderList[i]}]", end="  ")            
        for i in range(0, len(fileList)):
            if i%10==1:
                print(f"{fileList[i]}")
            print(f"{fileList[i]}", end="  ")
        print(f"Found {len(fileList) + len(folderList)} objects, {len(fileList)} files, and {len(folderList)} folders.\nBy the way, anything with a dot counts as a folder, so the numbers may be wrong!")            
        take()
    print(f"\nThe command '{cmd0}' wasn't recongnised, did you make it lowercase?")
    take()
def start():
    print(f"\nVersion {v}\nWARNING: Unstable build of UniversalCMD, expect bugs!\nThis is an open-source project, so you can take a look at my horrible code on GitHub!\n\nhelp for list of commands, all built-in commands are case-sensitive!");
    take()

start()

print("\n\nAn unknown error has occured, and a core loop stopped functioning, please report what you were doing leading up to this error to GitHub!!\n")
start()