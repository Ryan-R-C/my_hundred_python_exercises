c = ('\033[m',        #0 - no colors
     "\033[0;30;41m", #1 - red
     "\033[0;30;42m", #2 - green
     "\033[0;30;43m", #3 - yellow
     "\033[0;30;44m", #4 - blue
     "\033[0;30;45m", #5 - purple
     "\033[0;30;46m", #6 - cyan
     "\033[7;30m",    #7 - white
     "\033[0;30;48m", #8 - black
)


def helpa(com):
    title(f'Manual of \'{com}\':', 1)
    print(c[7], end="")
    help(com)
    print(c[0], end="")


def title(msg, color=0):
    sz = len(msg) + 2
    print(c[color], end="")
    print("~"*sz)
    print(f" {msg} ")
    print("~"*sz)
    print(c[0], end="")


comand = ''
while True:
    title("Help's sistem PyHelp",color=4)
    comand = str(input("Function or Library > "))
    if comand.upper() == "END":
        break
    else:
        helpa(comand)

title("By", 1)