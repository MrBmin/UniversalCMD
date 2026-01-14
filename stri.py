def sh(arg:str):
    length = 10
    print(arg)
    if len(arg) > length + 3:
        out = arg[:length] + "..."
        return out
    else:
        return arg