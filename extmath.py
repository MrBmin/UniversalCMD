import math

try:
    #square root
    if cmd1 == "-sqrt":
        print(math.sqrt(cmd2))

    #exponentiation (extmath -exp a b = a^b)
    if cmd1 == "-exp":
        print(math.exp(cmd2, cmd3))

    if cmd1 == "-?":
        print("extmath -sqrt a - Returns the square root of a\nextmath -exp a b - Returns a raised to the power of b\nextmath -ctn a - Counts to a (e.g. extmath -ctn 5 outputs 1, 2, 3, 4, 5)")

    #counts to n (extmath -ctn 10 outputs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    if cmd1 == "ctn":
        for i in range(cmd2):
            print(f"{i}", end="")
            if not i == cmd2:
                print(", ", end="")
    

except:
    print("One or more arguments were not numbers!")