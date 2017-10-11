def percent_to_gpv(mark):
    '''
    (int) -> float
    Returns the corresponding GPV to a given percentage mark.
    REQ: 0 <= mark <= 100
    >>> percent_to_gpv(1)
    0.0
    >>> percent_to_gpv(80)
    3.7
    '''

    # Create lists defining mark bands and their corresponding GPVS.
    mark_bands = [49, 52, 56, 59, 62, 66, 69, 72, 76, 79, 84, 89, 100]
    GPV_bands = [0.0, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0,
                 4.0]
    # Create a series of if conditionals corresponding mark ranges to GPVs.
    if (mark <= mark_bands[0]):
        GPV = GPV_bands[0]
    elif (mark <= mark_bands[1]):
        GPV = GPV_bands[1]
    elif (mark <= mark_bands[2]):
        GPV = GPV_bands[2]
    elif (mark <= mark_bands[3]):
        GPV = GPV_bands[3]
    elif (mark <= mark_bands[4]):
        GPV = GPV_bands[4]
    elif (mark <= mark_bands[5]):
        GPV = GPV_bands[5]
    elif (mark <= mark_bands[6]):
        GPV = GPV_bands[6]
    elif (mark <= mark_bands[7]):
        GPV = GPV_bands[7]
    elif (mark <= mark_bands[8]):
        GPV = GPV_bands[8]
    elif (mark <= mark_bands[9]):
        GPV = GPV_bands[9]
    elif (mark <= mark_bands[10]):
        GPV = GPV_bands[10]
    elif (mark <= mark_bands[11]):
        GPV = GPV_bands[11]
    elif (mark <= mark_bands[12]):
        GPV = GPV_bands[12]
    # return GPV
    return GPV


def card_namer(value, suit):
    '''
    (str, str) -> str
    Given the value and suit of a card, real or fake, return either the full
    name of the card if it is real, or that it is a fake card if it is not.
    REQ: value and suit be single character strings.
    REQ: All letters be upper case.
    >>> card_namer("T", "D")
    '10 of Diamonds'
    >>> card_namer("13", "D")
    'CHEATER!'
    '''

    # Create a data list for the accepted chars and their corresponding meaning
    suits = ["D", "Diamonds", "C", "Clubs", "H", "Hearts", "S", "Spades"]
    # Create list of special face cards and their corresponding letters
    face = ["A", "Ace", "J", "Jack", "Q", "Queen", "K", "King", "T", "10"]
    # Create a data list for possible card values
    nums = ["2", "3", "4", "5", "6", "7", "8", "9"]
    # Create if conditionals for what each letter/number mean. Three cases:
    # If the card value is a letter and the suit is valid
    if (value in face and suit in suits):
        # Define i and n as the index number + 1 of the value and suit input
        i = suits.index(suit[:]) + 1
        n = face.index(value[:]) + 1
        # Return the name of the card
        return str(face[n] + " of " + suits[i])
    # Case 2, is if the value is a number but still valid suit
    elif (value in nums and suit in suits):
        # Define i as the index number + 1 of the suit input
        i = suits.index(suit[:]) + 1
        # Return the name of the card
        return str(value + " of " + suits[i])
    # If the card is fake, returns 'Cheater!'
    else:
        return "CHEATER!"


def my_str(string):
    '''
    (obj) -> str
    Given an object, return the string version of that object.
    >>> my_str(False)
    'NO'
    >>> my_str(43.1)
    '43.1'
    '''

    # Create case where input is a string. In which case, just return it.
    if (type(string) is str):
        result = string
    # Create a case where input is a boolean, in which case return YES or NO
    # depending on wether it is true or false.
    elif (type(string) is bool):
        if(string):
            result = "YES"
        else:
            result = "NO"
    # Create a case where the input is an integer.
    elif (type(string) is int):
        if(string <= 10):
            result = "Small Number"
        elif(string <= 99):
            result = "Medium Number"
        else:
            result = "Large Number"
    # Create a case where the input is a float, in which case round to 2
    # decimal places and return as a string.
    elif (type(string) is float):
        result = str((round(string, 2)))
    else:
        result = "I dunno"
    return result
