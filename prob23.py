forcount = int(input()) #counts first line of code to run for loop
punctuations = "'!()-[]{};:\,<>./?@#$%^&*_~" #list of punctuation to remove

for i in range(0, forcount):#for loop that runs everything
    string = input() #takes input
    string = string.lower() #makes string lowercase
    unpunct = '' #blank string for later
    for char in string: #for loop that removes all punctuation by checkin if it is in the punctuation string
        if char not in punctuations:
            unpunct = unpunct + char
    reverse = unpunct[::-1] #reverses the string
    swap = ''
    for char in reverse:
        if char == 'a':
            swap = swap + 'e'
        elif char == 'e':
            swap = swap + 'a'
        elif char == 'b':
            swap = swap + 'q'
        elif char == 'q':
            swap = swap + 'b'
        elif char == 'd':
            swap = swap + 'p'
        elif char == 'p':
            swap = swap + 'd'
        elif char == 'h':
            swap = swap + 'y'
        elif char == 'y':
            swap = swap + 'h'
        elif char == 'm':
            swap = swap + 'w'
        elif char == 'w':
            swap = swap + 'm'
        elif char == 'u':
            swap = swap + 'n'
        elif char == 'n':
            swap = swap + 'u'
        else:
            swap = swap + char
    unspaced = swap.replace(' ', '')
    unspaced2 = unpunct.replace(' ', '')
    if unspaced == unspaced2:
        print(unpunct, "(is)", swap)
    else:
        print(unpunct, "(not)", swap)
    