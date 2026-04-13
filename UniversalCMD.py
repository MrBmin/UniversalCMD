    #import batch try:
    #Hey!
    #I see you saw the text at the start and wanted to look through my code!
    #
    #Just a quick warning, this code is probably going to be of horrid quality,
    #but remember, this is my first big Python project, my first real, public one,
    #my first time actively using GitHub, and I'm a slow learner!
    #
    #So if you have any constructive feedback or want to enhance my code in any
    #way whatsoever, just report it as an issue on the UniversalCMD repo, then
    #I'll 101% see it
    #
    #(You may have already seen this in UniversalCMD, but the start of the code
    #has - could be scrapped - spoilers for future updates, so skip until
    #the "import" train the start of the actual code)
print("Loading files...")
import os
import colorama
try:
    import handler
except BaseException as err:
    for i in range(1, 100):    
        print(colorama.Back.RED)
    print(err)
    print(colorama.Back.RED, f"A fatal error has occurred! ")    
    print(colorama.Back.RED, f"                                                  ")    
    print(colorama.Back.RED, f"The crash handler could not be initalised!        ")
    print(colorama.Back.RED, f"It may have either been moved, deleted,           ")
    print(colorama.Back.RED, f"or corrupted.                                     ")
    print(colorama.Back.RED, f"                                                  ")
    print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
    print(colorama.Back.RED, f"Code: HANDLER_NOT_FOUND                           ")
    print(colorama.Back.RED, f"                                                  ")
    print(colorama.Back.RED, f"It's too risky to execute any further!            ")
    print(colorama.Back.RED, f"                                                  ")
    print(colorama.Back.RED, f"Press enter to exit with return code 1.")
    input()
    os._exit(1)
try:
    open("totally-not-important.png", "r")
except:
    handler.handle("FILE_NOT_FOUND", "An essential file was not found or is corrupted!", "totally-not-important.png")
import re
try:
    import stri
except FileNotFoundError:
    handler.handle("FILE_NOT_FOUND", "An essential file was not found or is corrupted!", "stri.py")
import inspect
try:
    import customcmd as cus
except:
    handler.handle("FILE_NOT_FOUND", "An essential file was not found or contains invalid code!", "customcmd.py")
import json
import datetime
import random
import installer



try:

    print("Loading style...")
    print(colorama.Back.BLACK)
    # add date (-change) time (-change)
    
    #you probably cant decipher what this is supposed to do but please still ignore it
    
    #try:
    #    with open("jsons\\firstBoot.json", "r") as f:
    #        fp = json.load(f)
    #        if fp.get("value") == True:
    #            print(fp.get("displayMessage", "Could not fetch value <displayMessage> from <jsons\\firstBoot.json>, have you been messing with files?"), end="")
    #            e2u = input()
    #            if e2u not in ("y", "n"):
    #                print("Neither y or n were specified, defaulting to off...")
    #                e2u = "n"
    #            with open("jsons\\options.json", "r") as g:
    #                temp1 = open("jsons\\options.json").read()
    #                temp1.replace('"e2u": False', '"e2u": True')
    #                with open("jsons\\options.json", "w") as gp:
    #                    json.dump(json.load(g), temp1, indent=2)            
    #        fp["value"] = False
    #        f.seek(0)
    #    with open("jsons\\firstBoot.json", "w") as fpp:
    #        json.dump(fp, fpp, indent=2)
    #except:
    #    print("\nSorry, the block of code running now has been worked on for about an hour, so it is really buggy, and it crashed!\nDon't worry, it's not anything too important to the rest of UniversalCMD!")
    #    input()
    
    de = "0"
    v = "1.1.0 PRE-ALPHA 13/Apr/2026"
    help = "install [optional-feature / -? / -remove] - Installs the specified optional feature, requires an internet connection. Type install -? to get a list of optional features and how to use them once they're installed. Type install -remove [installed-feature] to uninstall an already installed optional feature\nhelp - Displays this menu\nexit - What do you think this does?\nchange or changelog - Displays the changelog\ncd [path] - Changes the working directory to the specified path\ndebug [on/off] - Enables/disables viewing of extra debug info (intended for dev use, but it's viewable to anyone at the moment)\ndir ([path])- Without any arguments, displays the contents of the current directory, if a valid argument is provided, the contents of the argument will be provided\ncalc [-add/-sub/-mult/-div] [At least 2 numbers] - Performs the requested operation on the numbers provided\ntest [wip command] - Executes the W.I.P command specified, purely intended for dev, if a string is specified, it will output a modified string\npy [python code] - Executes the python code specified, if it's valid, use \"\\n\" for new lines\ncustom [custom command] - Executes the custom command, defined in the <customcmd.py> file, instruction on how to make a custom command are commented in customcmd.py\n(de)cipher [text] ([date for decipherer]) - Ciphers text through about 5 levels of encryption, supports some non-alphanumeric symbols, decipherer requires the key and the date on which the input was ciphered (FYI this is just copied code from another project I was working on for like 3 days so it may be buggy/not fit in)\ninvoke [code] - Invokes a crash with the specified code (purely intended for testing error handling [NOT SUPPOSED TO MAKE IT TO PRE-A V1.1.0])\ntext [file.txt] - If the specified file exists, modify it, otherwise create it"
    ue = "UniversalCMD.py"
    temp0 = None
    def take():
        ue = "UniversalCMD.py"
        global de    
        print("", end="\n")
        print("UCMD " + os.getcwd() + ">", end="")
        cmd = input()
        cmd0 = cmd.split(" ")[0]
        cmd1 = "[NOT SPECIFIED!]"
        cmd2 = "[NOT SPECIFIED!]"
        cmd3 = "[NOT SPECIFIED!]"
        if len(cmd.split(" "))>=2 :
            cmd1 = cmd.split(" ")[1]
        if len(cmd.split(" "))>=3 :
            cmd2 = cmd.split(" ")[2]
        if len(cmd.split(" "))>=4 :
            cmd3 = cmd.split(" ")[3]
        if de=="1":
            print(f"Command breakdown\nTrigger : '{cmd0}'\nArguments:'{cmd.split(" ")[1:]}'")
        #test feature
        #extmath feature
        if f"{cmd0}"=="e2u":
            print("This feature is still being worked on, this feature will release with either pre-alpha v1.1.0, or the first alpha version")
            take()
        if f"{cmd0}"=="install":
            ue = "installer.py"
            if cmd1 == "-?":
                print(f"To install, type install, then one of the feature names below\nOnce a feature has been installed, it will be integrated as an actual command\n(e.g. install xyz, then type xyz to use the feature)")
                print(f"\nHere are the list of optional features\n\ne2u - This isn't a command, but rather a full replacement for UniversalCMD, which is Easier 2 Understand. Refer to this version's readme for more information\nextmath [many possible operations] - I'm not listing all of the operations here, so if you really want to know them, run install extmath, then restart UniversalCMD and type extmath -?")
                take()
            if cmd1 == "-remove":
                print("Sorry, I'm a solo developer, and I have a 5-day residental trip with my school the day after tomorrow so I don't have time to vomit out the logic for install -remove (and also I actually want to make y'know, the actual features with only the time tomorrow so I have to focus on that a LOT), but I will after!")
                take()
            installer.install(cmd1)
            take()
        if f"{cmd0}"=="invoke":
            handler.handle(cmd1, "User invoked crash!", "Nothing")
            take()
        if f"{cmd0}"=="cipher":
            if not len(cmd.split(" "))>=2 :
                print("cipher takes 1 argument!")
            else:
                inp = cmd.removeprefix("cipher ")
                features = 5
                alphanumerics = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                valids = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "!", "\"", "£", "$", "€", "%", "^", "&", "*", "(", ")", "`", "¬", "¦", "\\", "|", "-", "_", "+", "=", "[", "{", "}", "]", ";", ":", "@", "'", "#", "~", ",", "<", ".", ">", "/", "?"]
                key = alphanumerics[random.randint(0, 35)]
                for i in range(features - 1):
                    if i == 0:
                        key += alphanumerics[random.randint(5, 35)]
                    elif i == 1:
                        key += alphanumerics[random.randint(0, 35)]
                        if key[1] == key[0]:
                            key[1] = 0
                    key += alphanumerics[random.randint(0, 35)]
                out = ""
                for c in inp:
                    print(f"Translating \"{c}\"")    
                    try:
                        char = c.upper()
                        ind = valids.index(char)
                        ind += alphanumerics.index(key[0])
                        ind -= alphanumerics.index(key[1])
                        if i % 2 == 0: # type: ignore
                            ind += alphanumerics.index(key[2])
                            ind -= alphanumerics.index(key[3])
                            ind += datetime.datetime(year=datetime.datetime.now().year, day=datetime.datetime.now().day, month=datetime.datetime.now().month).timetuple().tm_yday
                            ind %= len(valids)
                    except BaseException as er:
                        out += c
                        print(f"DEBUG {er}")  
                    out += valids[ind]
    # alphanumerics.index(key[0])
                print(f"\nHere's the ciphered text:\n{out}\nKey: `{key}`\nCiphered on: {"%02d" % datetime.datetime.now().day}/{"%02d" % datetime.datetime.now().month}/{datetime.datetime.now().year}, remember that if you want to decipher this!")
                take()
            if f"{cmd0}"=="test":
                print(stri.sh(cmd1))
                take()
            if f"{cmd0}"=="py":
                cmd1 = " ".join(cmd.split(" ")[1:]).replace("\\n", "\n")
                try:
                    exec(cmd1)
                except BaseException as err:
                    print(f"Invalid code: {err}")
                take()
        if f"{cmd0}"=="custom":
            with open("customcmd.py", "r") as f:
                if "import os" in f:
                    print("WARNING: The custom command source, <customcmd.py>, uses the OS module, running a custom command may not be safe, are you sure you want to continue? >")
                    t = input()
                    print()
                    if f"{t}"=="y":
                        try:
                           arg = inspect.signature(getattr(cus, f"{cmd1}")).parameters
                           if len(arg)==0:
                                getattr(cus, f"{cmd1}")()
                           if len(arg)==1:
                                getattr(cus, f"{cmd1}")(cmd2)
                           if len(arg)==2:
                                getattr(cus, f"{cmd1}")(cmd2, cmd3)
                        except BaseException as err:
                            print(f"Couldn't execute command: {err}")
                    else:
                        print("Couldn't execute command: OS module not allowed by user")
                        take()
                    try:
                        arg = inspect.signature(getattr(cus, f"{cmd1}")).parameters
                        if len(arg)==0:
                            getattr(cus, f"{cmd1}")()
                            take()
                        if len(arg)==1:
                            getattr(cus, f"{cmd1}")(cmd2)
                            take()
                        if len(arg)==2:
                            getattr(cus, f"{cmd1}")(cmd2, cmd3)
                            take()
                    except BaseException as err:
                        print(f"Couldn't execute command: {err}")
            take()
        if f"{cmd}"=="help":
            print(help)
            take()
        if f"{cmd}"=="exit":
            os._exit(0)
        if f"{cmd}"=="change" or f"{cmd}"=="changelog":
            print(f"CHANGELOG\n{v}\n\nFEATURES\n-Tweaked the custom command to only warn you if it uses the OS module (This isn't working at the moment and instead just doesn't run if it detects the OS module for some reason, if you're seeing this, sorry!)\n-Subtly changed the version numbering to start at 1.0 instead of 0.0\n-Changed the command input line to say UCMD at the start, taking inspiration from PowerShell (and also to make sure I stop mixing up UniversalCMD with PowerShell during testing)\n\nBUGFIXES\n-Not really a bug, but made it so the version numbers are all synced\n-(Hopefully) fixed the bug where if you don't provide the correct number of arguments, UniversalCMD crashes")
            take()
        if f"{cmd0}"=="cd":
            if not len(cmd.split(" "))>=2 :
                print(f"cd takes 1 argument, can't execute command!")
                take()
            if os.path.exists(cmd1):
                os.chdir(cmd1)
            else:
                print(f"The directory provided, '{cmd1}', wasn't found!")
            take()
        if f"{cmd0}"=="debug":
            if not len(cmd.split(" "))>=2 :
                print(f"debug takes 1 argument, can't execute command!")
                take()
            if f"{cmd1}"=="on":
                de="1"
                with open("jsons\\options.json", "w") as f:
                    for line in f:
                        if "debug" in line:
                            temp2 = f.read().replace("\"debug\": true", "\"debug\": false")
                            f.write(temp2)
            else:
                de="0"
            print(de)
            take()
        if f"{cmd0}"=="dir":
            fileList = list()
            folderList = list()
            print("[Folder]  File\n")
            if not len(cmd.split(" "))>=2 :
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
            print(f"\nFound {len(fileList) + len(folderList)} objects, {len(fileList)} files, and {len(folderList)} folders.\nBy the way, anything with a dot counts as a folder, so the numbers may be wrong!")            
            take()
        if f"{cmd0}"=="calc":
            if not cmd3:
                print(f"calc takes 3 arguments, can't execute command!")
                take()
            if cmd1=="-add":
                try:
                    print(float(cmd2) + float(cmd3))
                    take()
                except:
                    print("One or more number arguments were not numbers!")
                    take()
            if cmd1=="-sub":
                try:
                    print(float(cmd2) - float(cmd3))
                    take()
                except:
                    print("One or more number arguments were not numbers!")
                    take()
            if cmd1=="-mult":
                try:
                    print(float(cmd2) * float(cmd3))
                    take()
                except:
                    print("One or more number arguments were not numbers!")
                    take()
            if cmd1=="-div":
                if cmd3=="0":
                    print("Attempted division by 0!")
                    take()
                try:
                    print(float(cmd2) / float(cmd3))
                    take()
                except:
                    print("One or more number arguments were not numbers!")
                    take()                  
        print(f"\nThe command '{cmd0}' wasn't recongnised, did you make it lowercase?")
        take()
    def start():
        print(colorama.Back.BLACK, f"\nVersion {v}\nI have no way of stopping you, but please, do not copy parts of UniversalCMD's code and label it as your own!!\nThis is an open-source project, so you can take a look at my horrible code on GitHub!\n[The comments near the start of the code may contain - unconfirmed - spoilers for future updates, so be careful!]\n\nhelp for list of commands, all built-in commands are case-sensitive!");
        take()
except KeyboardInterrupt:
    handler.handle("CTRL_C_ATTEMPTED", "Ctrl+C attempted!", "UniversalCMD.py and you (no offense)")

except FileNotFoundError:
    handler.handle("FILE_NOT_FOUND", "Couldn't find an essential file!", "AT LEAST UniversalCMD.py")

except BaseException as err:
    handler.handle("UNK_ERR", f"{err}", ue)
    
if __name__ == "__main__":
    start()
else:
    print("The file running has attempted to import UniversalCMD, although this is the wrong version!.\n\nThis is UniversalCMD v1.1.0 pre-alpha, I haven't made a library version yet, although at this version's release, it should be under development.")
    print("This script will now continue as normal, although any UniversalCMD library features won't work.")
      
    def cmd():
        print("This file has attempted to run a UniversalCMD library feature on a version prior to it being added!\nThis file is using UniversalCMD v1.1.0 pre-alpha and has attempted to call UniversalCMD.cmd()")

handler.handle("TAKE_FUNC_EXITED", "Command input has been unexpectedly cut off!", "UniversalCMD.py")



for i in range(1, 100):    
    print()


    
#fun fact:
#
#v1.0.3 pre-alpha's release was delayed by about 10 minutes due to 2FA issues
