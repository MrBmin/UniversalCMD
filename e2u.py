try:
    import os
    import colorama
    try:
        import handler
    except:
        for i in range(1, 100):    
            print(colorama.Back.RED)
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
        import installer
    except:
        handler.handle("FILE_NOT_FOUND", "UniversalCMD could not find an essential file!", "installer.py")
    import time   
    try:
        import readchar
        from readchar import key
    except:
        print("UniversalCMD E2U mode requires the \"readchar\" library to detect key presses\nwithout you pressing enter every time, press enter to exit UniversalCMD, type\n\"pip install readchar\" in the terminal, and try again.")
        input()
        handler.handle("FORCE_EXIT", "A required library for E2U mode is not installed!", "UniversalCMD.py")
    try:
        open("options.json")
    except:
        handler.handle("OPTIONS_NOT_FOUND", "UniversalCMD could not find an essential file!", "options.json")   
    
    #main background
    bg = colorama.Back.LIGHTCYAN_EX
    #window shadow on the background
    ws = colorama.Back.BLUE
    #main foreground
    fg = colorama.Fore.WHITE
    #window background
    wbg = colorama.Back.LIGHTBLACK_EX
    #title bar background
    tbg = colorama.Back.BLACK
    #selection background
    sbg = colorama.Back.WHITE
    #selection foreground
    sfg = colorama.Fore.BLACK
    #dangerous option foreground
    dfg = colorama.Fore.RED
    #resets all colours to terminal default (traditionally black background, white text)
    reset = colorama.Back.RESET + colorama.Fore.RESET

    depth = 1
    selection = 0
    version = "1.1.0 PRE-ALPHA 10/APR/2026"
    def debug():
        global depth
        depth += 1
        inp = input(colorama.Back.RESET + "DEBUG>")
        if inp == "vars":
            print(f"Variable check\n\nselection = {selection}\nversion = \"{version}\"\nbg =", bg, colorama.Back.RESET, "wbg =", wbg, colorama.Back.RESET, "tbg =", tbg, colorama.Back.RESET, "sbg =", sbg, colorama.Back.RESET, "\nfg =", fg, "text", colorama.Fore.RESET, "sfg= ", sfg, "text", colorama.Fore.RESET, "dfg =", dfg, "text", colorama.Fore.RESET)
        if inp == "exit":
            return
        if inp == "forceexit":
            inp = input("Why? >")
            handler.handle("FORCE_EXIT", f"The call came from within E2U's debug,\nThe user specified this reason: {inp}", "UniversalCMD.py")
        if inp == "bg":
            bg == colorama.Back.GREEN
        if inp == "help":
            print("\nDebug help list (in the order in which they are defined in the code)\nvars - provides a debug variable check\nexit - returns to e2u mode\nforceexit - used to forcibly exit UniversalCMD if the code is stuck in a loop")
        debug()
    
    
    global current_window
    def render(current_window:str | None = "UniversalCMD", delay_per_line:float | None = 0.0): #i was thinking of calling this function "main()" as if this was c or something
        global selection
        global depth
        global bg
        global ws
        if len(current_window) > 100: #its probably going to be very hard to see this error, but its good to have a fallback
            print("The name of the current window exceeded the length of E2U mode's rendering (100 characters long)\nPress enter to close the current window.")
            input()
            render()
        for i in range(100):
            print(colorama.Back.RESET)
        print(f"{tbg}{current_window} {sbg}{sfg}  ↑/↓ arrow keys to choose, enter to select, shift + i for information about the current window", bg)
        time.sleep(delay_per_line)
    
        #UniversalCMD Selection Menu
        if current_window == "UniversalCMD":
            print(bg, fg)
            for i in range(3):
                print()
                time.sleep(delay_per_line)
            print("                       ", tbg, fg, f"UniversalCMD Selection Menu           v{version}", bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "                                                                  ", ws, bg)
            time.sleep(delay_per_line)
            if selection == 0:
                print("                       ", sbg, sfg, "Actions                                                           ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "Actions                                                           ", ws, bg)
                time.sleep(delay_per_line)
            if selection == 1:
                print("                       ", sbg, dfg, "Options                                                           ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, dfg, "Options                                                           ", ws, bg)
                time.sleep(delay_per_line)
            if selection == 2:
                print("                       ", sbg, sfg, "Close (Exits UniversalCMD)                                        ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "Close (Exits UniversalCMD)                                        ", ws, bg)
                time.sleep(delay_per_line)
            print("                        ", ws, "                                                                   ", bg)
            time.sleep(delay_per_line)
            
            if readchar.readchar() == ",":
                selection -= 1
            if readchar.readchar() == ".":
                selection += 1
            if readchar.readchar() == "\n":
                if selection == 2:
                    for i in range(100):
                        print(colorama.Back.RESET)
                    os._exit(0)
                if selection == 0:
                    render("Actions")
                if selection == 1:
                    render("Options")
            if readchar.readchar() == "d":
                
                debug()
            if readchar.readchar() == "I":
                render("About: UniversalCMD Selection Menu")
            render(current_window, delay_per_line)
        if current_window == "Actions":
            print("                       ", tbg, fg, "UniversalCMD Actions                                              ", bg)
            print("                       ", wbg, dfg, "This is under development, expect bugs and not many features      ", ws, bg)
            print("                       ", wbg, fg, "Commands                                                          ", ws, bg)
            if selection == 0:
                print("                       ", sbg, sfg, "   calc                                                           ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "   calc                                                           ", ws, bg)
                time.sleep(delay_per_line)
            if selection == 1:
                print("                       ", sbg, sfg, "   install                                                        ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "   install                                                        ", ws, bg)
            if selection == 2:
                print("                       ", sbg, sfg, "   install                                                        ", ws, bg)
                time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "   install                                                        ", ws, bg)
                time.sleep(delay_per_line)
            print("                        ", ws, "                                                                   ", bg)
            if readchar.readchar() == "\n":
                for i in range(100):
                   print(colorama.Back.RESET)
                print(f"{tbg}{current_window} {sbg}{sfg}  ↑/↓ arrow keys to choose, enter to select, shift + i for information about the current window", bg)
                time.sleep(delay_per_line)
                print("                       ", tbg, fg, "UniversalCMD Actions                                              ", bg)
                print("                       ", wbg, fg, "Commands                                                          ", ws, bg)
                if selection == 0:
                    print("                       ", sbg, sfg, "   calc                                                           ", ws, bg)
                    time.sleep(delay_per_line)
                else:
                    print("                       ", wbg, fg, "   calc                                                           ", ws, bg)
                    time.sleep(delay_per_line)
                if selection == 1:
                    print("                       ", sbg, sfg, "   install                                                        ", ws, bg)
                    time.sleep(delay_per_line)
                else:
                    print("                       ", wbg, fg, "   install                                                        ", ws, bg)
                    time.sleep(delay_per_line)
            else:
                print("                       ", wbg, fg, "   install                                                        ", ws, bg)
                if selection == 0:
                    installer.e2u_install()
                if selection == 0:
                    print("                       ", wbg, fg, "                                                                  ", ws, bg)
                    print("                       ", wbg, fg, "Command is requesting input                                       ", ws, bg)
                    print("                        ", ws, "                                                                   ", bg)
                    print(reset)
                    op = input("What operation do you want to do? (+, -, /, *) >")
                    a = None
                    if not op in ["+", "-", "/", "*"]:
                        output = "Invalid operation!"
                    elif op == "+":
                        n1 = input("Type number 1 >")
                        try:
                            a = float(n1)
                        except:
                            output = "Number 1 wasn't a number"
                        n2 = input("Type number 2 >")
                        try:
                            a = float(n2)
                        except:
                            output = "Number 2 wasn't a number"
                        #i have to have a seperate case if a is 0 because
                        #if a is 0 it just wont execute
                        #it wont execute if:
                        #
                        #a == None
                        #a == 0
                        #a == ""
                        #or a isnt defined, where it just throws an error
                        #(in the case of universalcmd, triggers the error handler)
                        if a or a == 0:
                            output = f"{n1} + {n2} = {float(n1) + float(n2)}"
            for i in range(100):
                print(colorama.Back.RESET)
            print(f"{tbg}{current_window} {sbg}{sfg}  ↑/↓ arrow keys to choose, enter to select, shift + i for information about the current window", bg)
            time.sleep(delay_per_line)
            print("                       ", tbg, fg, "Command output                                    ", bg)
            temp = ""
            for i in range(50 - len(str(output))):
                temp += " "
            print("                       ", wbg, fg, "                                                  ", ws, bg)
            print("                       ", wbg, fg, str(output) + temp, ws, bg)
            print("                       ", wbg, fg, "                                                  ", ws, bg)
            print("                       ", sbg, sfg, "Press any key to go back                          ", ws, bg)
            print("                        ", ws, "                                                  ", ws, bg)
            readchar.readkey()
            render()
        #About: UniversalCMD Selection Menu
        #
        #compilation numbers work like this:
        #compilation YYWW/N
        #
        #YY is the current year in two digits
        #WW is the n-th week of the year (monday as the first day) (+ leading zero)
        #N is 1, although every time another compilation is compiled, it goes up until the next MONDAY
        #
        #the first public version (publicised on 4th jan 2026) would've been
        #v1.0.1 pre-alpha (compilation 2602/1)
        #rather than
        #v1.0.1 pre-alpha 04/JAN/2026
    
        if current_window == "About: UniversalCMD Selection Menu":
            print(bg, fg)
            for i in range(3):
                print()
                time.sleep(delay_per_line)
            print("                       ", tbg, fg, f"About: UniversalCMD Selection Menu                                ", bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "                                                                  ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "UniversalCMD Selection Menu v1.1.0 pre-alpha                      ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "Compilation 2614/1 (03/APR/2026)                                  ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "                                                                  ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "Description:                                                      ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", sbg, sfg, "UniversalCMD E2U Mode, an easier to understand and use version    ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", sbg, sfg, "of UniversalCMD. This project is open-source on GitHub, and you   ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", sbg, sfg, "may contribute.                                                   ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "                                                                  ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "Fun fact: this mode was inspired by another project I made for    ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "fun in 2024, although I lost motivation after about a month       ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "                                                                  ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "This window was written with minimal A.I. involvement,            ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "A.I. will only be used for if I'm really stuck on something,      ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", wbg, fg, "but A.I. code will NEVER be directly implemented whatsoever.      ", ws, bg)
            time.sleep(delay_per_line)
            print("                       ", sbg, sfg, "Back                                                              ", ws, bg)
            print("                        ", ws, "                                                                   ", bg)
            if readchar.readchar() == "\n":
                render()
        
        #Options
        if current_window == "Options":
            print(bg, fg)
            for i in range(3):
                print()
            print("                       ", tbg, fg, f"Options                                                          ", bg)
            print("                       ", wbg, fg, "                                                                 ", ws, bg)
            if selection == 0:
                print("                       ", sbg, sfg, "Background colour                                                ", ws, bg)
            else:
                print("                       ", wbg, fg, "Background colour                                                ", ws, bg)
            if selection == 1:
                print("                       ", sbg, dfg, "Debug                                                            ", ws, bg)
            else:
                print("                       ", wbg, dfg, "Debug                                                            ", ws, bg)
            if selection == 2:
                print("                       ", sbg, sfg, "Close                                                            ", ws, bg)
            else:
                print("                       ", wbg, fg, "Close                                                            ", ws, bg)
            print("                        ", ws, "                                                                  ", bg)
            
            if readchar.readkey() == ",":
                selection -= 1
            if readchar.readchar() == ".":
                selection += 1
            if readchar.readchar() == "\n":
                if selection == 2:
                    for i in range(100):
                        print(colorama.Back.RESET)
                    render()
                if selection == 0:
                    render("Options (Background Colour)")
            if readchar.readchar() == "d":
                
                debug()
            render(current_window, delay_per_line)
    
        #Options: Background colour
        if current_window == "Options (Background Colour)":
            print(bg, fg)
            for i in range(3):
                print()
            print("                       ", tbg, fg, f"Options                                         Background Colour", bg)
            print("                       ", wbg, fg, "                                                                 ", ws, bg)
            if selection == 0:
                print("                       ", sbg, sfg, "Blue                                                             ", ws, bg)
            else:
                print("                       ", wbg, fg, "Blue                                                             ", ws, bg)
            if selection == 1:
                print("                       ", sbg, sfg, "Green                                                            ", ws, bg)
            else:
                print("                       ", wbg, fg, "Green                                                            ", ws, bg)
            if selection == 2:
                print("                       ", sbg, sfg, "Red                                                              ", ws, bg)
            else:
                print("                       ", wbg, fg, "Red                                                              ", ws, bg)
            if selection == 3:
                print("                       ", sbg, dfg, "Back                                                            ", ws, bg)
            else:
                print("                       ", wbg, dfg, "Back                                                             ", ws, bg)
            print("                        ", ws, "                                                                  ", bg)
            
            if readchar.readchar() == ",":
                selection -= 1
            if readchar.readchar() == ".":
                selection += 1
            if readchar.readchar() == "\n":
                if selection == 3:
                    render("Options")
                if selection == 2:
                    with open("options.json", "r") as f:
                        temp = f.read()
                        temp.replace(f"\"e2u_bg\": \"{bg}\"", f"\"e2u_bg\": \"colorama.Back.LIGHTRED_EX\"")
                        temp.replace(f"\"e2u_ws\": \"{ws}\"", f"\"e2u_ws\": \"colorama.Back.RED\"")
                    with open("options.json", "w") as f:
                        print(colorama.Back.RESET, colorama.Fore.RESET, "\nDEBUG>\nSaving changes...")
                        time.sleep(1)
                        f.write(temp)
                    bg = colorama.Back.LIGHTRED_EX
                    ws = colorama.Back.RED
                    render(current_window, delay_per_line)
                if selection == 1:
                    bg = colorama.Back.LIGHTGREEN_EX
                    ws = colorama.Back.GREEN
                if selection == 0:
                    bg = colorama.Back.LIGHTCYAN_EX
                    ws = colorama.Back.BLUE
            if readchar.readchar() == "d":
                
                debug()
            render(current_window, delay_per_line)
    
        for i in range(3):
            print(bg)
            render(current_window, delay_per_line)
        print(colorama.Back.RESET, colorama.Fore.RESET)
        time.sleep(delay_per_line)
        print("RENDERING HAS FAILED, A DEBUG VARIABLE CHECK WILL NOW BE DISPLAYED")
        time.sleep(delay_per_line)
        print(f"Variable check\n\nselection = {selection}\nversion = \"{version}\"\nbg =", bg, colorama.Back.RESET, "wbg =", wbg, colorama.Back.RESET, "tbg =", tbg, colorama.Back.RESET, "sbg =", sbg, colorama.Back.RESET, "\nfg =", fg, "text", colorama.Fore.RESET, "sfg= ", sfg, "text", colorama.Fore.RESET, "dfg =", dfg, "text", colorama.Fore.RESET)
        time.sleep(delay_per_line)
        handler.handle("E2U_RENDER_FAILURE", "UniversalCMD has failed to render something!", "UniversalCMD.py")
    
    render()
    
except RecursionError:
    print(f"UniversalCMD has encountered a serious error, pay attention to the red screen ahead!")
    time.sleep(4)
    for i in range(1, 100):    
        print(colorama.Back.RED)
    print(f"A near-unavoidable error has occurred! ")    
    print(f"                                                  ")    
    print(f"Python has a function limit of 1000 functions     ")
    print(f"nested within eachother, at the moment,           ")
    print(f"this limit has been reached, and there's nothing  ")
    print(f"to do but exit or crash.                          ")
    print(f"                                                  ")
    print(f"This may have happened naturally, or rendering    ")
    print(f"has failed, and got stuck in an infinite loop due ")
    print(f"to a typo in the code I haven't found.            ")
    print(f"Seriously, code typos can be this fatal!          ")
    print(f"                                                  ")
    print(f"UniversalCMD will now exit in order to prevent    ")
    print(f"an unavoidable exception.                         ")
    print(f"                                                  ")
    print(f"Code: MAX_FUNC_DEPTH_NEARBY                       ")
    print(f"What failed: the limitations of computing         ")
    # what else was i supposed to put for the "what failed" bit?
    print(f"                                                  ")
    print(f"Press enter to forcibly exit.")
    input()
    os._exit(1)
except NameError as err:
    handler.handle("UNK_VAR", err)
except BaseException as err:
    handler.handle("UNK_ERR", err)