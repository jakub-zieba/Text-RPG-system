import re

def main():
    print("welcome to this simple toy")

    run = True

    while run:  
        equasion = input("PLease provide the calculation to perform, the string must not include '='.\n Write h for help...\n")
        if equasion == "h":
            printhelp()
        elif equasion == "e" or equasion == "^D":
            run = False
        elif re.search("=", equasion):
            print("Error, '=' given") 
            run = False
        else:
            performMath(equasion)

def performMath(equasion):
    #normalize the equasion
    equasion = re.sub('[a-zA-Z,.:()" "]', '', equasion)
    print(f"Normalized equasion: {equasion}")
    print(f"{equasion} = {eval(equasion)}")



def printhelp():
    print("Provide these for the program to perform:\n e, ^D to exit.\n h for help")

main()