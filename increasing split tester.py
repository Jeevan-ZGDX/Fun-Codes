

def split_tester(N, d):
    #Your code for split_tester function goes here (instead of keyword pass)
    #Your code should include docstrings and the body of the function
    """
        (string, string) -> bool
        precondition: both N and d must be positive integers such that N%d==0

        The function splits the given string N into a sequence of d length integers then prints them to the screen sepe
        It then return True if the sequence is strictly increasing, otherwise it returns False.
    """
    lastNum = -1
    checkInc = True
    seq = ''
    d = int(d)

    for i in range(0,len(N), d):
        newNum = N[i:i+d]
        seq += newNum

        if int(newNum) < lastNum:
            checkInc = False

        lastNum = int(newNum)

        if i < len(N)-d:
            seq += ', '

    print(seq)

    return checkInc

#You can add more function definitions here if you like
def ascii_name_plaque(name): #Taken from Assignments 1
    """
        (string) -> None

        Displays to the screen a name plaque with the given name padded by 1 space
        inside a box of stars with underscores before and after the name
    """
    newStr = "*__" + name + "__*"
    stars = len(newStr)

    print("*" , stars)
    print("* " + (stars-3)* ' '+ "*")
    print(newStr)



# main
# Your code for the welcome message goes here, instead of name="Vida"
print()
ascii_name_plaque("Welcome to my increacing-splits tester")
print()
name = input("What is your name? ").strip()
print()
ascii_name_plaque(name + ", welcome to my increasing-strips tester.")
print()


flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-splits of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
        #YOUR CODE GOES HERE. The next line should be elif or else.
    elif question=='yes':
        print('Good choice!')

        N = input("Enter a positive integer: ").strip().replace(',','')
        if len(N) > 1:
            x = 1
        else:
            x = 0

        if N.isdigit() or (N[0] == '-' and N[x:].isdigit()):
            if int(N) > 0:
                print("Input the split. The split has to divide the length of, " + N + " i.e" + str(len(N)))
                d = input().strip().replace(',','')
                if d.isdigit():
                    if int(d) > 0:
                        if len(N)%int(d)==0:
                            isInc = split_tester(N,d)
                            if isInc:
                                print("The sequence is increasing")
                            else:
                                print("The sequence is Not increasing")
                        else:
                            print(d + ' does not divide ' + str(len(N)) + '. Try again')
                    else:
                        print("The input has to be a positive integer. Try again")
                else:
                    print('The input can only contain digits. Try again.')
            else:
                print("The input has to be a positive integer. Try again.")
        else:
            print('The input can only contain digits. Try again.')
    else:
        print("Please enter yes or no. Try again.")
#finally your code goes here too.
print()
ascii_name_plaque("Good bye" + name + '!')
print()
