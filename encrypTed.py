import secrets
import string
import re
from unidecode import unidecode

# Function to offset a letter in the alphabet (bounces back at A and Z instead of just looping around)
def offsetAlphaCharacter(charAlphaIndex, offsetRemaining, offsetDirection = "forwards", cipherMode = False):
    # Used to generate a part in the binary paragraph to indicate if the offset should be reversed to retrieve the original letter
    if cipherMode == True:
        directionReverses = 0

    if charAlphaIndex == 25:
        if offsetDirection != "backwards":
            offsetDirection = "backwards"
            if offsetRemaining != 0 and cipherMode == True:
                directionReverses += 1
        
    elif charAlphaIndex == 0:
        if offsetDirection != "forwards":
            offsetDirection = "forwards"
            if offsetRemaining != 0 and cipherMode == True:
                directionReverses += 1

    # Bounce the letter around the alphabet depending on the offset
    while offsetRemaining > 0:
        if offsetDirection == "forwards":
            if offsetRemaining > 25 - charAlphaIndex:
                offsetRemaining = offsetRemaining - (25 - charAlphaIndex)
                charAlphaIndex = 25
                offsetDirection = "backwards"
                if cipherMode == True:
                    directionReverses += 1
            else:
                charAlphaIndex = charAlphaIndex + offsetRemaining
                offsetRemaining = 0
        elif offsetDirection == "backwards":
            if offsetRemaining > charAlphaIndex:
                offsetRemaining = offsetRemaining - charAlphaIndex
                charAlphaIndex = 0
                offsetDirection = "forwards"
                if cipherMode == True:
                    directionReverses += 1
            else:
                charAlphaIndex = charAlphaIndex - offsetRemaining
                offsetRemaining = 0
    
    if cipherMode == True:
        return [charAlphaIndex, directionReverses%2]
    else:
        return charAlphaIndex

# Function to offset a number (bounces back at 0 and 9 instead of just looping around)
def offsetDigitCharacter(digit, offsetRemaining, offsetDirection = "forwards", cipherMode = False):
    digit = int(digit)

    # Used to generate a part in the binary paragraph to indicate if the offset should be reversed to retrieve the original number
    if cipherMode == True:
        directionReverses = 0

    if digit == 9:
        if offsetDirection != "backwards":
            offsetDirection = "backwards"
            if offsetRemaining != 0 and cipherMode == True:
                directionReverses += 1
        
    elif digit == 0:
        if offsetDirection != "forwards":
            offsetDirection = "forwards"
            if offsetRemaining != 0 and cipherMode == True:
                directionReverses += 1

    # Bounce the number around the alphabet depending on the offset
    while offsetRemaining > 0:
        if offsetDirection == "forwards":
            if offsetRemaining > 9 - digit:
                offsetRemaining = offsetRemaining - (9 - digit)
                digit = 9
                offsetDirection = "backwards"
                if cipherMode == True:
                    directionReverses += 1
            else:
                digit = digit + offsetRemaining
                offsetRemaining = 0
        elif offsetDirection == "backwards":
            if offsetRemaining > digit:
                offsetRemaining = offsetRemaining - digit
                digit = 0
                offsetDirection = "forwards"
                if cipherMode == True:
                    directionReverses += 1
            else:
                digit = digit - offsetRemaining
                offsetRemaining = 0
    
    if cipherMode == True:
        return [digit, directionReverses%2]
    else:
        return digit

mode = input("Do you want to 'cipher' or 'decipher': ")
regex = re.compile('[^a-zA-Z]')
mode = regex.sub('', mode).upper() # Format the input to uppercase letters only

while mode != "CIPHER" and mode != "C" and mode != "DECIPHER" and mode !="D":
    mode = input("You have to type 'cipher' or 'decipher' depending on what you want to do: ")

if mode == "CIPHER" or mode == "C": # CIPHER MODE
    # Gather inputs
    text = input("Provide the text you wish to cipher: ")

    x = secrets.randbits(10)
    while x == 0: 
        x = secrets.randbits(10)

    y = secrets.randbits(10)
    while y == 0: 
        y = secrets.randbits(10)

    uselessAmount = input("Provide the number of useless characters in the key: ")
    while not uselessAmount.isdigit():
        input("Provide the NUMBER of useless characters in the key: ")

    uselessAmount = int(uselessAmount)

    #GENERATING THE BINARY PARAGRAPH
    filteredText = unidecode(text.replace(" ", "").upper())

    # Loop to generate the random binary string + useless characters
    binaryKey = ""

    for character in filteredText:
        binaryKey = binaryKey + str(secrets.randbits(1))

    for i in range(uselessAmount):
        binaryKey = binaryKey + str(secrets.randbits(1))

    # Cipher the text
    encryptedText = ""
    isReverseBinaryList = ""

    for i in range(len(filteredText)):
        character = filteredText[i]

        if binaryKey[i] == "1": # If the corresponding binary value is 1, we use X for offset, if its 0, we use Y and reverse the direction
            if character.isalpha():
                newCharacterInfo = offsetAlphaCharacter(string.ascii_uppercase.index(character), x, "forwards", True)
                newCharacter = string.ascii_uppercase[newCharacterInfo[0]]
                isReverseBinaryCurrentChar = newCharacterInfo[1]
            elif character.isdigit():
                newCharacterInfo = offsetDigitCharacter(character, x, "forwards", True)
                newCharacter = newCharacterInfo[0]
                isReverseBinaryCurrentChar = newCharacterInfo[1]
            else:
                newCharacter = character
                isReverseBinaryCurrentChar = 0
        else:
            if character.isalpha():
                newCharacterInfo = offsetAlphaCharacter(string.ascii_uppercase.index(character), y, "backwards", True)
                newCharacter = string.ascii_uppercase[newCharacterInfo[0]]
                isReverseBinaryCurrentChar = newCharacterInfo[1]
            elif character.isdigit():
                newCharacterInfo = offsetDigitCharacter(character, y, "backwards", True)
                newCharacter = newCharacterInfo[0]
                isReverseBinaryCurrentChar = newCharacterInfo[1]
            else:
                newCharacter = character
                isReverseBinaryCurrentChar = 0
        
        encryptedText = encryptedText + str(newCharacter)
        isReverseBinaryList = isReverseBinaryList + str(isReverseBinaryCurrentChar)

    # ONLY everse the key part of the binary paragraph, add x and y binary values (length of 10 for each) and add the indicator for reversing each character or not for deciphering
    reversedBinaryKey = binaryKey[::-1]
    xBinary = f'{x:010b}'
    yBinary = f'{y:010b}'

    finalBinaryParagraph = reversedBinaryKey + xBinary + yBinary + isReverseBinaryList


    # Print the encrypted text + binary paragraph
    print("Encrypted text: " + encryptedText)
    print("Key: " + finalBinaryParagraph)

elif mode == "DECIPHER" or mode == "D": # DECIPHER MODE
    
    encryptedText = input("Provide the text you wish to decipher: ")
    encryptedText = unidecode(encryptedText.replace(" ", "").upper()) # Makes sure the code won't break if the user inputs weird stuff | probably not fully secure, did not test crazy characters

    binaryParagraph = input("Provide the binary paragraph: ")
    while not binaryParagraph.isdigit():
        print("The binary paragraph is the one composed of 1s and 0s.")
        binaryParagraph = input("Provide the binary paragraph: ")


    # Read x, y and the reverse indicator part
    isReverseBinaryList = binaryParagraph[-len(encryptedText):]
    x = int(binaryParagraph[-len(encryptedText)-20:-len(encryptedText)-10], 2)
    y = int(binaryParagraph[-len(encryptedText)-10:-len(encryptedText)], 2)

    # Remove that stuff and reverse the key part of the paragraph
    binaryKey = binaryParagraph[:-len(encryptedText)-20][::-1]

    # Decipher the text
    decryptedText = ""

    for i in range(len(encryptedText)):
        character = encryptedText[i]

        if binaryKey[i] == "1": # Same as ciphering except everything is reversed
            if character.isalpha():
                if isReverseBinaryList[i] == "1":
                    newCharacter = string.ascii_uppercase[offsetAlphaCharacter(string.ascii_uppercase.index(character), x)]
                else:
                    newCharacter = string.ascii_uppercase[offsetAlphaCharacter(string.ascii_uppercase.index(character), x, "backwards")]
                
            elif character.isdigit():
                if isReverseBinaryList[i] == "1":
                    newCharacter = offsetDigitCharacter(character, x)
                else:
                    newCharacter = offsetDigitCharacter(character, x, "backwards")
            else:
                newCharacter = character
        else:
            if character.isalpha():
                if isReverseBinaryList[i] == "1":
                    newCharacter = string.ascii_uppercase[offsetAlphaCharacter(string.ascii_uppercase.index(character), y, "backwards")]
                else:
                    newCharacter = string.ascii_uppercase[offsetAlphaCharacter(string.ascii_uppercase.index(character), y)]
                
            elif character.isdigit():
                if isReverseBinaryList[i] == "1":
                    newCharacter = offsetDigitCharacter(character, y, "backwards")
                else:
                    newCharacter = offsetDigitCharacter(character, y)
            else:
                newCharacter = character
        
        decryptedText = decryptedText + str(newCharacter)

    # Print the results
    print("Decrypted text: " + decryptedText)
input("Press enter to exit.")