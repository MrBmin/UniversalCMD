import os
import requests
import handler
import textwrap
import time
import colorama
import random



def install(feature:str):
    print(colorama.Back.BLUE)
    print(f"Attempting to find feature \"{feature}\"")
    url = f"https://raw.githubusercontent.com/MrBmin/UniversalCMD/refs/heads/optional-features/{feature}.py"

    req = requests.get(url)


    if req.status_code == 200:
        if feature == "e2u":
            print("\n!WARNING!\nThe specified optional feature, \"e2u\", rather than being a command, replaces UniversalCMD entirely! And still has some bugs I can't fix for some reason along with no option to go back.\nThe installation process involves erasing UniversalCMD, and THEN replacing it with E2U mode. Proceed with extra caution.")
        print(f"GitHub returned status code 200 (OK), downloading \"{feature}\"")
        print("Installation: [#---------] 05% complete")
        with open(f"download.py", "wb") as f:
            f.write(req.content)
        print("Installation: [#---------] 12% complete")
        print(f"\n\"{feature}\" downloaded, are you sure you want to install this at the risk of corrupting UniversalCMD? (y/n)")
        t = input()
        if t == "y":
            
            print("UniversalCMD will now install this feature, although this should take a few seconds, please do not interrupt the installation")
            #I know this looks meaningless, but making progress bars take longer than they should make the user trust it more
            try:
                if feature not in ["e2u"]:
                    with open("UniversalCMD.py", "r") as f:
                        with open("download.py", "r") as f2:
                            print("Installation: [##--------] 20% complete")
                            time.sleep(0.3)
                            temp = f.read()
                            temp = temp.replace(f"#{feature} feature", "if f\"{cmd0}\"==\""+feature+"\":\n"+textwrap.indent(f2.read(), "            ")+"\n            take()")
                            print("Installation: [####------] 35% complete")
                            time.sleep(0.3)
                    with open("UniversalCMD.py", "w") as f:
                        f.write(temp)
                        print(f"Installation: [#####-----] {random.randint(45, 54)}% complete")                    
                        time.sleep(random.random() % 1)
                        print(f"Installation: [######----] {random.randint(56, 64)}% complete")
                        time.sleep(random.random() % 1)
                        print(f"Installation: [########--] {random.randint(76, 84)}% complete")
                        time.sleep(random.random() % 1)
                        print(f"Installation: [##########] 99% complete")
                        time.sleep(4)
                        print(colorama.Back.BLACK)
                else:
                    with open("UniversalCMD.py", "w") as f:
                        with open("download.py", "r") as f2:
                            print("Installation: [##--------] 20% complete")
                            time.sleep(0.3)
                            temp = f2.read()
                            print("Installation: [####------] 35% complete")
                            time.sleep(0.3)
                    with open("UniversalCMD.py", "w") as f:
                        f.write(temp)
                        print(f"Installation: [#####-----] {random.randint(45, 54)}% complete")                    
                        time.sleep(random.random() % 1)
                        print(f"Installation: [######----] {random.randint(56, 64)}% complete")
                        time.sleep(random.random() % 1)
                        print(f"Installation: [########--] {random.randint(76, 84)}% complete")
                        time.sleep(random.random() % 1)
                        print(f"Installation: [##########] 99% complete")
                        time.sleep(4)
                        print(colorama.Back.BLACK)
                    print(f"Installed \"{feature}\", you may now return to UniversalCMD, although you need to properly restart it to use the feature.")
            except BaseException as err:
                handler.handle("FEATURE_INSTALLATION_FAILURE", f"Installing \"{feature}\" has failed, UniversalCMD may now be corrupted!!", f"installer.py and {feature}.py")
            os.remove("download.py")
        else:
            print(colorama.Back.BLACK)
            import UniversalCMD
    else:
        print(colorama.Back.BLACK)
        print(f"\nCouldn't fetch \"{feature}\", GitHub returned status code {req.status_code}")

def e2u_install():
    print(colorama.Back.BLUE)
    print("Sorry, but at the time of E2U mode's release, there's no optional features available for it.\nI've been working really hard on regular E2U mode and\n I can't be bothered to make any E2U optional features.\n\nEverything between v1.1.0a pre-alpha and v1.1.1 pre-alpha will purely just be bugfixing\n(and optional features for vanilla UniversalCMD). E2U optional features will be in v1.1.0 pre-alpha.")
    input()
