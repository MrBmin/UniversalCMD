import colorama
import os
import datetime
import time

def handle(code:str, reason:str, failure:str):
    #ONE OF THE ARGUMENTS IS CALLED FAILURE LMAOOO
    print(f"UniversalCMD has encountered a serious error: {reason}")
    time.sleep(2)
    if code == "FEATURE_INSTALLATION_FAILURE":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"A possibly fatal error has occurred! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"Installing an optional feature has failed,        ")
        print(colorama.Back.RED, f"in order to make the features into commands,      ")
        print(colorama.Back.RED, f"UniversalCMD's code must be modified, so          ")
        print(colorama.Back.RED, f"UniversalCMD may or may not be corrupted,         ")
        print(colorama.Back.RED, f"please re-download UniversalCMD from MrBmin's     ")
        print(colorama.Back.RED, f"GitHub profile!                                   ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
        print(colorama.Back.RED, f"Code: FEATURE_INSTALLATION_FAILURE                ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to exit with return code 1.")
        input()
        os._exit(1)
    if code == "BATCH_FAIL":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"An error has occurred that wasn't caught anywhere! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"The execution of the specified batch file failed! ")
        print(colorama.Back.RED, f"this just got added and there's already a leak AAH")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
        print(colorama.Back.RED, f"Code: BATCH_FAIL                                  ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to return to UniversalCMD.")
        input()
        import UniversalCMD
    if code == "FILE_NOT_FOUND":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"An error has occurred that wasn't caught anywhere! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"A file used by UniversalCMD wasn't found,         ")
        print(colorama.Back.RED, f"UniversalCMD will not execute any further         ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
        print(colorama.Back.RED, f"Code: FILE_NOT_FOUND                              ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to exit with return code 1.")
        input()
        os._exit(1)
    if code == "CTRL_C_ATTEMPTED":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"An error has occurred that wasn't caught anywhere! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"You shouldn't exit UniversalCMD with Ctrl+C!      ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"You have to use the \"exit\" command to give        ")
        print(colorama.Back.RED, f"UniversalCMD a chance to clean temporary files!   ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to return to UniversalCMD.")
        input()
        import UniversalCMD
    if code == "UNK_ERR":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"An error has occurred that wasn't caught anywhere! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"Caught unknown error!                             ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
        print(colorama.Back.RED, f"Code: UNK_ERR                                     ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to return to UniversalCMD.")
        input()
        import UniversalCMD
    if code == "TAKE_FUNC_EXITED":
        for i in range(1, 100):    
            print(colorama.Back.RED)
        print(colorama.Back.RED, f"An error has occurred that wasn't caught anywhere! ")    
        print(colorama.Back.RED, f"                                                  ")    
        print(colorama.Back.RED, f"The core function, \"take()\", has been           ")
        print(colorama.Back.RED, f"quit unexpectedly, preventing command input!         ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Please report this in the UniversalCMD repo!      ")
        print(colorama.Back.RED, f"Code: TAKE_FUNC_EXITED                            ")
        print(colorama.Back.RED, f"What failed: {failure}                            ")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Also report what you were doing before this error.")
        print(colorama.Back.RED, f"                                                  ")
        print(colorama.Back.RED, f"Press enter to return to UniversalCMD.")
        input()
        import UniversalCMD
    print(f"UniversalCMD has crashed with an invalid error code: {code}")
    #open(f"\ucmd-crashdump.txt", "x")
    #open(f"\ucmd-crashdump.txt", "w").write(f"UniversalCMD has crashed!\n\nError code:{code}\n")
print("Initialised error handler.")